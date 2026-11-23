"""Infographic pipeline for the comandos page (contract: work/infographic-contracts.md, sections 1-9).

Every subcommand prints one JSON object on stdout, except `labels` (plain text lines on success).
Exit codes: 0 success, 1 failed check or unusable input, 2 bad usage.
"""

from __future__ import annotations

import argparse
import base64
import difflib
import hashlib
import html
import io
import json
import logging
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unicodedata
from collections.abc import Callable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from types import ModuleType
from typing import Any, Final, NoReturn
from urllib.parse import urlsplit

from playwright.sync_api import Browser, Page, Route, sync_playwright
from playwright.sync_api import Error as PlaywrightError

LOGGER = logging.getLogger("infographic_register_tool")

EXIT_OK: Final = 0
EXIT_FAILED: Final = 1
EXIT_USAGE: Final = 2

PAGE_SOURCE: Final = Path("src/comandos-nativos.html")
STANDALONE_PAGE: Final = Path("comandos-nativos.html")
INFOGRAPHICS_DIR: Final = Path("assets/infographics")
MANIFEST: Final = INFOGRAPHICS_DIR / "manifest.json"
DEFAULT_TEMPLATE: Final = Path(__file__).resolve().parent.parent / "references" / "infographic-vector.html"
BLUEPRINT_NAME: Final = "blueprint.json"
VECTOR_NAME: Final = "infographic.html"
IMAGE_NAME: Final = "infographic.png"
WEBP_NAME: Final = "infographic.webp"
WEBP_QUALITY: Final = 90
DOWNLOAD_NAME: Final = "infographic-1920.png"
DOWNLOAD_WIDTH: Final = 1920
PDF_NAME: Final = "infographic.pdf"
QA_NAME: Final = "qa-report.json"
DOWNLOADS_ENV: Final = "INFOGRAPHIC_DOWNLOADS_DIR"
CHROME_PATH: Final = "/usr/bin/google-chrome"
PAGE_TIMEOUT_MS: Final = 15_000
XDG_TIMEOUT_S: Final = 10
RENDER_SCALE: Final = 2
CHECK_VIEWPORT: Final = (1600, 900)
VIEWPORT_BY_ASPECT: Final = {"16:9": (1600, 900), "4:5": (1080, 1350)}
ASPECTS: Final = ("16:9", "4:5")
SLUG_PATTERN: Final = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
LOCAL_SCHEMES: Final = frozenset({"file", "data", "about", "blob"})
PARTIAL_SUFFIXES: Final = frozenset({".crdownload", ".part", ".tmp"})
PNG_SIGNATURE: Final = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE: Final = b"\xff\xd8\xff"
HEAD_BYTES: Final = 1024
MIME_BY_KIND: Final = {"jpeg": "image/jpeg", "webp": "image/webp"}
ACCEPTED_KINDS: Final = {"png": ("png", "jpeg", "webp"), "html": ("html",)}
DEFAULT_FILE_MODE: Final = 0o644
MIN_PREFIX_CHARS: Final = 4
UI_LABELS: Final = {
    "zone1": "Identidade e gatilho",
    "zone2": "Fluxo de execução",
    "zone3": "Conexões e variações",
    "when": "Quando usar",
    "pitfalls": "Armadilhas comuns",
    "example": "Exemplo",
}
LAYERS: Final = ("input", "processing", "result")
STEP_COUNT: Final = (3, 5)
LABEL_WORDS: Final = (3, 7)
PURPOSE_WORDS: Final = (1, 12)
CONTRAST_ITEMS: Final = (1, 3)
RELATED_ITEMS: Final = (1, 3)
OPTIONAL_ITEMS: Final = (0, 3)
WIDE_STEP_WORDS: Final = 5
VERB_WORDS: Final = (1, 2)
FORBIDDEN_TAGS: Final = frozenset({"link", "iframe", "object", "embed", "form", "base"})
RAW_TEXT_TAGS: Final = frozenset({"script", "style"})
JSON_SCRIPT_TYPE: Final = "application/json"
BLUEPRINT_SCRIPT_ID: Final = "blueprint"
EVENT_ATTRIBUTE_PREFIX: Final = "on"
URL_ATTRIBUTE_NAMES: Final = frozenset({"href", "src", "action", "formaction"})
ACTIVE_SCHEMES: Final = ("javascript:", "vbscript:")
DATA_HTML_SCHEME: Final = "data:text/html"
ZOOM_CONTROL_SELECTOR: Final = '[data-testid^="infographic-zoom"]'
HIDE_ZOOM_CONTROLS_CSS: Final = f"{ZOOM_CONTROL_SELECTOR} {{ display: none !important; }}"
VISIBLE_ZOOM_COUNT_JS: Final = """(selector) => [...document.querySelectorAll(selector)].filter(
    (element) => getComputedStyle(element).display !== "none" && element.getClientRects().length > 0
).length"""
NETWORK_REFERENCE: Final = re.compile(r"""(?i)https?:|(?:^|[\s(,='"])//[^\s/]""")
NAMESPACE_URIS: Final = frozenset(
    {"http://www.w3.org/2000/svg", "http://www.w3.org/1999/xlink", "http://www.w3.org/1999/xhtml"}
)
SCRIPT_TOKEN_PATTERNS: Final = tuple(
    re.compile(pattern)
    for pattern in (
        r"\bfetch\b",
        r"\bXMLHttpRequest\b",
        r"\bWebSocket\b",
        r"\bEventSource\b",
        r"\bsendBeacon\b",
        r"\bimport\s*\(",
        r"\bimportScripts\b",
        r"\bwindow\.open\b",
        r"\blocation\s*[.=]",
        r"\bdocument\.cookie\b",
        r"\blocalStorage\b",
        r"\bsessionStorage\b",
        r"\bindexedDB\b",
    )
)
SLOT_PATTERN: Final = re.compile(r'<script type="application/json" id="blueprint">(.*?)</script>', re.DOTALL)
PDF_PAGE_OBJECT: Final = re.compile(rb"/Type\s*/Page\b")
BLOCK_BEGIN: Final = "/* INFOGRAPHICS:BEGIN"
BLOCK_END: Final = "/* INFOGRAPHICS:END"
BLOCK_FIELDS: Final = ("command", "formats", "model_mode", "updated_at")
QA_MODEL_MODES: Final = ("notebooklm", "vector_fallback")
QA_ISSUE_TYPES: Final = ("typo", "missing_accent", "garbled", "truncated", "wrong_language")
QA_ERROR_KEYS: Final = ("expected", "found", "location", "issue_type")
STANDALONE_HEAD: Final = (
    '<!doctype html>\n<html lang="pt-BR" data-theme="dark">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n"
)
STANDALONE_TAIL: Final = "\n</html>\n"
READ_GLOBALS_JS: Final = """() => ({
  cards: COMMANDS.map((card) => card.id),
  categories: CATEGORIES.map((category) => ({ name: category.name, ids: category.ids })),
})"""
TEXT_NODES_JS: Final = """() => {
  const skipped = new Set(["SCRIPT", "STYLE", "TEMPLATE", "NOSCRIPT"]);
  const isHidden = (element) => {
    for (let node = element; node && node !== document.documentElement; node = node.parentElement) {
      if (skipped.has(node.tagName.toUpperCase()) || node.getAttribute("aria-hidden") === "true") return true;
      const style = getComputedStyle(node);
      if (style.display === "none" || style.visibility === "hidden") return true;
    }
    return false;
  };
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const texts = [];
  for (let node = walker.nextNode(); node; node = walker.nextNode()) {
    if (node.nodeValue.trim() && !isHidden(node.parentElement)) texts.push(node.nodeValue);
  }
  return texts;
}"""


class ToolError(Exception):
    """A failed check or unusable input: reported as JSON, exit 1."""


class UsageError(Exception):
    """Bad usage or an unknown project root: reported as JSON, exit 2."""


@dataclass(frozen=True)
class PageFacts:
    card_ids: frozenset[str]
    category_by_id: dict[str, str]


@dataclass(frozen=True)
class ClosedString:
    location: str
    text: str


class JsonArgumentParser(argparse.ArgumentParser):
    """argparse that reports bad usage as one JSON object on stdout, exit 2."""

    def error(self, message: str) -> NoReturn:
        emit({"ok": False, "error": message})
        raise SystemExit(EXIT_USAGE)


def emit(result: Mapping[str, Any]) -> None:
    sys.stdout.write(json.dumps(result, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- arguments and dispatch


def valid_slug(value: str) -> str:
    if not SLUG_PATTERN.fullmatch(value):
        raise argparse.ArgumentTypeError("slug must be a card id: letters, digits, '-' or '_'")
    return value


def _add_slug(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("slug", type=valid_slug, help="card id, for example compact")


def _add_slug_and_template(parser: argparse.ArgumentParser) -> None:
    _add_slug(parser)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)


def _add_slug_and_file(parser: argparse.ArgumentParser) -> None:
    _add_slug(parser)
    parser.add_argument("--file", type=Path, default=None)


def _add_out_and_downloads(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--downloads", type=Path, default=None)


def _add_collect_arguments(parser: argparse.ArgumentParser) -> None:
    _add_slug(parser)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--kind", choices=("png", "html"), required=True)
    parser.add_argument("--downloads", type=Path, default=None)


SUBCOMMAND_ARGUMENTS: Final[dict[str, Callable[[argparse.ArgumentParser], None]]] = {
    "check-blueprint": _add_slug,
    "labels": _add_slug,
    "render-template": _add_slug_and_template,
    "check-vector": _add_slug_and_file,
    "snapshot-downloads": _add_out_and_downloads,
    "collect-download": _add_collect_arguments,
    "render-fallback": _add_slug,
    "check-qa": _add_slug,
    "register": _add_slug,
}


def build_parser() -> argparse.ArgumentParser:
    parser = JsonArgumentParser(description="Infographic pipeline for the comandos page.")
    parser.add_argument("--root", type=Path, default=None, help="project root (default: search upward from cwd)")
    subcommands = parser.add_subparsers(dest="subcommand", required=True, parser_class=JsonArgumentParser)
    for name, configure in SUBCOMMAND_ARGUMENTS.items():
        configure(subcommands.add_parser(name))
    return parser


def resolve_root(option: Path | None) -> Path:
    start = (option or Path.cwd()).resolve()
    for folder in (start, *start.parents):
        if (folder / PAGE_SOURCE).is_file():
            return folder
    raise UsageError(f"no {PAGE_SOURCE} found from {start} upward; pass --root")


def main(argv: Sequence[str] | None = None) -> int:
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr, format="%(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    try:
        result = HANDLERS[args.subcommand](resolve_root(args.root), args)
    except UsageError as error:
        emit({"ok": False, "error": str(error)})
        return EXIT_USAGE
    except ToolError as error:
        emit({"ok": False, "error": str(error)})
        return EXIT_FAILED
    except PlaywrightError:
        LOGGER.exception("browser step failed")
        emit({"ok": False, "error": "browser step failed; see stderr"})
        return EXIT_FAILED
    except OSError:
        LOGGER.exception("file step failed")
        emit({"ok": False, "error": "file step failed; see stderr"})
        return EXIT_FAILED
    if args.subcommand == "labels" and result["ok"]:
        sys.stdout.write("\n".join(result["lines"]) + "\n")
    else:
        emit(result)
    return EXIT_OK if result["ok"] else EXIT_FAILED


# ---------------------------------------------------------------- paths, files, atomic writes


def relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def slug_folder(root: Path, slug: str) -> Path:
    base = (root / INFOGRAPHICS_DIR).resolve()
    folder = (base / slug).resolve()
    if folder.parent != base:
        raise UsageError("slug must name one folder under the infographics directory")
    return folder


def read_required_bytes(path: Path) -> bytes:
    if not path.is_file():
        raise ToolError(f"{path.name} not found")
    return path.read_bytes()


def read_required_text(path: Path) -> str:
    try:
        return read_required_bytes(path).decode("utf-8")
    except UnicodeDecodeError as error:
        raise ToolError(f"{path.name} is not UTF-8") from error


def load_json_object(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(read_required_text(path))
    except ValueError as error:
        raise ToolError(f"{path.name} is not valid JSON") from error
    if not isinstance(data, dict):
        raise ToolError(f"{path.name} must hold a JSON object")
    return data


def make_temp_sibling(target: Path) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(dir=target.parent, prefix=f".{target.name}.", suffix=".tmp")
    os.close(descriptor)
    return Path(name)


def fsync_path(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def publish_temp(temp: Path, target: Path) -> None:
    """Flush the finished temp file, keep the target's mode, rename it over the target, flush the folder."""
    mode = stat.S_IMODE(target.stat().st_mode) if target.exists() else DEFAULT_FILE_MODE
    fsync_path(temp)
    os.chmod(temp, mode)
    os.replace(temp, target)
    fsync_path(target.parent)


def write_atomic(target: Path, payload: bytes) -> None:
    temp = make_temp_sibling(target)
    try:
        temp.write_bytes(payload)
        publish_temp(temp, target)
    finally:
        temp.unlink(missing_ok=True)


def move_into_place(source: Path, target: Path) -> None:
    """Copy into the target's folder first so the rename stays on one filesystem, then drop the source."""
    temp = make_temp_sibling(target)
    try:
        shutil.copyfile(source, temp)
        publish_temp(temp, target)
    finally:
        temp.unlink(missing_ok=True)
    source.unlink()


def pillow_image_module() -> ModuleType:
    """Import Pillow only when register runs, so the other subcommands never need it."""
    try:
        from PIL import Image
    except ImportError as error:
        raise ToolError("Pillow is required for register: pip install pillow") from error
    return Image


def encode_webp(png: Path) -> bytes:
    """Re-encode the audited PNG as WebP at its full size (the view format)."""
    image_module = pillow_image_module()
    buffer = io.BytesIO()
    with image_module.open(png) as image:
        image.save(buffer, "WEBP", quality=WEBP_QUALITY)
    return buffer.getvalue()


def encode_download_png(png: Path) -> bytes:
    """Resize the audited PNG to DOWNLOAD_WIDTH, keeping the aspect ratio and the mode (the download format)."""
    image_module = pillow_image_module()
    buffer = io.BytesIO()
    with image_module.open(png) as image:
        height = round(image.height * DOWNLOAD_WIDTH / image.width)
        image.resize((DOWNLOAD_WIDTH, height), image_module.LANCZOS).save(buffer, "PNG", optimize=True)
    return buffer.getvalue()


def derived_images(folder: Path) -> dict[str, bytes]:
    """The WebP view and the 1920 px download, both from the audited PNG; encoded before anything is written."""
    source = folder / IMAGE_NAME
    return {WEBP_NAME: encode_webp(source), DOWNLOAD_NAME: encode_download_png(source)}


# ---------------------------------------------------------------- blueprint (contract section 3)


def load_blueprint(folder: Path) -> dict[str, Any]:
    return load_json_object(folder / BLUEPRINT_NAME)


def _check_text(path: str, value: object, errors: list[str]) -> None:
    if not isinstance(value, str):
        errors.append(f"{path} must be text")


def _check_words(path: str, value: object, bounds: tuple[int, int], errors: list[str]) -> None:
    low, high = bounds
    if not isinstance(value, str):
        errors.append(f"{path} must be text")
    elif not low <= len(value.split()) <= high:
        errors.append(f"{path} must have {low} to {high} words")


def _header_errors(blueprint: Mapping[str, Any], slug: str) -> list[str]:
    errors: list[str] = []
    version = blueprint.get("version")
    if type(version) is not int or version != 1:
        errors.append("version must be 1")
    if blueprint.get("slug") != slug:
        errors.append(f"slug must be {slug}")
    if blueprint.get("command") != f"/{slug}":
        errors.append(f"command must be /{slug}")
    _check_text("category", blueprint.get("category"), errors)
    if blueprint.get("aspect") not in ASPECTS:
        errors.append("aspect must be 16:9 or 4:5")
    return errors


def _ui_errors(ui: object) -> list[str]:
    if not isinstance(ui, dict):
        return ["ui must be an object"]
    if set(ui) != set(UI_LABELS):
        return ["ui must have exactly the six contract keys"]
    return [f"ui.{key} must be {UI_LABELS[key]!r}" for key in UI_LABELS if ui[key] != UI_LABELS[key]]


def _step_errors(steps: list[Any]) -> list[str]:
    errors: list[str] = []
    for index, step in enumerate(steps):
        path = f"flow.steps[{index}]"
        if not isinstance(step, dict):
            errors.append(f"{path} must be an object")
            continue
        if step.get("layer") not in LAYERS:
            errors.append(f"{path}.layer must be input, processing or result")
        _check_words(f"{path}.label", step.get("label"), LABEL_WORDS, errors)
    ids = [step.get("id") if isinstance(step, dict) else None for step in steps]
    if not all(isinstance(step_id, str) for step_id in ids) or len(set(ids)) != len(ids):
        errors.append("flow.steps ids must be unique text")
    layers = [step.get("layer") if isinstance(step, dict) else None for step in steps]
    if layers[0] != "input" or layers[-1] != "result":
        errors.append("the first step must be input and the last step result")
    return errors


def _single_edge_errors(index: int, edge: object, source_id: object, target_id: object) -> list[str]:
    path = f"flow.edges[{index}]"
    if not isinstance(edge, dict):
        return [f"{path} must be an object"]
    errors: list[str] = []
    if edge.get("from") != source_id or edge.get("to") != target_id:
        errors.append(f"{path} must link {source_id} to {target_id}")
    verb = edge.get("verb")
    if not isinstance(verb, str) or not VERB_WORDS[0] <= len(verb.split()) <= VERB_WORDS[1] or verb != verb.lower():
        errors.append(f"{path}.verb must be 1 or 2 lowercase words")
    return errors


def _edge_errors(edges: object, steps: list[Any]) -> list[str]:
    if not isinstance(edges, list) or len(edges) != len(steps) - 1:
        return ["flow.edges must have one edge per consecutive step pair"]
    ids = [step.get("id") if isinstance(step, dict) else None for step in steps]
    errors: list[str] = []
    for index, edge in enumerate(edges):
        errors += _single_edge_errors(index, edge, ids[index], ids[index + 1])
    return errors


def _flow_errors(flow: object) -> list[str]:
    if not isinstance(flow, dict):
        return ["flow must be an object"]
    steps = flow.get("steps")
    if not isinstance(steps, list) or not STEP_COUNT[0] <= len(steps) <= STEP_COUNT[1]:
        return ["flow.steps must have 3 to 5 items"]
    return _step_errors(steps) + _edge_errors(flow.get("edges"), steps)


def _entry_errors(path: str, entries: object, literal_key: str, bounds: tuple[int, int]) -> list[str]:
    if not isinstance(entries, list):
        return [f"{path} must be a list"]
    errors: list[str] = []
    if not bounds[0] <= len(entries) <= bounds[1]:
        errors.append(f"{path} must have {bounds[0]} to {bounds[1]} items")
    for index, entry in enumerate(entries):
        item_path = f"{path}[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{item_path} must be an object")
            continue
        _check_text(f"{item_path}.{literal_key}", entry.get(literal_key), errors)
        _check_words(f"{item_path}.label", entry.get("label"), LABEL_WORDS, errors)
    return errors


def _connection_errors(connections: object) -> list[str]:
    if not isinstance(connections, dict):
        return ["connections must be an object"]
    errors: list[str] = []
    for name, literal_key, bounds in (
        ("flags", "text", OPTIONAL_ITEMS),
        ("files", "text", OPTIONAL_ITEMS),
        ("related", "command", RELATED_ITEMS),
    ):
        errors += _entry_errors(f"connections.{name}", connections.get(name), literal_key, bounds)
    return errors


def _list_words_errors(path: str, items: object) -> list[str]:
    if not isinstance(items, list) or not CONTRAST_ITEMS[0] <= len(items) <= CONTRAST_ITEMS[1]:
        return [f"{path} must have 1 to 3 items"]
    errors: list[str] = []
    for index, item in enumerate(items):
        _check_words(f"{path}[{index}]", item, LABEL_WORDS, errors)
    return errors


def _contrast_errors(contrast: object, command: object) -> list[str]:
    if not isinstance(contrast, dict):
        return ["contrast must be an object"]
    errors = _list_words_errors("contrast.when", contrast.get("when"))
    errors += _list_words_errors("contrast.pitfalls", contrast.get("pitfalls"))
    example = contrast.get("example")
    if not isinstance(example, str) or not isinstance(command, str) or not _starts_with_command(example, command):
        errors.append("contrast.example must start with the command")
    return errors


def _starts_with_command(example: str, command: str) -> bool:
    # A subcommand card id (design-consent) is typed with a space (/design consent).
    return example.startswith((command, command.replace("-", " ", 1)))


def _identity_errors(identity: object) -> list[str]:
    if not isinstance(identity, dict):
        return ["identity must be an object"]
    errors: list[str] = []
    _check_words("identity.purpose", identity.get("purpose"), PURPOSE_WORDS, errors)
    return errors


def _hygiene_errors(node: object, path: str = "blueprint") -> list[str]:
    if isinstance(node, dict):
        return [error for key, child in node.items() for error in _hygiene_errors(child, f"{path}.{key}")]
    if isinstance(node, list):
        return [error for index, child in enumerate(node) for error in _hygiene_errors(child, f"{path}[{index}]")]
    if not isinstance(node, str):
        return []
    if not node or node != node.strip() or "\n" in node or "\r" in node:
        return [f"{path} must be non-empty, unpadded and single-line"]
    return []


def structure_errors(blueprint: Mapping[str, Any], slug: str) -> list[str]:
    """Browser-free rules of contract section 3."""
    errors = _header_errors(blueprint, slug)
    errors += _ui_errors(blueprint.get("ui"))
    errors += _identity_errors(blueprint.get("identity"))
    errors += _flow_errors(blueprint.get("flow"))
    errors += _connection_errors(blueprint.get("connections"))
    errors += _contrast_errors(blueprint.get("contrast"), blueprint.get("command"))
    return errors + _hygiene_errors(blueprint)


def page_errors(blueprint: Mapping[str, Any], facts: PageFacts) -> list[str]:
    """Rules of contract section 3 that need the page's card ids and categories."""
    slug = blueprint["slug"]
    errors: list[str] = []
    if slug not in facts.card_ids:
        errors.append(f"slug {slug} is not a card id of the page")
    if facts.category_by_id.get(slug) != blueprint["category"]:
        errors.append("category does not match the page category of this card")
    for index, related in enumerate(blueprint["connections"]["related"]):
        target = related["command"]
        if target[:1] != "/" or target[1:] not in facts.card_ids:
            errors.append(f"connections.related[{index}].command is not a card id of the page")
    return errors


def audit_blueprint(root: Path, slug: str) -> tuple[dict[str, Any], list[str]]:
    """Structure first (no browser); page rules only when the structure passes."""
    blueprint = load_blueprint(slug_folder(root, slug))
    errors = structure_errors(blueprint, slug)
    if errors:
        return blueprint, errors
    return blueprint, page_errors(blueprint, read_page_facts(root))


def failure(slug: str, errors: list[str]) -> dict[str, Any]:
    return {"ok": False, "slug": slug, "errors": errors}


def closed_list(blueprint: Mapping[str, Any]) -> list[ClosedString]:
    """The closed string list of contract section 3, in its order."""
    entries = _head_entries(blueprint) + _flow_entries(blueprint["flow"])
    entries += _connection_entries(blueprint["connections"]) + _contrast_entries(blueprint["contrast"])
    return [ClosedString(location, text) for location, text in entries]


def _head_entries(blueprint: Mapping[str, Any]) -> list[tuple[str, str]]:
    entries = [("command", blueprint["command"]), ("category", blueprint["category"])]
    entries += [(f"ui.{key}", blueprint["ui"][key]) for key in UI_LABELS]
    return entries + [("identity.purpose", blueprint["identity"]["purpose"])]


def _flow_entries(flow: Mapping[str, Any]) -> list[tuple[str, str]]:
    entries = [(f"flow.steps[{i}].label", step["label"]) for i, step in enumerate(flow["steps"])]
    return entries + [(f"flow.edges[{i}].verb", edge["verb"]) for i, edge in enumerate(flow["edges"])]


def _connection_entries(connections: Mapping[str, Any]) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for name, literal_key in (("flags", "text"), ("files", "text"), ("related", "command")):
        for index, entry in enumerate(connections[name]):
            entries.append((f"connections.{name}[{index}].{literal_key}", entry[literal_key]))
            entries.append((f"connections.{name}[{index}].label", entry["label"]))
    return entries


def _contrast_entries(contrast: Mapping[str, Any]) -> list[tuple[str, str]]:
    entries = [(f"contrast.when[{i}]", text) for i, text in enumerate(contrast["when"])]
    entries += [(f"contrast.pitfalls[{i}]", text) for i, text in enumerate(contrast["pitfalls"])]
    return entries + [("contrast.example", contrast["example"])]


# ---------------------------------------------------------------- browser and page (contract sections 1, 8)


@contextmanager
def open_browser() -> Iterator[Browser]:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=CHROME_PATH, headless=True)
        try:
            yield browser
        finally:
            browser.close()


def guard_requests(page: Page) -> list[str]:
    """Let local schemes through, abort and record every other request."""
    blocked: list[str] = []

    def guard(route: Route) -> None:
        url = route.request.url
        if urlsplit(url).scheme in LOCAL_SCHEMES:
            route.continue_()
            return
        blocked.append(url)
        route.abort()

    page.route("**/*", guard)
    return blocked


@contextmanager
def open_document(browser: Browser, document: Path, size: tuple[int, int], scale: float = 1) -> Iterator[tuple[Page, list[str]]]:
    context = browser.new_context(viewport={"width": size[0], "height": size[1]}, device_scale_factor=scale)
    try:
        page = context.new_page()
        blocked = guard_requests(page)
        page.goto(document.as_uri(), wait_until="load", timeout=PAGE_TIMEOUT_MS)
        yield page, blocked
    finally:
        context.close()


def build_standalone(source: str) -> str:
    return STANDALONE_HEAD + source + STANDALONE_TAIL


def facts_from_globals(data: Mapping[str, Any]) -> PageFacts:
    category_by_id: dict[str, str] = {}
    for category in data["categories"]:
        for card_id in category["ids"]:
            category_by_id.setdefault(card_id, category["name"])
    return PageFacts(card_ids=frozenset(data["cards"]), category_by_id=category_by_id)


def read_page_facts(root: Path) -> PageFacts:
    """Render the page wrapper from a temp file and read COMMANDS and CATEGORIES after the scripts ran."""
    source = read_required_text(root / PAGE_SOURCE)
    with tempfile.TemporaryDirectory(prefix="infographic-page-") as scratch:
        document = Path(scratch) / STANDALONE_PAGE.name
        document.write_bytes(build_standalone(source).encode("utf-8"))
        with open_browser() as browser, open_document(browser, document, CHECK_VIEWPORT) as (page, _blocked):
            try:
                data = page.evaluate(READ_GLOBALS_JS)
            except PlaywrightError as error:
                raise ToolError("COMMANDS or CATEGORIES could not be read from the page") from error
    return facts_from_globals(data)


# ---------------------------------------------------------------- labels and render-template


def labels_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    blueprint, errors = audit_blueprint(root, slug)
    if errors:
        return failure(slug, errors)
    return {"ok": True, "slug": slug, "lines": [entry.text for entry in closed_list(blueprint)]}


def blueprint_warnings(blueprint: Mapping[str, Any]) -> list[str]:
    """Advice that never fails the check: at 16:9 a step label should have at most 5 words."""
    if blueprint.get("aspect") != "16:9":
        return []
    return [
        f"flow.steps[{index}].label has {len(step['label'].split())} words; at 16:9 use at most {WIDE_STEP_WORDS}"
        for index, step in enumerate(blueprint["flow"]["steps"])
        if len(step["label"].split()) > WIDE_STEP_WORDS
    ]


def check_blueprint_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    blueprint, errors = audit_blueprint(root, slug)
    warnings = [] if errors else blueprint_warnings(blueprint)
    return {"ok": not errors, "slug": slug, "errors": errors, "warnings": warnings}


def render_slot(template: str, blueprint: Mapping[str, Any]) -> str:
    """Fill the one blueprint slot by slicing, so backslashes in the JSON are never interpreted."""
    matches = list(SLOT_PATTERN.finditer(template))
    if len(matches) != 1:
        raise ToolError("the template must hold exactly one blueprint slot")
    payload = json.dumps(blueprint, ensure_ascii=False).replace("</", "<\\/")
    slot = matches[0]
    return template[: slot.start(1)] + payload + template[slot.end(1) :]


def render_template_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    blueprint, errors = audit_blueprint(root, slug)
    if errors:
        return failure(slug, errors)
    rendered = render_slot(read_required_text(args.template), blueprint)
    target = slug_folder(root, slug) / VECTOR_NAME
    write_atomic(target, rendered.encode("utf-8"))
    return {"ok": True, "slug": slug, "path": relative(root, target)}


# ---------------------------------------------------------------- check-vector (contract section 4)


def is_network_reference(name: str, value: str) -> bool:
    """Namespace declarations name a URI that is never fetched, so only other values count."""
    declares_namespace = name == "xmlns" or name.startswith("xmlns:")
    if declares_namespace and value in NAMESPACE_URIS:
        return False
    return NETWORK_REFERENCE.search(value) is not None


@dataclass(frozen=True)
class ScriptBlock:
    """One <script> element as the browser will see it: declared type, id, whether it has src, and its raw text."""

    script_type: str
    script_id: str
    has_src: bool
    text: str


def first_attributes(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
    """A browser keeps the first of a repeated attribute, so the scan keeps it too."""
    attributes: dict[str, str] = {}
    for name, value in attrs:
        attributes.setdefault(name, value or "")
    return attributes


class StaticScanner(HTMLParser):
    """Attributes, inline style and <style> are scanned for URLs and active schemes; every <script> is collected."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.findings: list[str] = []
        self.scripts: list[ScriptBlock] = []
        self._raw_tag: str | None = None
        self._raw_attributes: dict[str, str] = {}
        self._raw_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = first_attributes(attrs)
        self._record_tag_findings(tag, attributes)
        for name, value in attrs:
            self._record_attribute_findings(tag, name, value or "")
        if tag in RAW_TEXT_TAGS:
            self._raw_tag = tag
            self._raw_attributes = attributes

    def handle_data(self, data: str) -> None:
        if self._raw_tag is not None:
            self._raw_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == self._raw_tag:
            self._close_raw()

    def close(self) -> None:
        super().close()
        if self._raw_tag is not None:
            self._close_raw()  # an unterminated script or style runs to the end of the document

    def _record_tag_findings(self, tag: str, attributes: Mapping[str, str]) -> None:
        if tag in FORBIDDEN_TAGS:
            self.findings.append(f"<{tag}> is not allowed")
        if tag == "script" and "src" in attributes:
            self.findings.append("<script src> is not allowed")
        if tag == "meta" and "http-equiv" in attributes:
            self.findings.append("<meta http-equiv> is not allowed")

    def _record_attribute_findings(self, tag: str, name: str, value: str) -> None:
        if name.startswith(EVENT_ATTRIBUTE_PREFIX):
            self.findings.append(f"event handler attribute {name} on <{tag}> is not allowed")
        if is_network_reference(name, value):
            self.findings.append(f"network reference in attribute {name} of <{tag}>")
        self.findings.extend(active_scheme_findings(tag, name, value))

    def _close_raw(self) -> None:
        text = "".join(self._raw_text)
        if self._raw_tag == "style":
            if NETWORK_REFERENCE.search(text):
                self.findings.append("network reference inside <style>")
        else:
            self.scripts.append(
                ScriptBlock(
                    script_type=self._raw_attributes.get("type", "").strip().lower(),
                    script_id=self._raw_attributes.get("id", ""),
                    has_src="src" in self._raw_attributes,
                    text=text,
                )
            )
        self._raw_tag = None
        self._raw_attributes = {}
        self._raw_text.clear()


def starts_with_doctype(text: str) -> bool:
    return text.lstrip("﻿ \t\r\n").lower().startswith("<!doctype html>")


def url_key(value: str) -> str:
    """The URL a browser would read: entities decoded once more, lowercased, spaces and control characters dropped."""
    decoded = html.unescape(value).lower()
    return "".join(char for char in decoded if not char.isspace() and unicodedata.category(char)[0] != "C")


def active_scheme_findings(tag: str, name: str, value: str) -> list[str]:
    key = url_key(value)
    schemes = [scheme for scheme in ACTIVE_SCHEMES if scheme in key]
    if name.rsplit(":", 1)[-1] in URL_ATTRIBUTE_NAMES and DATA_HTML_SCHEME in key:
        schemes.append(DATA_HTML_SCHEME)
    return [f"active URL scheme {scheme} in attribute {name} of <{tag}>" for scheme in schemes]


def scan_markup(document: str) -> StaticScanner:
    scanner = StaticScanner()
    scanner.feed(document)
    scanner.close()
    return scanner


def is_executable(block: ScriptBlock) -> bool:
    return not block.has_src and block.script_type != JSON_SCRIPT_TYPE


def script_key(block: ScriptBlock) -> tuple[str, str]:
    """Declared type and sha256 of the text: the same text under another type is another script."""
    return block.script_type, hashlib.sha256(block.text.encode("utf-8")).hexdigest()


def template_script_allowlist(template: str) -> frozenset[tuple[str, str]]:
    """Every executable inline script of the template, by type and sha256; read at run time, never hardcoded."""
    return frozenset(script_key(block) for block in scan_markup(template).scripts if is_executable(block))


def token_findings(text: str) -> list[str]:
    return [f"forbidden token {pattern.pattern} in inline script" for pattern in SCRIPT_TOKEN_PATTERNS if pattern.search(text)]


def script_findings(blocks: Sequence[ScriptBlock], allowlist: frozenset[tuple[str, str]]) -> list[str]:
    findings: list[str] = []
    for block in blocks:
        if block.has_src:
            continue  # already reported as <script src>
        if block.script_type == JSON_SCRIPT_TYPE:
            if block.script_id != BLUEPRINT_SCRIPT_ID:
                findings.append(f'<script type="application/json"> with id "{block.script_id}" is not allowed')
            continue
        key = script_key(block)
        if key not in allowlist:
            findings.append(
                f"inline script of type {block.script_type or 'classic'} is not in the template allowlist"
                f" (sha256 {key[1]})"
            )
            continue
        findings.extend(token_findings(block.text))
    return findings


def static_findings(document: str, allowlist: frozenset[tuple[str, str]]) -> list[str]:
    findings = [] if starts_with_doctype(document) else ["document must start with <!doctype html>"]
    scanner = scan_markup(document)
    return findings + scanner.findings + script_findings(scanner.scripts, allowlist)


def normalize_fragment(value: str) -> str:
    """NFC, entity decoding and whitespace collapse; edge spaces are kept so text nodes can be joined."""
    return re.sub(r"\s+", " ", html.unescape(unicodedata.normalize("NFC", value)))


def strip_marks(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value)
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def error_entry(expected: str, found: str, location: str, issue_type: str) -> dict[str, str]:
    return {"expected": expected, "found": found, "location": location, "issue_type": issue_type}


def longest_prefix_in(expected: str, corpus: str) -> str:
    for length in range(len(expected) - 1, MIN_PREFIX_CHARS - 1, -1):
        if expected[:length] in corpus:
            return expected[:length]
    return ""


def _missing_errors(closed: Sequence[ClosedString], expected_texts: Sequence[str], corpus: str) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    for entry, expected in zip(closed, expected_texts, strict=True):
        if expected in corpus:
            continue
        found = longest_prefix_in(expected, corpus)
        errors.append(error_entry(expected, found, entry.location, "truncated" if found else "typo"))
    return errors


def _unexpected_errors(rendered: Sequence[str], expected_texts: Sequence[str]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    for index, node in enumerate(rendered):
        visible = node.strip()
        if not any(char.isalnum() for char in visible) or any(visible in text for text in expected_texts):
            continue
        closest = difflib.get_close_matches(visible, expected_texts, n=1, cutoff=0.0)
        accent_only = any(strip_marks(visible) in strip_marks(text) for text in expected_texts)
        issue = "missing_accent" if accent_only else "typo"
        errors.append(error_entry(closest[0] if closest else "", visible, f"rendered text node {index + 1}", issue))
    return errors


def text_parity_errors(nodes: Sequence[str], closed: Sequence[ClosedString]) -> list[dict[str, str]]:
    rendered = [normalize_fragment(node) for node in nodes]
    corpus = normalize_fragment("".join(rendered))
    expected_texts = [normalize_fragment(entry.text).strip() for entry in closed]
    return _missing_errors(closed, expected_texts, corpus) + _unexpected_errors(rendered, expected_texts)


def vector_report(findings: list[str], requests: list[str], errors: list[dict[str, str]]) -> dict[str, Any]:
    return {
        "ok": not (findings or requests or errors),
        "static_findings": findings,
        "network_requests": requests,
        "errors": errors,
    }


def check_vector_document(
    browser: Browser, document: Path, closed: Sequence[ClosedString], allowlist: frozenset[tuple[str, str]]
) -> dict[str, Any]:
    text = read_required_text(document)
    findings = static_findings(text, allowlist)
    if findings:
        return vector_report(findings, [], [])
    with open_document(browser, document, CHECK_VIEWPORT) as (page, blocked):
        nodes = page.evaluate(TEXT_NODES_JS)
    return vector_report([], list(blocked), text_parity_errors(nodes, closed))


def run_vector_check(document: Path, blueprint: Mapping[str, Any]) -> dict[str, Any]:
    allowlist = template_script_allowlist(read_required_text(DEFAULT_TEMPLATE))
    with open_browser() as browser:
        return check_vector_document(browser, document, closed_list(blueprint), allowlist)


def check_vector_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    blueprint, errors = audit_blueprint(root, slug)
    if errors:
        return failure(slug, errors)
    document = args.file.resolve() if args.file else slug_folder(root, slug) / VECTOR_NAME
    return {"slug": slug, **run_vector_check(document, blueprint)}


# ---------------------------------------------------------------- downloads (contract section 8)


def resolve_downloads(option: Path | None) -> Path:
    if option is not None:
        return option
    configured = os.environ.get(DOWNLOADS_ENV)
    if configured:
        return Path(configured)
    return xdg_downloads_dir()


def xdg_downloads_dir() -> Path:
    fallback = Path.home() / "Downloads"
    try:
        completed = subprocess.run(
            ["xdg-user-dir", "DOWNLOAD"], capture_output=True, text=True, timeout=XDG_TIMEOUT_S, check=False
        )
    except (OSError, subprocess.TimeoutExpired):
        LOGGER.warning("xdg-user-dir unavailable; using %s", fallback)
        return fallback
    line = completed.stdout.strip()
    return Path(line) if completed.returncode == 0 and line else fallback


def snapshot_listing(folder: Path) -> dict[str, list[int]]:
    if not folder.is_dir():
        raise ToolError("downloads folder not found")
    listing: dict[str, list[int]] = {}
    for entry in folder.iterdir():
        if entry.is_file():
            info = entry.stat()
            listing[entry.name] = [info.st_size, info.st_mtime_ns]
    return listing


def snapshot_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    del root
    listing = snapshot_listing(resolve_downloads(args.downloads))
    write_atomic(args.out, (json.dumps(listing, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    return {"ok": True, "count": len(listing), "out": str(args.out)}


def new_files(folder: Path, snapshot: Mapping[str, Any]) -> list[str]:
    current = snapshot_listing(folder)
    return sorted(
        name
        for name, fingerprint in current.items()
        if Path(name).suffix.lower() not in PARTIAL_SUFFIXES and snapshot.get(name) != fingerprint
    )


def detect_kind(data: bytes) -> str | None:
    if data.startswith(PNG_SIGNATURE):
        return "png"
    if data.startswith(JPEG_SIGNATURE):
        return "jpeg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if starts_with_doctype(data[:HEAD_BYTES].decode("utf-8", errors="ignore")):
        return "html"
    return None


def convert_to_png(data: bytes, mime: str) -> bytes:
    """Load the image in an <img> data URL and screenshot it at its natural size."""
    encoded = base64.b64encode(data).decode("ascii")
    markup = f'<!doctype html><html><body style="margin:0"><img id="picture" src="data:{mime};base64,{encoded}"></body></html>'
    with open_browser() as browser:
        context = browser.new_context(device_scale_factor=1)
        try:
            page = context.new_page()
            page.set_content(markup, wait_until="load", timeout=PAGE_TIMEOUT_MS)
            width, height = page.evaluate(
                "() => { const img = document.getElementById('picture'); return [img.naturalWidth, img.naturalHeight]; }"
            )
            if not width or not height:
                raise ToolError("the downloaded image could not be decoded")
            page.set_viewport_size({"width": width, "height": height})
            return page.locator("#picture").screenshot(type="png", timeout=PAGE_TIMEOUT_MS)
        finally:
            context.close()


def collect_download_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    downloads = resolve_downloads(args.downloads)
    found = new_files(downloads, load_json_object(args.snapshot))
    if len(found) != 1:
        return {"ok": False, "slug": slug, "error": "expected exactly one new complete download", "found": found}
    source = downloads / found[0]
    data = source.read_bytes()
    kind = detect_kind(data)
    if kind is None or kind not in ACCEPTED_KINDS[args.kind]:
        return {"ok": False, "slug": slug, "error": f"the download is not a {args.kind} file", "found": found}
    folder = slug_folder(root, slug)
    target = folder / (VECTOR_NAME if kind == "html" else IMAGE_NAME)
    if kind in MIME_BY_KIND:
        write_atomic(target, convert_to_png(data, MIME_BY_KIND[kind]))
        source.unlink()
    else:
        move_into_place(source, target)
    return {
        "ok": True,
        "slug": slug,
        "source": found[0],
        "target": relative(root, target),
        "detected": kind,
        "converted": kind in MIME_BY_KIND,
    }


# ---------------------------------------------------------------- render-fallback (contract section 8)


def count_pdf_pages(data: bytes) -> int:
    return len(PDF_PAGE_OBJECT.findall(data))


def ensure_single_pdf_page(data: bytes) -> None:
    pages = count_pdf_pages(data)
    if pages != 1:
        raise ToolError(f"the PDF has {pages} pages, expected 1")


def hide_export_controls(page: Page) -> None:
    page.add_style_tag(content=HIDE_ZOOM_CONTROLS_CSS)


def assert_export_controls_hidden(page: Page) -> None:
    """A zoom control with a null box or display none is hidden; any other one would reach the export."""
    visible = page.evaluate(VISIBLE_ZOOM_COUNT_JS, ZOOM_CONTROL_SELECTOR)
    if visible:
        raise ToolError(f"{visible} zoom control(s) still visible in the export")


def render_outputs(browser: Browser, document: Path, size: tuple[int, int]) -> tuple[bytes, bytes]:
    """Return the PNG screenshot and the single-viewport PDF as bytes; zoom controls never reach either."""
    context = browser.new_context(device_scale_factor=RENDER_SCALE)
    try:
        page = context.new_page()
        page.set_viewport_size({"width": size[0], "height": size[1]})
        page.goto(document.as_uri(), wait_until="load", timeout=PAGE_TIMEOUT_MS)
        # Print media puts the template canvas at 1:1 and full bleed, as in the PDF; screen media scales it to fit.
        page.emulate_media(media="print")
        hide_export_controls(page)
        assert_export_controls_hidden(page)
        png = page.screenshot(type="png", full_page=False)
        pdf = page.pdf(
            width=f"{size[0]}px",
            height=f"{size[1]}px",
            print_background=True,
            page_ranges="1",
        )
    finally:
        context.close()
    return png, pdf


def render_fallback_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    blueprint, errors = audit_blueprint(root, slug)
    if errors:
        return failure(slug, errors)
    folder = slug_folder(root, slug)
    document = folder / VECTOR_NAME
    if not document.is_file():
        raise ToolError(f"{VECTOR_NAME} not found")
    size = VIEWPORT_BY_ASPECT[blueprint["aspect"]]
    with open_browser() as browser:
        png, pdf = render_outputs(browser, document, size)
    ensure_single_pdf_page(pdf)
    png_target, pdf_target = folder / IMAGE_NAME, folder / PDF_NAME
    write_atomic(png_target, png)
    write_atomic(pdf_target, pdf)
    return {
        "ok": True,
        "slug": slug,
        "png": relative(root, png_target),
        "pdf": relative(root, pdf_target),
        "pdf_pages": 1,
        "viewport": list(size),
    }


# ---------------------------------------------------------------- check-qa (contract section 5)


def _qa_entry_errors(index: int, entry: object) -> list[str]:
    path = f"errors[{index}]"
    if not isinstance(entry, dict):
        return [f"{path} must be an object"]
    errors = [f"{path}.{key} must be text" for key in QA_ERROR_KEYS if not isinstance(entry.get(key), str)]
    if entry.get("issue_type") not in QA_ISSUE_TYPES:
        errors.append(f"{path}.issue_type is not an allowed type")
    return errors


def _qa_attempt_error(attempt: object) -> list[str]:
    if type(attempt) is not int or not 1 <= attempt <= 3:
        return ["attempt must be 1 to 3"]
    return []


def qa_errors(report: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    if report.get("passed") is not True:
        errors.append("passed must be true")
    errors += _qa_attempt_error(report.get("attempt"))
    if report.get("model_mode") not in QA_MODEL_MODES:
        errors.append("model_mode is not an allowed mode")
    entries = report.get("errors")
    if not isinstance(entries, list):
        return errors + ["errors must be a list"]
    if entries:
        errors.append("errors must be empty")
    for index, entry in enumerate(entries):
        errors += _qa_entry_errors(index, entry)
    return errors


def load_qa_report(folder: Path) -> dict[str, Any] | None:
    if not (folder / QA_NAME).is_file():
        return None
    return load_json_object(folder / QA_NAME)


def check_qa_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    report = load_qa_report(slug_folder(root, slug))
    if report is None:
        raise ToolError(f"{QA_NAME} not found")
    errors = qa_errors(report)
    return {"ok": not errors, "slug": slug, "errors": errors}


# ---------------------------------------------------------------- register (contract sections 6, 7, 8)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_manifest(root: Path) -> dict[str, Any]:
    if not (root / MANIFEST).is_file():
        return {"version": 1, "items": {}}
    manifest = load_json_object(root / MANIFEST)
    if not isinstance(manifest.get("items"), dict):
        raise ToolError("manifest.json must hold an items object")
    return manifest


def manifest_bytes(manifest: Mapping[str, Any]) -> bytes:
    return (json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def block_items(items: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        slug: {field: item.get(field) for field in BLOCK_FIELDS}
        for slug, item in sorted(items.items())
        if item.get("qa_status") == "passed"
    }


def replace_page_block(source: str, items: Mapping[str, Any]) -> str:
    """Replace the lines between the one BEGIN and the one END marker (contract section 7)."""
    lines = source.splitlines(keepends=True)
    begins = [i for i, line in enumerate(lines) if line.lstrip().startswith(BLOCK_BEGIN)]
    ends = [i for i, line in enumerate(lines) if line.lstrip().startswith(BLOCK_END)]
    if len(begins) != 1 or len(ends) != 1 or begins[0] > ends[0]:
        raise ToolError("the page must hold exactly one INFOGRAPHICS BEGIN marker and one END marker")
    payload = json.dumps(block_items(items), ensure_ascii=False, indent=2, sort_keys=True)
    body = f"const INFOGRAPHICS = {payload};\n"
    return "".join(lines[: begins[0] + 1]) + body + "".join(lines[ends[0] :])


def formats_for(root: Path, folder: Path, has: Mapping[str, bool]) -> dict[str, str | None]:
    """The WebP view and the 1920 px download both come from the audited PNG, so they exist exactly when it does."""
    names = {
        "vector": (VECTOR_NAME, has["vector"]),
        "image": (WEBP_NAME, has["image"]),
        "download": (DOWNLOAD_NAME, has["image"]),
        "pdf": (PDF_NAME, has["pdf"]),
    }
    return {key: relative(root, folder / name) if present else None for key, (name, present) in names.items()}


def register_gate_errors(folder: Path, blueprint: Mapping[str, Any], qa: Mapping[str, Any] | None, has: Mapping[str, bool]) -> list[str]:
    """Contract section 8 gates for the register decision table (see the report)."""
    mode = qa["model_mode"] if qa is not None else "vector"
    errors: list[str] = []
    if has["vector"]:
        vector = run_vector_check(folder / VECTOR_NAME, blueprint)
        if not vector["ok"]:
            errors.append("check-vector failed on infographic.html")
    if qa is not None and mode != "vector_fallback" and qa_errors(qa):
        errors.append("check-qa failed on qa-report.json")
    if mode == "notebooklm" and not has["image"]:
        errors.append("image mode needs infographic.png")
    if mode in ("vector", "vector_fallback") and not has["vector"]:
        errors.append(f"{mode} mode needs infographic.html")
    return errors


def register_result(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    slug = args.slug
    blueprint, errors = audit_blueprint(root, slug)
    if errors:
        return failure(slug, errors)
    folder = slug_folder(root, slug)
    has = {"vector": (folder / VECTOR_NAME).is_file(), "image": (folder / IMAGE_NAME).is_file(), "pdf": (folder / PDF_NAME).is_file()}
    qa = load_qa_report(folder)
    if not any(has.values()) and qa is None:
        return failure(slug, ["nothing to register: no infographic files and no qa report"])
    errors = register_gate_errors(folder, blueprint, qa, has)
    if errors:
        return failure(slug, errors)
    mode = qa["model_mode"] if qa is not None else "vector"
    derived = derived_images(folder) if has["image"] else {}
    manifest = load_manifest(root)
    manifest.setdefault("version", 1)
    manifest["items"][slug] = {
        "slug": slug,
        "command": blueprint["command"],
        "formats": formats_for(root, folder, has),
        "qa_status": "passed",
        "model_mode": mode,
        "updated_at": utc_now(),
    }
    new_source = replace_page_block(read_required_text(root / PAGE_SOURCE), manifest["items"])
    for name, payload in derived.items():
        write_atomic(folder / name, payload)
    write_atomic(root / MANIFEST, manifest_bytes(manifest))
    write_atomic(root / PAGE_SOURCE, new_source.encode("utf-8"))
    write_atomic(root / STANDALONE_PAGE, build_standalone(new_source).encode("utf-8"))
    return {
        "ok": True,
        "slug": slug,
        "qa_status": "passed",
        "model_mode": mode,
        "manifest": relative(root, root / MANIFEST),
        "page": relative(root, root / PAGE_SOURCE),
        "standalone": relative(root, root / STANDALONE_PAGE),
    }


HANDLERS: Final[dict[str, Callable[[Path, argparse.Namespace], dict[str, Any]]]] = {
    "check-blueprint": check_blueprint_result,
    "labels": labels_result,
    "render-template": render_template_result,
    "check-vector": check_vector_result,
    "snapshot-downloads": snapshot_result,
    "collect-download": collect_download_result,
    "render-fallback": render_fallback_result,
    "check-qa": check_qa_result,
    "register": register_result,
}


if __name__ == "__main__":
    raise SystemExit(main())
