"""Layout gate for the vector template: every blueprint fixture, rendered through the module's own slot path."""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest
from blueprint_fixtures import FIXTURE_NAMES, load_fixture
from conftest import load_register_tool
from playwright.sync_api import Browser, BrowserContext, Page

rc = load_register_tool()

TEMPLATE = Path(os.environ.get("INFOGRAPHIC_TEMPLATE_UNDER_TEST", rc.DEFAULT_TEMPLATE))
TOLERANCE_PX = 1
BALANCED_FIXTURES = {"five-words-16x9", "minimal-16x9", "seed-16x9"}
MAX_BAND_PX = 120
MIN_STEP_HEIGHT_PX = 170
STEP_FONT_PX = {"regular": 24, "tight": 20}
BOX_SELECTOR = ".step, .verb, .link, .box, .notes__example, .zone__heading, .band__title, .band__purpose, .band__category"
LAYOUT_JS = """([boxSelector, tolerance]) => {
  const canvas = document.querySelector(".canvas");
  const frame = canvas.getBoundingClientRect();
  const boxes = [...canvas.querySelectorAll(boxSelector)];
  const name = (node) => `${node.className.split(" ")[0]}: ${node.textContent.trim().slice(0, 40)}`;
  const rects = boxes.map((node) => node.getBoundingClientRect());
  const overflow = boxes.filter((node) =>
    node.scrollWidth > node.clientWidth + tolerance || node.scrollHeight > node.clientHeight + tolerance).map(name);
  const outside = boxes.filter((_node, index) => {
    const rect = rects[index];
    return rect.left < frame.left - tolerance || rect.top < frame.top - tolerance
      || rect.right > frame.right + tolerance || rect.bottom > frame.bottom + tolerance;
  }).map(name);
  const intersections = [];
  for (let first = 0; first < boxes.length; first += 1) {
    for (let second = first + 1; second < boxes.length; second += 1) {
      const a = rects[first];
      const b = rects[second];
      const wide = Math.min(a.right, b.right) - Math.max(a.left, b.left);
      const high = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      if (wide > tolerance && high > tolerance) intersections.push(`${name(boxes[first])} / ${name(boxes[second])}`);
    }
  }
  const zones = [".band", ".zone--flow", ".zone--links", ".zone--notes"].map((selector) => canvas.querySelector(selector).getBoundingClientRect());
  const [band, flow, links, notes] = zones;
  const bands = [flow.top - band.bottom, links.top - flow.bottom, notes.top - links.bottom, frame.bottom - notes.bottom];
  const step = canvas.querySelector(".step");
  const stepBox = step.getBoundingClientRect();
  return {
    overflow, intersections, outside,
    canvasOverflow: canvas.scrollHeight > canvas.clientHeight + tolerance || canvas.scrollWidth > canvas.clientWidth + tolerance,
    bands,
    tight: canvas.classList.contains("canvas--tight"),
    stepFont: parseFloat(getComputedStyle(step).fontSize),
    stepBox: [Math.round(stepBox.width), Math.round(stepBox.height)],
  };
}"""
ZOOM_DISPLAY_JS = """(selector) => [...document.querySelectorAll(selector)].map((node) => getComputedStyle(node).display)"""


def write_fixture_page(name: str, folder: Path) -> tuple[Path, dict[str, Any]]:
    """Fill the slot with rc.render_slot, the same call render-template uses, and write the page."""
    blueprint = load_fixture(name)
    document = folder / f"{name}.html"
    document.write_text(rc.render_slot(TEMPLATE.read_text(encoding="utf-8"), blueprint), encoding="utf-8")
    return document, blueprint


def open_page(browser: Browser, document: Path, size: tuple[int, int], problems: list[str]) -> tuple[BrowserContext, Page, list[str]]:
    """A page with the module's request guard and console listeners armed before it loads."""
    context = browser.new_context(viewport={"width": size[0], "height": size[1]})
    page = context.new_page()
    blocked = rc.guard_requests(page)
    page.on("console", lambda message: problems.append(message.text) if message.type == "error" else None)
    page.on("pageerror", lambda error: problems.append(str(error)))
    page.goto(document.as_uri(), wait_until="load", timeout=rc.PAGE_TIMEOUT_MS)
    return context, page, blocked


def collect(browser: Browser, name: str, folder: Path) -> dict[str, Any]:
    """Render one fixture and gather every measurement the tests assert on."""
    document, blueprint = write_fixture_page(name, folder)
    size = rc.VIEWPORT_BY_ASPECT[blueprint["aspect"]]
    problems: list[str] = []
    context, page, blocked = open_page(browser, document, size, problems)
    try:
        parity = rc.text_parity_errors(page.evaluate(rc.TEXT_NODES_JS), rc.closed_list(blueprint))
        screen_zoom = page.evaluate(ZOOM_DISPLAY_JS, rc.ZOOM_CONTROL_SELECTOR)
        page.evaluate("document.documentElement.setAttribute('data-export', '')")
        export_zoom = page.evaluate(ZOOM_DISPLAY_JS, rc.ZOOM_CONTROL_SELECTOR)
        page.evaluate("document.documentElement.removeAttribute('data-export')")
        page.emulate_media(media="print")
        print_zoom = page.evaluate(ZOOM_DISPLAY_JS, rc.ZOOM_CONTROL_SELECTOR)
        layout = page.evaluate(LAYOUT_JS, [BOX_SELECTOR, TOLERANCE_PX])
        pdf = page.pdf(width=f"{size[0]}px", height=f"{size[1]}px", print_background=True)
    finally:
        context.close()
    return {
        "name": name,
        "aspect": blueprint["aspect"],
        "blocked": blocked,
        "problems": problems,
        "parity": parity,
        "screen_zoom": screen_zoom,
        "export_zoom": export_zoom,
        "print_zoom": print_zoom,
        "pdf_pages": rc.count_pdf_pages(pdf),
        **layout,
    }


@pytest.fixture(scope="module")
def browser() -> Iterator[Browser]:
    with rc.open_browser() as opened:
        yield opened


@pytest.fixture(scope="module", params=FIXTURE_NAMES)
def measured(request: pytest.FixtureRequest, browser: Browser, tmp_path_factory: pytest.TempPathFactory) -> dict[str, Any]:
    return collect(browser, request.param, tmp_path_factory.mktemp("layout"))


def test_no_request_leaves_the_machine(measured: dict[str, Any]) -> None:
    assert measured["blocked"] == []


def test_console_stays_clean(measured: dict[str, Any]) -> None:
    assert measured["problems"] == []


def test_text_matches_the_closed_list(measured: dict[str, Any]) -> None:
    assert measured["parity"] == []


def test_no_text_overflows_its_box(measured: dict[str, Any]) -> None:
    assert measured["overflow"] == []


def test_no_boxes_intersect(measured: dict[str, Any]) -> None:
    assert measured["intersections"] == []


def test_nothing_sits_outside_the_canvas(measured: dict[str, Any]) -> None:
    assert measured["outside"] == []


def test_canvas_does_not_overflow(measured: dict[str, Any]) -> None:
    assert measured["canvasOverflow"] is False


def test_pdf_has_one_page(measured: dict[str, Any]) -> None:
    assert measured["pdf_pages"] == 1


def test_zoom_controls_are_hidden_in_print_and_export(measured: dict[str, Any]) -> None:
    assert "none" not in measured["screen_zoom"]
    assert measured["export_zoom"] == ["none"] * 3
    assert measured["print_zoom"] == ["none"] * 3


def test_step_text_is_24_px_and_drops_to_20_only_when_tight(measured: dict[str, Any]) -> None:
    if measured["aspect"] == "4:5":
        assert measured["stepFont"] == STEP_FONT_PX["tight"]
    else:
        assert measured["stepFont"] == STEP_FONT_PX["tight" if measured["tight"] else "regular"]


def test_calm_fixtures_never_go_tight(measured: dict[str, Any]) -> None:
    if measured["name"] in BALANCED_FIXTURES | {"seed-4x5", "stress-4x5", "stress-16x9"}:
        assert measured["tight"] is False


def test_balanced_fixtures_fill_boxes_and_leave_no_wide_band(measured: dict[str, Any]) -> None:
    if measured["name"] not in BALANCED_FIXTURES:
        pytest.skip("balance is asserted for the seed, minimal and five-words cases")
    assert measured["stepBox"][1] >= MIN_STEP_HEIGHT_PX
    assert max(measured["bands"]) <= MAX_BAND_PX, measured["bands"]
