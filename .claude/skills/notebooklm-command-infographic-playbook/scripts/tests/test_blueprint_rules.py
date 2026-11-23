"""check-blueprint: connection counts, the 16:9 step-label warnings and the shared fixtures."""

from __future__ import annotations

import copy
from typing import Any

import pytest
from blueprint_fixtures import FIXTURE_NAMES, WIDE_WARNING_FIXTURES, load_fixture
from conftest import BLUEPRINT_SEED, Project, load_register_tool, result_json


def check(project: Project, blueprint: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    project.write_blueprint(blueprint)
    completed = project.run("check-blueprint", "compact")
    return completed.returncode, result_json(completed)


def test_fixture_set_is_the_agreed_one() -> None:
    assert FIXTURE_NAMES == [
        "five-words-16x9",
        "minimal-16x9",
        "seed-16x9",
        "seed-4x5",
        "stress-16x9",
        "stress-4x5",
        "worst-16x9",
        "worst-4x5",
    ]


@pytest.mark.parametrize("name", FIXTURE_NAMES)
def test_every_fixture_passes_check_blueprint(project: Project, name: str) -> None:
    code, report = check(project, load_fixture(name))
    assert (code, report["ok"], report["errors"]) == (0, True, [])
    expects_warning = name in WIDE_WARNING_FIXTURES
    assert bool(report["warnings"]) is expects_warning


def mutated(mutate: Any) -> dict[str, Any]:
    blueprint = copy.deepcopy(BLUEPRINT_SEED)
    mutate(blueprint)
    return blueprint


RELATED = {"command": "/clear", "label": "Recomeça com contexto vazio"}
FLAG = {"text": "[instruções]", "label": "Diz o que o resumo preserva"}


@pytest.mark.parametrize(
    ("mutate", "path"),
    [
        (lambda bp: bp["connections"].update(related=[]), "connections.related"),
        (lambda bp: bp["connections"].update(related=[RELATED] * 4), "connections.related"),
        (lambda bp: bp["connections"].update(flags=[FLAG] * 4), "connections.flags"),
        (lambda bp: bp["connections"].update(files=[FLAG] * 4), "connections.files"),
    ],
)
def test_connection_counts_out_of_range_are_errors(project: Project, mutate: Any, path: str) -> None:
    code, report = check(project, mutated(mutate))
    assert code == 1
    assert any(error.startswith(path) and "items" in error for error in report["errors"])


@pytest.mark.parametrize(
    "mutate",
    [
        lambda bp: bp["connections"].update(related=[RELATED]),
        lambda bp: bp["connections"].update(flags=[], files=[]),
        lambda bp: bp["connections"].update(flags=[FLAG] * 3, files=[FLAG] * 3),
    ],
)
def test_connection_counts_in_range_pass(project: Project, mutate: Any) -> None:
    code, report = check(project, mutated(mutate))
    assert (code, report["errors"]) == (0, [])


@pytest.mark.parametrize("words", [6, 7])
def test_wide_step_labels_over_five_words_warn_without_failing(project: Project, words: int) -> None:
    label = " ".join(["palavra"] * words)
    code, report = check(project, mutated(lambda bp: bp["flow"]["steps"][1].update(label=label)))
    assert (code, report["ok"]) == (0, True)
    assert len(report["warnings"]) == 1
    assert "flow.steps[1]" in report["warnings"][0]
    assert str(words) in report["warnings"][0]


def test_five_word_step_labels_do_not_warn(project: Project) -> None:
    code, report = check(project, copy.deepcopy(BLUEPRINT_SEED))
    assert (code, report["warnings"]) == (0, [])


def test_tall_step_labels_never_warn(project: Project) -> None:
    def seven_words(blueprint: dict[str, Any]) -> None:
        blueprint["aspect"] = "4:5"
        blueprint["flow"]["steps"][1]["label"] = " ".join(["palavra"] * 7)

    code, report = check(project, mutated(seven_words))
    assert (code, report["warnings"]) == (0, [])


def test_failed_check_reports_empty_warnings(project: Project) -> None:
    code, report = check(project, mutated(lambda bp: bp["connections"].update(related=[])))
    assert (code, report["warnings"]) == (1, [])


@pytest.mark.parametrize(
    ("command", "example", "ok"),
    [
        ("/design-consent", "/design consent", True),
        ("/design-consent", "/design-consent", True),
        ("/compact", "/compact mantenha testes", True),
        ("/design-consent", "/design revoke", False),
        ("/compact", "/clear", False),
    ],
)
def test_example_may_type_a_subcommand_id_with_a_space(command: str, example: str, ok: bool) -> None:
    tool = load_register_tool()
    contrast = {"when": ["Antes de pedir o acesso"], "pitfalls": ["Só você digita o comando"], "example": example}
    errors = tool._contrast_errors(contrast, command)
    assert ("contrast.example must start with the command" not in errors) is ok
