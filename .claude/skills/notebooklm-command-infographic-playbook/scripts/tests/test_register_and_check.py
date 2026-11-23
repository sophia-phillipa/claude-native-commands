"""Tests for infographic-register-tool.py: every subcommand of contract section 8, on fixture project roots."""

from __future__ import annotations

import copy
import io
import json
import re
import stat
import struct
import subprocess
import sys
import zlib
from pathlib import Path
from typing import Any

import pytest
from conftest import (
    BLUEPRINT_SEED,
    PAGE_FIXTURE,
    SCRIPT_PATH,
    TEMPLATE_FIXTURE,
    Project,
    load_register_tool,
    result_json,
    seed_strings,
    standalone_wrapper,
    vector_html,
)
from PIL import Image

rc = load_register_tool()

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
SLOT_PATTERN = re.compile(r'<script type="application/json" id="blueprint">(.*?)</script>', re.DOTALL)
INFOGRAPHICS_BLOCK = re.compile(r"const INFOGRAPHICS = (.*?);\n/\* INFOGRAPHICS:END", re.DOTALL)
VECTOR_KEYS = {"expected", "found", "location", "issue_type"}
WEBP_PATH = "assets/infographics/compact/infographic.webp"
PNG_PATH = "assets/infographics/compact/infographic.png"
DOWNLOAD_PATH = "assets/infographics/compact/infographic-1920.png"
PAGE_UNDER_TEST = Path(__file__).resolve().parents[5] / "src" / "comandos-nativos.html"


def write_png_stub(path: Path, body: bytes = b"stub") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(PNG_SIGNATURE + body)


def write_real_png(path: Path, size: tuple[int, int] = (96, 54)) -> None:
    """A decodable RGBA PNG of a non-square size: the register converts it, so a stub is not enough."""
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGBA", size, (31, 41, 110, 255)).save(path, "PNG")


def snapshot(project: Project, name: str = "snap.json") -> Path:
    out = project.root.parent / name
    completed = project.run("snapshot-downloads", "--out", str(out))
    assert completed.returncode == 0, completed.stdout
    return out


def page_block(project: Project) -> dict[str, Any]:
    match = INFOGRAPHICS_BLOCK.search(project.page_source.read_text(encoding="utf-8"))
    assert match is not None
    return json.loads(match.group(1))


# ---------------------------------------------------------------- check-blueprint


def test_check_blueprint_accepts_contract_seed(project: Project) -> None:
    project.write_blueprint()
    completed = project.run("check-blueprint", "compact")
    assert completed.returncode == 0, completed.stdout
    assert result_json(completed)["ok"] is True


@pytest.mark.parametrize(
    ("mutate", "word"),
    [
        (lambda bp: bp.update(category="Outra categoria"), "category"),
        (lambda bp: bp["flow"]["steps"][0].update(label="Uma duas três quatro cinco seis sete oito"), "label"),
        (lambda bp: bp["flow"]["edges"][0].update({"to": "s3"}), "edge"),
        (lambda bp: bp["identity"].update(purpose=" Resume a conversa."), "purpose"),
        (lambda bp: bp["connections"]["related"][0].update(command="/nope"), "related"),
        (lambda bp: bp["contrast"].update(example="Mantenha /compact"), "example"),
        (lambda bp: bp["ui"].update(zone1="Outro título"), "zone1"),
    ],
)
def test_check_blueprint_rejects_contract_violations(project: Project, mutate: Any, word: str) -> None:
    blueprint = copy.deepcopy(BLUEPRINT_SEED)
    mutate(blueprint)
    project.write_blueprint(blueprint)
    completed = project.run("check-blueprint", "compact")
    assert completed.returncode == 1
    report = result_json(completed)
    assert report["ok"] is False
    assert word in " ".join(report["errors"]).lower()


def test_check_blueprint_missing_file_is_json_failure(project: Project) -> None:
    completed = project.run("check-blueprint", "compact")
    assert completed.returncode == 1
    assert result_json(completed)["ok"] is False
    assert "Traceback" not in completed.stderr


def test_check_blueprint_bad_json_is_json_failure(project: Project) -> None:
    project.slug_dir().mkdir(parents=True)
    (project.slug_dir() / "blueprint.json").write_text("{", encoding="utf-8")
    completed = project.run("check-blueprint", "compact")
    assert completed.returncode == 1
    assert result_json(completed)["ok"] is False
    assert "Traceback" not in completed.stderr


def test_bad_usage_prints_json_and_exits_2(project: Project) -> None:
    completed = project.run("check-blueprint")
    assert completed.returncode == 2
    assert result_json(completed)["ok"] is False


def test_page_facts_include_cards_pushed_at_runtime(project: Project) -> None:
    blueprint = copy.deepcopy(BLUEPRINT_SEED)
    blueprint.update(slug="extra-card", command="/extra-card")
    blueprint["contrast"]["example"] = "/extra-card mantenha testes"
    project.write_blueprint(blueprint, slug="extra-card")
    completed = project.run("check-blueprint", "extra-card")
    assert completed.returncode == 0, completed.stdout


# ---------------------------------------------------------------- labels


def test_labels_prints_closed_list_in_contract_order(project: Project) -> None:
    project.write_blueprint()
    completed = project.run("labels", "compact")
    assert completed.returncode == 0, completed.stdout
    assert completed.stdout.splitlines() == seed_strings()


def test_labels_fails_as_json_without_blueprint(project: Project) -> None:
    completed = project.run("labels", "compact")
    assert completed.returncode == 1
    assert result_json(completed)["ok"] is False


# ---------------------------------------------------------------- render-template


def write_template(project: Project, text: str) -> Path:
    path = project.root.parent / "template.html"
    path.write_text(text, encoding="utf-8")
    return path


def test_render_template_fills_slot_with_escaped_json(project: Project) -> None:
    blueprint = copy.deepcopy(BLUEPRINT_SEED)
    blueprint["contrast"]["example"] = '/compact </script> \\u00e9 \\\\ "fim"'
    project.write_blueprint(blueprint)
    template = write_template(project, TEMPLATE_FIXTURE)
    completed = project.run("render-template", "compact", "--template", str(template))
    assert completed.returncode == 0, completed.stdout
    rendered = (project.slug_dir() / "infographic.html").read_text(encoding="utf-8")
    slot = SLOT_PATTERN.findall(rendered)
    assert len(slot) == 1
    assert "</" not in slot[0]
    assert json.loads(slot[0].replace("<\\/", "</")) == blueprint


def test_render_template_rejects_missing_slot(project: Project) -> None:
    project.write_blueprint()
    template = write_template(project, "<!doctype html><html><body></body></html>")
    completed = project.run("render-template", "compact", "--template", str(template))
    assert completed.returncode == 1
    assert not (project.slug_dir() / "infographic.html").exists()


def test_render_template_rejects_two_slots(project: Project) -> None:
    project.write_blueprint()
    doubled = TEMPLATE_FIXTURE.replace("</body>", '<script type="application/json" id="blueprint">{}</script></body>')
    template = write_template(project, doubled)
    completed = project.run("render-template", "compact", "--template", str(template))
    assert completed.returncode == 1
    assert not (project.slug_dir() / "infographic.html").exists()


# ---------------------------------------------------------------- check-vector


def check_vector_report(project: Project, text: str) -> tuple[subprocess.CompletedProcess[str], dict[str, Any]]:
    project.write_blueprint()
    project.write_vector(text)
    completed = project.run("check-vector", "compact")
    return completed, result_json(completed)


def strings_without(*removed: str) -> list[str]:
    return [text for text in seed_strings() if text not in removed]


def test_check_vector_passes_on_matching_vector(project: Project) -> None:
    completed, report = check_vector_report(project, vector_html(seed_strings()))
    assert completed.returncode == 0, completed.stdout
    assert report["ok"] is True
    assert report["errors"] == []
    assert report["network_requests"] == []


def test_check_vector_rejects_missing_doctype(project: Project) -> None:
    text = vector_html(seed_strings()).replace("<!doctype html>\n", "")
    completed, report = check_vector_report(project, text)
    assert completed.returncode == 1
    assert report["static_findings"]


def test_check_vector_rejects_external_image_without_rendering(project: Project) -> None:
    extra = '<img src="https://example.invalid/a.png" alt="">'
    completed, report = check_vector_report(project, vector_html(seed_strings(), extra))
    assert completed.returncode == 1
    assert report["static_findings"]
    assert report["network_requests"] == []


def test_check_vector_rejects_external_script_src(project: Project) -> None:
    extra = '<script src="https://example.invalid/a.js"></script>'
    completed, report = check_vector_report(project, vector_html(seed_strings(), extra))
    assert completed.returncode == 1
    assert report["static_findings"]


def test_check_vector_rejects_fetch_in_inline_script(project: Project) -> None:
    extra = '<script>fetch("/dados")</script>'
    completed, report = check_vector_report(project, vector_html(seed_strings(), extra))
    assert completed.returncode == 1
    assert report["static_findings"]


def test_check_vector_records_runtime_request(project: Project) -> None:
    """In-process: the CLI runs only the shipped template's scripts, so this page's script is allowlisted here."""
    extra = '<script>new Image().src = "ht" + "tps://example.invalid/x";</script>'
    text = vector_html(seed_strings(), extra)
    project.write_blueprint()
    document = project.write_vector(text)
    allowlist = rc.template_script_allowlist(text)
    with rc.open_browser() as browser:
        report = rc.check_vector_document(browser, document, rc.closed_list(BLUEPRINT_SEED), allowlist)
    assert report["ok"] is False
    assert report["static_findings"] == []
    assert "https://example.invalid/x" in report["network_requests"]


def test_check_vector_reports_missing_string_in_contract_shape(project: Project) -> None:
    text = vector_html(strings_without("Quando usar"))
    completed, report = check_vector_report(project, text)
    assert completed.returncode == 1
    missing = [error for error in report["errors"] if error["expected"] == "Quando usar"]
    assert len(missing) == 1
    assert set(missing[0]) == VECTOR_KEYS
    assert missing[0]["issue_type"] in {"typo", "truncated"}


def test_check_vector_reports_misspelling_as_unexpected(project: Project) -> None:
    text = vector_html(seed_strings(), "<p>Quando usr</p>")
    completed, report = check_vector_report(project, text)
    assert completed.returncode == 1
    unexpected = [error for error in report["errors"] if error["found"] == "Quando usr"]
    assert len(unexpected) == 1
    assert unexpected[0]["expected"] == "Quando usar"
    assert unexpected[0]["issue_type"] == "typo"


def test_check_vector_reports_invented_text(project: Project) -> None:
    completed, report = check_vector_report(project, vector_html(seed_strings(), "<p>Texto inventado</p>"))
    assert completed.returncode == 1
    assert any(error["found"] == "Texto inventado" for error in report["errors"])


def test_check_vector_ignores_hidden_and_aria_hidden_text(project: Project) -> None:
    extra = '<p style="display:none">Texto oculto</p><p aria-hidden="true">Dica extra</p>'
    completed, report = check_vector_report(project, vector_html(seed_strings(), extra))
    assert completed.returncode == 0, report
    assert report["errors"] == []


def test_check_vector_joins_svg_tspans_before_matching(project: Project) -> None:
    svg = '<svg width="200" height="40"><text><tspan>Quando</tspan><tspan> usar</tspan></text></svg>'
    completed, report = check_vector_report(project, vector_html(strings_without("Quando usar"), svg))
    assert completed.returncode == 0, report
    assert report["errors"] == []


def test_check_vector_reads_text_not_css_uppercase(project: Project) -> None:
    heading = '<h3 style="text-transform:uppercase">Exemplo</h3>'
    completed, report = check_vector_report(project, vector_html(strings_without("Exemplo"), heading))
    assert completed.returncode == 0, report


def test_check_vector_does_not_scan_json_slot_text(project: Project) -> None:
    slot = '<script type="application/json" id="blueprint">{"note": "fetch(x) https://example.invalid"}</script>'
    completed, report = check_vector_report(project, vector_html(seed_strings(), slot))
    assert completed.returncode == 0, report


@pytest.mark.parametrize(
    "markup",
    [
        '<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"></svg>',
        '<svg width="10" height="10"><a xmlns:xlink="http://www.w3.org/1999/xlink"></a></svg>',
        '<div xmlns="http://www.w3.org/1999/xhtml"></div>',
    ],
)
def test_check_vector_does_not_flag_namespace_declarations(project: Project, markup: str) -> None:
    completed, report = check_vector_report(project, vector_html(seed_strings(), markup))
    assert completed.returncode == 0, completed.stdout
    assert report["static_findings"] == []
    assert report["network_requests"] == []


@pytest.mark.parametrize(
    "markup",
    [
        '<a href="https://example.invalid/page">link</a>',
        '<img src="http://www.w3.org/2000/svg" alt="">',
        '<svg xmlns="https://example.invalid/ns" width="10" height="10"></svg>',
    ],
)
def test_check_vector_still_flags_other_http_urls(project: Project, markup: str) -> None:
    completed, report = check_vector_report(project, vector_html(seed_strings(), markup))
    assert completed.returncode == 1
    assert report["static_findings"]


# ---------------------------------------------------------------- check-vector: active content


def rendered_template(project: Project) -> str:
    """The shipped template rendered by the CLI, so the vector carries the template's own scripts."""
    project.write_blueprint()
    completed = project.run("render-template", "compact")
    assert completed.returncode == 0, completed.stdout
    return (project.slug_dir() / "infographic.html").read_text(encoding="utf-8")


def insert_before_body_end(text: str, markup: str) -> str:
    return text.replace("</body>", f"{markup}</body>", 1)


ACTIVE_CONTENT_CASES = [
    pytest.param(lambda text: text.replace("<body>", '<body onload="alert(1)">', 1), "onload", id="body-onload"),
    pytest.param(
        lambda text: insert_before_body_end(text, '<a href="javascript:alert(1)">x</a>'),
        "javascript:",
        id="javascript-href",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<a href="jav&#x09;ascript:alert(1)">x</a>'),
        "javascript:",
        id="entity-obfuscated-javascript",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<a href="vbscript:msgbox(1)">x</a>'),
        "vbscript:",
        id="vbscript-href",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<a href="data:text/html,%3Cscript%3Ealert(1)%3C/script%3E">x</a>'),
        "data:text/html",
        id="data-html-href",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<div style="background:url(javascript:alert(1))"></div>'),
        "javascript:",
        id="javascript-inside-style-value",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<svg width="10" height="10" onload="alert(1)"></svg>'),
        "onload",
        id="svg-onload",
    ),
    pytest.param(
        lambda text: insert_before_body_end(
            text, '<svg width="10" height="10"><rect width="10" height="10" onclick="alert(1)"/></svg>'
        ),
        "onclick",
        id="svg-rect-onclick",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<script>window["fe"+"tch"]("/x")</script>'),
        "inline script",
        id="obfuscated-fetch-script",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<script type="module">const answer = 42;</script>'),
        "inline script",
        id="module-script-with-harmless-text",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, "<script>alert(1)"),
        "inline script",
        id="unterminated-script-runs-to-end",
    ),
    pytest.param(
        lambda text: insert_before_body_end(text, '<script type="application/json" id="other">{}</script>'),
        "application/json",
        id="json-data-with-other-id",
    ),
]


@pytest.mark.parametrize(("transform", "expected"), ACTIVE_CONTENT_CASES)
def test_check_vector_rejects_active_content(project: Project, transform: Any, expected: str) -> None:
    completed, report = check_vector_report(project, transform(rendered_template(project)))
    assert completed.returncode == 1, completed.stdout
    assert report["ok"] is False
    assert any(expected in finding for finding in report["static_findings"]), report["static_findings"]


def test_check_vector_passes_on_untouched_template_output(project: Project) -> None:
    completed, report = check_vector_report(project, rendered_template(project))
    assert completed.returncode == 0, completed.stdout
    assert report["ok"] is True
    assert report["static_findings"] == []


def test_check_vector_rejects_one_changed_character_in_template_script(project: Project) -> None:
    text = rendered_template(project)
    match = re.search(r"<script>(.*?)</script>", text, re.DOTALL)
    assert match is not None
    body = match.group(1)
    middle = len(body) // 2
    replacement = "_" if body[middle] != "_" else "-"
    tampered = text[: match.start(1)] + body[:middle] + replacement + body[middle + 1 :] + text[match.end(1) :]
    completed, report = check_vector_report(project, tampered)
    assert completed.returncode == 1, completed.stdout
    assert any("not in the template allowlist" in finding for finding in report["static_findings"])


# ---------------------------------------------------------------- snapshot and collect-download


def test_snapshot_records_name_size_and_mtime(project: Project) -> None:
    (project.downloads / "a.png").write_bytes(b"12345")
    out = snapshot(project)
    recorded = json.loads(out.read_text(encoding="utf-8"))
    stat_info = (project.downloads / "a.png").stat()
    assert recorded == {"a.png": [stat_info.st_size, stat_info.st_mtime_ns]}


def test_collect_png_moves_new_file_into_place(project: Project) -> None:
    project.write_blueprint()
    snap = snapshot(project)
    write_png_stub(project.downloads / "image.png", b"new")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 0, completed.stdout
    target = project.slug_dir() / "infographic.png"
    assert target.read_bytes() == PNG_SIGNATURE + b"new"
    assert not (project.downloads / "image.png").exists()
    assert sorted(path.name for path in project.slug_dir().iterdir()) == ["blueprint.json", "infographic.png"]


def test_collect_moves_only_the_new_png_and_leaves_older_downloads(project: Project) -> None:
    project.write_blueprint()
    write_png_stub(project.downloads / "older.png", b"old")
    (project.downloads / "notes.txt").write_text("unrelated", encoding="utf-8")
    snap = snapshot(project)
    write_png_stub(project.downloads / "Infographic.png", b"studio")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 0, completed.stdout
    assert result_json(completed)["source"] == "Infographic.png"
    assert (project.slug_dir() / "infographic.png").read_bytes() == PNG_SIGNATURE + b"studio"
    assert sorted(path.name for path in project.downloads.iterdir()) == ["notes.txt", "older.png"]


def test_collect_refuses_several_new_pngs_and_moves_nothing(project: Project) -> None:
    project.write_blueprint()
    snap = snapshot(project)
    write_png_stub(project.downloads / "first.png", b"first")
    write_png_stub(project.downloads / "second.png", b"second")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 1
    assert result_json(completed)["found"] == ["first.png", "second.png"]
    assert not (project.slug_dir() / "infographic.png").exists()
    assert sorted(path.name for path in project.downloads.iterdir()) == ["first.png", "second.png"]


def test_collect_fails_on_zero_new_files(project: Project) -> None:
    snap = snapshot(project)
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 1
    report = result_json(completed)
    assert report["ok"] is False and report["found"] == []


def test_collect_fails_listing_several_new_files(project: Project) -> None:
    snap = snapshot(project)
    write_png_stub(project.downloads / "one.png")
    write_png_stub(project.downloads / "two.png")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 1
    assert result_json(completed)["found"] == ["one.png", "two.png"]


def test_collect_ignores_partial_downloads(project: Project) -> None:
    snap = snapshot(project)
    (project.downloads / "partial.png.crdownload").write_bytes(b"half")
    (project.downloads / "other.part").write_bytes(b"half")
    write_png_stub(project.downloads / "done.png")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 0, completed.stdout


def test_collect_counts_changed_file_as_new(project: Project) -> None:
    (project.downloads / "again.png").write_bytes(b"old")
    snap = snapshot(project)
    write_png_stub(project.downloads / "again.png", b"changed-size")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 0, completed.stdout


def test_collect_rejects_wrong_kind(project: Project) -> None:
    snap = snapshot(project)
    write_png_stub(project.downloads / "image.png")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "html")
    assert completed.returncode == 1
    assert not (project.slug_dir() / "infographic.html").exists()


def test_collect_html_requires_doctype(project: Project) -> None:
    snap = snapshot(project)
    (project.downloads / "page.html").write_text("<p>sem doctype</p>", encoding="utf-8")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "html")
    assert completed.returncode == 1


def test_collect_html_moves_doctype_file(project: Project) -> None:
    snap = snapshot(project)
    (project.downloads / "page.html").write_text(vector_html(seed_strings()), encoding="utf-8")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "html")
    assert completed.returncode == 0, completed.stdout
    assert (project.slug_dir() / "infographic.html").exists()


def test_collect_converts_jpeg_to_png(project: Project, make_jpeg_and_webp: tuple[bytes, bytes]) -> None:
    jpeg, _ = make_jpeg_and_webp
    snap = snapshot(project)
    (project.downloads / "photo.jpg").write_bytes(jpeg)
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 0, completed.stdout
    report = result_json(completed)
    assert report["detected"] == "jpeg" and report["converted"] is True
    assert (project.slug_dir() / "infographic.png").read_bytes().startswith(PNG_SIGNATURE)


def test_collect_converts_webp_to_png(project: Project, make_jpeg_and_webp: tuple[bytes, bytes]) -> None:
    _, webp = make_jpeg_and_webp
    snap = snapshot(project)
    (project.downloads / "photo.webp").write_bytes(webp)
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 0, completed.stdout
    assert result_json(completed)["detected"] == "webp"
    assert (project.slug_dir() / "infographic.png").read_bytes().startswith(PNG_SIGNATURE)


def test_collect_keeps_older_file_when_new_one_is_invalid(project: Project) -> None:
    write_png_stub(project.slug_dir() / "infographic.png", b"old")
    snap = snapshot(project)
    (project.downloads / "broken.png").write_bytes(b"not an image at all")
    completed = project.run("collect-download", "compact", "--snapshot", str(snap), "--kind", "png")
    assert completed.returncode == 1
    assert (project.slug_dir() / "infographic.png").read_bytes() == PNG_SIGNATURE + b"old"


# ---------------------------------------------------------------- render-fallback


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    assert data[:8] == PNG_SIGNATURE
    width, height = struct.unpack(">II", data[16:24])
    return width, height


@pytest.mark.parametrize(
    ("aspect", "expected_png"),
    [("16:9", (3200, 1800)), ("4:5", (2160, 2700))],
)
def test_render_fallback_renders_png_and_single_page_pdf(project: Project, aspect: str, expected_png: tuple[int, int]) -> None:
    blueprint = copy.deepcopy(BLUEPRINT_SEED)
    blueprint["aspect"] = aspect
    project.write_blueprint(blueprint)
    project.write_vector()
    completed = project.run("render-fallback", "compact")
    assert completed.returncode == 0, completed.stdout
    assert png_size(project.slug_dir() / "infographic.png") == expected_png
    pdf = (project.slug_dir() / "infographic.pdf").read_bytes()
    assert rc.count_pdf_pages(pdf) == 1


def png_first_pixel(path: Path) -> tuple[int, int, int]:
    """RGB of the top-left pixel: only the first scanline's first pixel is unfiltered."""
    data = path.read_bytes()
    assert data[:8] == PNG_SIGNATURE
    assert data[24] == 8
    channels = {2: 3, 6: 4}[data[25]]
    idat, offset = b"", 8
    while offset < len(data):
        length, kind = struct.unpack(">I4s", data[offset : offset + 8])
        if kind == b"IDAT":
            idat += data[offset + 8 : offset + 8 + length]
        offset += 12 + length
    raw = zlib.decompressobj().decompress(idat, 1 + channels)
    # First pixel of the first row: left, up and up-left are all zero, so filters 0-4 leave its bytes as stored.
    assert raw[0] in range(5)
    return raw[1], raw[2], raw[3]


def test_render_fallback_png_is_full_bleed_canvas(project: Project) -> None:
    rendered_template(project)
    completed = project.run("render-fallback", "compact")
    assert completed.returncode == 0, completed.stdout
    # The dark header band starts at the canvas edge; a scaled-down canvas leaves the light page background there.
    assert sum(png_first_pixel(project.slug_dir() / "infographic.png")) < 300


ZOOM_SELECTOR = '[data-testid^="infographic-zoom"]'
VISIBLE_ZOOM_JS = """(selector) => [...document.querySelectorAll(selector)].filter(
    (element) => getComputedStyle(element).display !== "none" && element.getClientRects().length > 0
).length"""


def test_render_fallback_exports_template_output(project: Project) -> None:
    rendered_template(project)
    completed = project.run("render-fallback", "compact")
    assert completed.returncode == 0, completed.stdout
    assert result_json(completed)["ok"] is True
    assert png_size(project.slug_dir() / "infographic.png") == (3200, 1800)
    assert rc.count_pdf_pages((project.slug_dir() / "infographic.pdf").read_bytes()) == 1


def test_export_hides_zoom_controls_on_template_output(project: Project) -> None:
    rendered_template(project)
    document = project.slug_dir() / "infographic.html"
    with rc.open_browser() as browser:
        context = browser.new_context(viewport={"width": 1600, "height": 900})
        try:
            page = context.new_page()
            page.goto(document.as_uri(), wait_until="load")
            assert page.locator(ZOOM_SELECTOR).count() == 3
            assert page.evaluate(VISIBLE_ZOOM_JS, ZOOM_SELECTOR) == 3
            rc.hide_export_controls(page)
            assert page.evaluate(VISIBLE_ZOOM_JS, ZOOM_SELECTOR) == 0
        finally:
            context.close()


def test_export_check_fails_while_zoom_controls_are_visible() -> None:
    with rc.open_browser() as browser:
        page = browser.new_page()
        page.set_content('<button data-testid="infographic-zoom-in" type="button">+</button>')
        with pytest.raises(rc.ToolError, match="zoom"):
            rc.assert_export_controls_hidden(page)
        rc.hide_export_controls(page)
        rc.assert_export_controls_hidden(page)


def test_count_pdf_pages_counts_page_objects_only() -> None:
    assert rc.count_pdf_pages(b"1 0 obj << /Type /Pages /Count 1 >> endobj 2 0 obj << /Type /Page >>") == 1
    assert rc.count_pdf_pages(b"<< /Type /Page >>\n<< /Type/Page >>\n<< /Type /Pages >>") == 2
    assert rc.count_pdf_pages(b"<< /Type /Pages >>") == 0


def test_ensure_single_pdf_page_rejects_two_pages() -> None:
    with pytest.raises(rc.ToolError):
        rc.ensure_single_pdf_page(b"<< /Type /Page >>\n<< /Type /Page >>")


# ---------------------------------------------------------------- check-qa


def qa_report(**overrides: Any) -> dict[str, Any]:
    report: dict[str, Any] = {"passed": True, "attempt": 1, "model_mode": "notebooklm", "errors": []}
    report.update(overrides)
    return report


def write_qa(project: Project, report: dict[str, Any]) -> None:
    project.slug_dir().mkdir(parents=True, exist_ok=True)
    (project.slug_dir() / "qa-report.json").write_text(json.dumps(report), encoding="utf-8")


def test_check_qa_accepts_approved_report(project: Project) -> None:
    write_qa(project, qa_report())
    completed = project.run("check-qa", "compact")
    assert completed.returncode == 0, completed.stdout


@pytest.mark.parametrize(
    "report",
    [
        qa_report(passed=False),
        qa_report(errors=[{"expected": "a", "found": "b", "location": "x", "issue_type": "typo"}]),
        qa_report(model_mode="gpt"),
        qa_report(model_mode="nano_banana_2"),
        qa_report(attempt=4),
        qa_report(errors=[{"expected": "a", "found": "b", "location": "x", "issue_type": "weird"}]),
    ],
)
def test_check_qa_rejects_unapproved_or_malformed_report(project: Project, report: dict[str, Any]) -> None:
    write_qa(project, report)
    completed = project.run("check-qa", "compact")
    assert completed.returncode == 1
    assert result_json(completed)["ok"] is False


def test_check_qa_missing_report_fails(project: Project) -> None:
    completed = project.run("check-qa", "compact")
    assert completed.returncode == 1


# ---------------------------------------------------------------- register


def read_manifest(project: Project) -> dict[str, Any]:
    return json.loads(project.manifest.read_text(encoding="utf-8"))


def test_register_vector_only_writes_manifest_page_and_standalone(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout

    manifest = read_manifest(project)
    item = manifest["items"]["compact"]
    assert item["formats"] == {
        "vector": "assets/infographics/compact/infographic.html",
        "image": None,
        "download": None,
        "pdf": None,
    }
    assert item["qa_status"] == "passed"
    assert item["model_mode"] == "vector"
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", item["updated_at"])
    assert project.manifest.read_text(encoding="utf-8").startswith('{\n  "items": {')

    block = page_block(project)
    assert set(block) == {"compact"}
    assert set(block["compact"]) == {"command", "formats", "model_mode", "updated_at"}
    source = project.page_source.read_text(encoding="utf-8")
    assert source.startswith(PAGE_FIXTURE[: PAGE_FIXTURE.index("/* INFOGRAPHICS:BEGIN")])
    assert project.standalone.read_bytes() == standalone_wrapper(source).encode("utf-8")


def test_register_image_mode_uses_qa_mode_and_webp(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_real_png(project.slug_dir() / "infographic.png")
    write_qa(project, qa_report())
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout
    item = read_manifest(project)["items"]["compact"]
    assert item["model_mode"] == "notebooklm"
    assert item["formats"]["image"] == WEBP_PATH


def test_register_converts_png_to_full_size_webp_and_keeps_png(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    png = project.slug_dir() / "infographic.png"
    write_real_png(png, (96, 54))
    png_before = png.read_bytes()
    write_qa(project, qa_report())
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout

    webp = project.slug_dir() / "infographic.webp"
    data = webp.read_bytes()
    assert data[:4] == b"RIFF" and data[8:12] == b"WEBP"
    with Image.open(webp) as image:
        assert image.format == "WEBP"
        assert image.size == (96, 54)
    expected = io.BytesIO()
    with Image.open(png) as source:
        source.save(expected, "WEBP", quality=90)
    assert data == expected.getvalue()
    assert png.read_bytes() == png_before
    assert read_manifest(project)["items"]["compact"]["formats"]["image"] == WEBP_PATH
    assert page_block(project)["compact"]["formats"]["image"] == WEBP_PATH
    assert PNG_PATH not in project.manifest.read_text(encoding="utf-8")
    assert PNG_PATH not in project.page_source.read_text(encoding="utf-8")


@pytest.mark.parametrize(
    ("source_size", "expected_size"),
    [((2752, 1536), (1920, 1072)), ((1000, 333), (1920, 639))],
)
def test_register_writes_1920_png_download_keeping_ratio_and_mode(
    project: Project, source_size: tuple[int, int], expected_size: tuple[int, int]
) -> None:
    project.write_blueprint()
    project.write_vector()
    write_real_png(project.slug_dir() / "infographic.png", source_size)
    write_qa(project, qa_report())
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout

    download = project.slug_dir() / "infographic-1920.png"
    assert download.read_bytes()[:8] == PNG_SIGNATURE
    with Image.open(download) as image:
        assert image.format == "PNG"
        assert image.size == expected_size
        assert image.mode == "RGBA"
    assert read_manifest(project)["items"]["compact"]["formats"]["download"] == DOWNLOAD_PATH
    assert page_block(project)["compact"]["formats"]["download"] == DOWNLOAD_PATH


def test_register_with_unreadable_png_fails_and_writes_nothing(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_png_stub(project.slug_dir() / "infographic.png")
    write_qa(project, qa_report())
    before = project.page_source.read_bytes()
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert result_json(completed)["ok"] is False
    assert not project.manifest.exists()
    assert not (project.slug_dir() / "infographic.webp").exists()
    assert not (project.slug_dir() / "infographic-1920.png").exists()
    assert project.page_source.read_bytes() == before


def test_register_twice_gives_same_files_and_bytes_except_updated_at(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_real_png(project.slug_dir() / "infographic.png")
    write_qa(project, qa_report())
    assert project.run("register", "compact").returncode == 0
    names_first = sorted(path.name for path in project.slug_dir().iterdir())
    webp_first = (project.slug_dir() / "infographic.webp").read_bytes()
    download_first = (project.slug_dir() / "infographic-1920.png").read_bytes()
    manifest_first = project.manifest.read_text(encoding="utf-8")
    page_first = project.page_source.read_text(encoding="utf-8")
    standalone_first = project.standalone.read_text(encoding="utf-8")

    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout
    assert sorted(path.name for path in project.slug_dir().iterdir()) == names_first
    assert (project.slug_dir() / "infographic.webp").read_bytes() == webp_first
    assert (project.slug_dir() / "infographic-1920.png").read_bytes() == download_first
    without_stamp = re.compile(r'"updated_at": "[^"]*"')
    for before, after in (
        (manifest_first, project.manifest),
        (page_first, project.page_source),
        (standalone_first, project.standalone),
    ):
        assert without_stamp.sub("", after.read_text(encoding="utf-8")) == without_stamp.sub("", before)


def test_reregister_switches_manifest_from_png_path_to_webp(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_real_png(project.slug_dir() / "infographic.png")
    write_qa(project, qa_report())
    seeded = {
        "version": 1,
        "items": {
            "compact": {
                "slug": "compact",
                "command": "/compact",
                "formats": {
                    "vector": "assets/infographics/compact/infographic.html",
                    "image": PNG_PATH,
                    "pdf": None,
                },
                "qa_status": "passed",
                "model_mode": "notebooklm",
                "updated_at": "2026-11-22T21:00:00Z",
            }
        },
    }
    project.manifest.parent.mkdir(parents=True, exist_ok=True)
    project.manifest.write_text(json.dumps(seeded), encoding="utf-8")
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout
    assert read_manifest(project)["items"]["compact"]["formats"]["image"] == WEBP_PATH
    assert page_block(project)["compact"]["formats"]["image"] == WEBP_PATH


def test_register_notebooklm_without_png_fails(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_qa(project, qa_report())
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert not project.manifest.exists()


def test_register_image_mode_with_failed_qa_leaves_everything_untouched(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_png_stub(project.slug_dir() / "infographic.png")
    write_qa(project, qa_report(passed=False))
    project.standalone.write_text("antigo", encoding="utf-8")
    before = project.page_source.read_bytes()
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert not project.manifest.exists()
    assert project.page_source.read_bytes() == before
    assert project.standalone.read_text(encoding="utf-8") == "antigo"


def test_register_vector_fallback_skips_check_qa_and_registers_checked_vector(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_real_png(project.slug_dir() / "infographic.png")
    write_qa(
        project,
        qa_report(
            passed=False,
            model_mode="vector_fallback",
            errors=[{"expected": "Quando usar", "found": "Quando usr", "location": "zona 4", "issue_type": "typo"}],
        ),
    )
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout
    item = read_manifest(project)["items"]["compact"]
    assert item["model_mode"] == "vector_fallback"
    assert item["qa_status"] == "passed"
    assert item["formats"]["image"] == WEBP_PATH
    assert item["formats"]["download"] == DOWNLOAD_PATH
    assert (project.slug_dir() / "infographic.webp").is_file()


def test_register_vector_fallback_without_png_has_no_image_or_download(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    write_qa(project, qa_report(model_mode="vector_fallback"))
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout
    formats = read_manifest(project)["items"]["compact"]["formats"]
    assert formats["image"] is None
    assert formats["download"] is None


def test_missing_pillow_is_a_tool_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "PIL", None)
    with pytest.raises(rc.ToolError):
        rc.encode_download_png(tmp_path / "infographic.png")


def test_page_download_button_saves_png() -> None:
    source = PAGE_UNDER_TEST.read_text(encoding="utf-8")
    assert 'const INFOGRAPHIC_FILES = [["download", "Baixar PNG", "png"], ["pdf", "Baixar PDF", "pdf"]];' in source
    assert "Baixar WebP" not in source


def test_register_vector_fallback_still_needs_passing_vector(project: Project) -> None:
    project.write_blueprint()
    project.write_vector(vector_html(seed_strings(), "<p>Texto inventado</p>"))
    write_png_stub(project.slug_dir() / "infographic.png")
    write_qa(project, qa_report(model_mode="vector_fallback"))
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert not project.manifest.exists()


def test_register_vector_fallback_without_html_fails(project: Project) -> None:
    project.write_blueprint()
    write_png_stub(project.slug_dir() / "infographic.png")
    write_qa(project, qa_report(model_mode="vector_fallback"))
    completed = project.run("register", "compact")
    assert completed.returncode == 1


def test_register_fails_when_vector_check_fails(project: Project) -> None:
    project.write_blueprint()
    project.write_vector(vector_html(strings_without("Exemplo")))
    before = project.page_source.read_bytes()
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert not project.manifest.exists()
    assert project.page_source.read_bytes() == before


def test_register_rejects_duplicate_markers(project: Project) -> None:
    second_block = "/* INFOGRAPHICS:BEGIN (copy) */\n/* INFOGRAPHICS:END */\n"
    doubled = PAGE_FIXTURE.replace("/* INFOGRAPHICS:END */\n", "/* INFOGRAPHICS:END */\n" + second_block, 1)
    project.page_source.write_text(doubled, encoding="utf-8")
    project.write_blueprint()
    project.write_vector()
    before = project.page_source.read_bytes()
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert project.page_source.read_bytes() == before
    assert not project.manifest.exists()


def test_register_rejects_missing_markers(project: Project) -> None:
    project.page_source.write_text(PAGE_FIXTURE.replace("/* INFOGRAPHICS:END */\n", ""), encoding="utf-8")
    project.write_blueprint()
    project.write_vector()
    before = project.page_source.read_bytes()
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert project.page_source.read_bytes() == before


def test_register_requires_blueprint(project: Project) -> None:
    completed = project.run("register", "compact")
    assert completed.returncode == 1
    assert not project.manifest.exists()


def test_register_requires_some_format(project: Project) -> None:
    project.write_blueprint()
    completed = project.run("register", "compact")
    assert completed.returncode == 1


def test_register_block_lists_only_passed_items_and_keeps_others(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    project.manifest.parent.mkdir(parents=True, exist_ok=True)
    seeded = {
        "version": 1,
        "items": {
            "context": {
                "slug": "context",
                "command": "/context",
                "formats": {"vector": None, "image": None, "pdf": None},
                "qa_status": "failed",
                "model_mode": "notebooklm",
                "updated_at": "2026-11-20T10:00:00Z",
            },
            "clear": {
                "slug": "clear",
                "command": "/clear",
                "formats": {"vector": None, "image": None, "pdf": None},
                "qa_status": "passed",
                "model_mode": "vector",
                "updated_at": "2026-11-21T10:00:00Z",
            },
        },
    }
    project.manifest.write_text(json.dumps(seeded), encoding="utf-8")
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout
    items = read_manifest(project)["items"]
    assert set(items) == {"clear", "compact", "context"}
    assert set(page_block(project)) == {"clear", "compact"}


def test_register_keeps_page_source_mode(project: Project) -> None:
    project.write_blueprint()
    project.write_vector()
    project.page_source.chmod(0o640)
    completed = project.run("register", "compact")
    assert completed.returncode == 0, completed.stdout
    assert stat.S_IMODE(project.page_source.stat().st_mode) == 0o640


# ---------------------------------------------------------------- atomic writes and root discovery


def test_atomic_write_failure_keeps_target_and_removes_temp(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    folder = tmp_path / "atomic"
    folder.mkdir()
    target = folder / "manifest.json"
    target.write_bytes(b"old")

    def refuse(source: str, destination: str) -> None:
        raise OSError("rename refused")

    monkeypatch.setattr(rc.os, "replace", refuse)
    with pytest.raises(OSError):
        rc.write_atomic(target, b"new")
    assert target.read_bytes() == b"old"
    assert [path.name for path in folder.iterdir()] == ["manifest.json"]


def test_atomic_write_keeps_target_mode(tmp_path: Path) -> None:
    target = tmp_path / "page.html"
    target.write_bytes(b"old")
    target.chmod(0o640)
    rc.write_atomic(target, b"new")
    assert target.read_bytes() == b"new"
    assert stat.S_IMODE(target.stat().st_mode) == 0o640


def test_root_is_found_from_a_subdirectory(project: Project) -> None:
    project.write_blueprint()
    completed = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "check-blueprint", "compact"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=str(project.slug_dir()),
        timeout=240,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout


def test_root_not_found_is_usage_error(tmp_path: Path) -> None:
    completed = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "check-blueprint", "compact"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=str(tmp_path),
        timeout=240,
        check=False,
    )
    assert completed.returncode == 2
    assert result_json(completed)["ok"] is False
