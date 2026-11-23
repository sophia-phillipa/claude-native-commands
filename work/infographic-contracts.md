# Infographic skill: shared contracts

Single source for the four build packages (skill text, script, template, page integration) and for the test session. Skill files are written in English; every infographic string is PT-BR.

## 1. Paths

Project root `R` = the root of this repository's clone (on Sophia's machine, `~/projects/claude-native-commands`; GitHub repository sophia-phillipa/claude-native-commands).

| What | Path (relative to `R`) |
| --- | --- |
| Skill | `.claude/skills/gemini-infographic-generator/` |
| Page source (fragment: starts with `<title>`, no doctype) | `src/comandos-nativos.html` |
| Standalone page (built, never edited by hand) | `comandos-nativos.html` |
| Per-command assets | `assets/infographics/<slug>/` |
| Manifest | `assets/infographics/manifest.json` |
| Downloads folder | output of `xdg-user-dir DOWNLOAD` (here `~/Downloads`) |

`<slug>` is the card id: the command name without `/` (`compact`). It must equal an `id` in the page's `COMMANDS` array (`src/comandos-nativos.html`, `const COMMANDS = [` near line 453; a lote 6 block later pushes more ids, so read ids from the rendered `article.cmd[id]` or by evaluating the data, not by regex on one array).

Standalone build: the file is exactly this wrapper around the page source, byte for byte:

```
<!doctype html>\n<html lang="pt-BR" data-theme="dark">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n
<page source>
\n</html>\n
```

The claude.ai artifact is published by the main session only, from `src/comandos-nativos.html`, with the asset files and `capabilities: {downloads: true}`. Nothing in the skill publishes.

## 2. Files in `assets/infographics/<slug>/`

`blueprint.json` (source of truth), `infographic.html` (vector mode), `infographic.png` (image mode, or the PNG rendered from the vector; the audit source), `infographic.webp` (the registered image, converted from the PNG by `register`), `infographic-1920.png` (the registered download, the PNG resized to 1920 px wide by `register`), `infographic.pdf` (optional, rendered from the vector), `qa-report.json` (image audit).

## 3. `blueprint.json` (version 1)

```json
{
  "version": 1,
  "slug": "compact",
  "command": "/compact",
  "category": "Contexto e memória",
  "aspect": "16:9",
  "ui": {
    "zone1": "Identidade e gatilho",
    "zone2": "Fluxo de execução",
    "zone3": "Conexões e variações",
    "when": "Quando usar",
    "pitfalls": "Armadilhas comuns",
    "example": "Exemplo"
  },
  "identity": { "purpose": "Resume a conversa e libera contexto." },
  "flow": {
    "steps": [
      { "id": "s1", "layer": "input", "label": "A conversa enche a janela" },
      { "id": "s2", "layer": "input", "label": "Você digita /compact com instruções" },
      { "id": "s3", "layer": "processing", "label": "O motor lê o histórico" },
      { "id": "s4", "layer": "processing", "label": "O motor escreve resumo fiel" },
      { "id": "s5", "layer": "result", "label": "Sessão segue mais leve" }
    ],
    "edges": [
      { "from": "s1", "to": "s2", "verb": "motiva" },
      { "from": "s2", "to": "s3", "verb": "executa" },
      { "from": "s3", "to": "s4", "verb": "gera" },
      { "from": "s4", "to": "s5", "verb": "reduz" }
    ]
  },
  "connections": {
    "flags": [ { "text": "[instruções]", "label": "Diz o que o resumo preserva" } ],
    "files": [],
    "related": [
      { "command": "/context", "label": "Mede quanto contexto sobrou" },
      { "command": "/autocompact", "label": "Ajusta a compactação automática" },
      { "command": "/clear", "label": "Recomeça com contexto vazio" }
    ]
  },
  "contrast": {
    "when": [ "Perto do limite da sessão", "Antes da compactação automática" ],
    "pitfalls": [ "Sem instruções, detalhes podem sumir", "Mensagens exatas viram resumo" ],
    "example": "/compact mantenha testes e decisões"
  }
}
```

This is the reviewed `/compact` seed; use it as the worked example.

Rules (enforced by `check-blueprint`):
- `version` 1; `slug` matches a card id; `command` is `"/" + slug`; `category` is that card's category name; `aspect` is `"16:9"` or `"4:5"`.
- `ui` has exactly the six keys above with exactly those PT-BR values.
- `flow.steps`: 3 to 5 items, unique `id`s, `layer` in `input | processing | result`, first step `input`, last step `result`. `flow.edges`: a single chain, one edge per consecutive pair (`steps.length - 1` edges), `verb` of 1 or 2 lowercase words.
- Word limits, counted on whitespace-separated tokens: every box label (`flow.steps[].label`, `connections.*[].label`, `contrast.when[]`, `contrast.pitfalls[]`) has 3 to 7 words; `identity.purpose` has at most 12 words; `contrast.when` and `contrast.pitfalls` have 1 to 3 items each. At 16:9, each `flow.steps[].label` should have at most 5 words (Sophia's decision, 22/11/2026): `check-blueprint` reports 6 or 7 words at 16:9 in a `warnings` list of its JSON output without failing.
- Literal identifiers are matched exactly and are exempt from word limits: `command`, `connections.flags[].text`, `connections.files[].text`, `connections.related[].command`, `contrast.example`. Every `related[].command` is `"/" + <an existing card id>`; `contrast.example` starts with `command`.
- `connections.related` has 1 to 3 items (every guide command relates to at least one other card, so zone 3 is never empty); `connections.flags` and `connections.files` have 0 to 3 items each.
- No string is empty, has leading or trailing spaces, or contains a newline.

Closed string list (the `labels` subcommand prints it, one per line, in this order): `command`, `category`, the six `ui` values, `identity.purpose`, each step label, each edge verb, each flag `text` then `label`, each file `text` then `label`, each related `command` then `label`, each `when`, each `pitfalls`, `example`. The image prompt pastes this list verbatim; the vector check uses it as the allowed text.

## 4. Vector check (`check-vector`)

Input `infographic.html`. Fails (exit 1, JSON report on stdout) on any of:
- Does not start with `<!doctype html>` (case-insensitive, after optional BOM and whitespace).
- Network or active content: any `http:`, `https:` or protocol-relative `//host` URL in an attribute, inline style or `<style>` (except an `xmlns` or `xmlns:*` attribute whose value is exactly `http://www.w3.org/2000/svg`, `http://www.w3.org/1999/xlink` or `http://www.w3.org/1999/xhtml`: namespace names are never fetched); `<script src>`, `<link>`, `<iframe>`, `<object>`, `<embed>`, `<form>`, `<base>`, `<meta http-equiv>`; in inline scripts any of `fetch`, `XMLHttpRequest`, `WebSocket`, `EventSource`, `sendBeacon`, `import(`, `importScripts`, `window.open`, `location.`/`location=`, `document.cookie`, `localStorage`, `sessionStorage`, `indexedDB`. Also any request the page attempts while rendered (headless Chrome via Playwright, every non-`file:`/`data:`/`about:` request aborted and recorded).
- Text parity, on the rendered DOM (headless Chrome, after scripts run): collect the visible text of every text node (HTML and SVG `<text>`/`<tspan>`), normalize each with Unicode NFC, HTML entity decoding and whitespace collapse (case-sensitive). (a) Every string of the closed list must occur in the concatenated normalized text → else `missing`. (b) Every normalized text node must be a substring of some closed-list string → else `unexpected` (catches misspellings and invented text). Nodes with no letter or digit (arrows, bullets, `+`, `−`) are exempt.
- Error entries use the image report's shape: `{ "expected", "found", "location", "issue_type" }` with `issue_type` in `typo | missing_accent | garbled | truncated | wrong_language` (for `missing` use `truncated` when a prefix was found, else `typo`; for `unexpected` use `missing_accent` when the NFD-stripped text matches a list string, else `typo`).

## 5. `qa-report.json` (image audit, written by Claude after reading the PNG)

Exactly the user's format:

```json
{ "passed": true, "attempt": 1, "model_mode": "notebooklm", "errors": [] }
```

`model_mode` in `notebooklm | vector_fallback`; `attempt` 1 to 3; each error `{ "expected", "found", "location", "issue_type" }` with `issue_type` in `typo | missing_accent | garbled | truncated | wrong_language`. Approved only when `passed` is `true` and `errors` is empty.

## 6. `manifest.json`

```json
{
  "version": 1,
  "items": {
    "compact": {
      "slug": "compact",
      "command": "/compact",
      "formats": {
        "vector": "assets/infographics/compact/infographic.html",
        "image": "assets/infographics/compact/infographic.webp",
        "download": "assets/infographics/compact/infographic-1920.png",
        "pdf": "assets/infographics/compact/infographic.pdf"
      },
      "qa_status": "passed",
      "model_mode": "notebooklm",
      "updated_at": "2026-11-22T21:00:00Z"
    }
  }
}
```

`formats.*` is a path relative to `R` (and so relative to the page) or `null`. `formats.image` is the `infographic.webp` that `register` converts from the audited `infographic.png` (section 8): the view the modal shows at full size. `formats.download` is the `infographic-1920.png` that `register` resizes from the same PNG (1920 px wide, height from the aspect ratio): the file the page's download button saves as `<slug>-infografico.png`. Both are `null` when there is no audited PNG (vector only). `infographic.png` stays on disk as the audit source and is not registered. `qa_status` in `passed | failed | pending`. `model_mode` in `notebooklm | vector_fallback | vector` (`vector` = only a vector infographic, checked by `check-vector`). Keys sorted; written atomically (temp file + rename), UTF-8, 2-space indent.

## 7. Page integration contract

The page source holds exactly one generated block, inside its main `<script>`, before the cards are rendered:

```
/* INFOGRAPHICS:BEGIN (generated by register_and_check.py; do not edit by hand) */
const INFOGRAPHICS = {};
/* INFOGRAPHICS:END */
```

`register` replaces the text between the two marker lines with `const INFOGRAPHICS = <json>;` where `<json>` holds only manifest items whose `qa_status` is `passed`, keyed by slug, each `{ "command", "formats", "model_mode", "updated_at" }`, then rebuilds the standalone page (section 1). The page shows infographic controls only on cards whose id is a key of `INFOGRAPHICS`.

## 8. Script CLI: `scripts/infographic-register-tool.py`

Python 3 standard library plus Playwright (`from playwright.sync_api import sync_playwright`, launched with `executable_path="/usr/bin/google-chrome"`, headless), and Pillow for `register` only (imported by one helper that both converters use; a missing Pillow is a JSON tool error). Run as `python3 <skill>/scripts/infographic-register-tool.py <subcommand> ...` from any folder; it finds `R` as the folder that holds `src/comandos-nativos.html`, searching upward from the current directory, or from `--root`. Every subcommand prints a JSON result on stdout and exits 0 on success, 1 on a failed check, 2 on bad usage.

| Subcommand | Does |
| --- | --- |
| `check-blueprint <slug>` | Validates `blueprint.json` (section 3) against the page's card ids and categories. |
| `labels <slug>` | Prints the closed string list, one per line (plain text, not JSON). |
| `render-template <slug>` | Fills the skill's `references/infographic-vector.html` with the blueprint (section 9) and writes `infographic.html`. Deterministic. |
| `check-vector <slug> [--file PATH]` | Section 4 on `infographic.html` (or PATH). |
| `snapshot-downloads --out FILE` | Records the names, sizes and mtimes of the files in the Downloads folder. |
| `collect-download <slug> --snapshot FILE --kind png\|html` | Takes the single new, complete file since the snapshot (ignores `.crdownload`/`.part`; fails on zero or several), checks its type by content (PNG signature; JPEG/WebP converted to PNG through Playwright; HTML must pass the doctype check), moves it to `infographic.png` or `infographic.html`. |
| `render-fallback <slug>` | From `infographic.html` renders `infographic.png` (device scale factor 2; viewport 1600x900 for 16:9, 1080x1350 for 4:5) and `infographic.pdf` (one page of the same size, backgrounds printed). |
| `check-qa <slug>` | Validates `qa-report.json` (section 5). |
| `register <slug>` | Requires `check-blueprint` to pass, `check-vector` to pass when `infographic.html` exists, `check-qa` to pass when `infographic.png` came from image mode (`qa-report.json` present and `model_mode` not `vector_fallback`); when `infographic.png` exists, converts it to `infographic.webp` (Pillow, WebP quality 90, same width and height) and to `infographic-1920.png` (Pillow, LANCZOS resize to 1920 px wide, height `round(h * 1920 / w)`, mode kept, PNG optimized), registers both as `formats.image` and `formats.download`, and writes both files only after both are encoded; writes the manifest item, updates the page block (section 7) and rebuilds the standalone page. |

## 9. Vector template contract: `references/infographic-vector.html`

A complete self-contained page (`<!doctype html>`, inline CSS and inline JS only, no external URL of any kind, system fonts) that renders the four zones from a blueprint embedded as `<script type="application/json" id="blueprint">…</script>` (exactly one such element). `render-template` replaces that element's content with `json.dumps(blueprint, ensure_ascii=False)` with every `</` written as `<\/`. Shipped with the `/compact` seed in the slot so it renders as a demo. All visible text comes from the blueprint (the closed list); controls (zoom in, zoom out, reset) are icon-only with `aria-label` and no visible letters. Tooltips may only repeat closed-list strings. `@media print` prints exactly one page at the aspect size, controls hidden.

## 10. Design system (shared by template, skill text and prompts)

Light canvas. Fonts: `system-ui, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`; commands and flags in `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.

| Token | Value | Role |
| --- | --- | --- |
| `--bg` | `#F7F8FC` | canvas |
| `--ink` | `#1A1C29` | main text |
| `--muted` | `#4A4F66` | secondary text, connectors |
| `--line` | `#D5D9E6` | hairlines |
| `--identity` | `#3B2F8F` (text `#FFFFFF`) | zone 1 band |
| `--input` | fill `#E3F0FF`, stroke `#1F6FD1`, text `#0B3B75` | flow: entrada/contexto |
| `--processing` | fill `#EEE7FF`, stroke `#6B46D9`, text `#3A1F8F` | flow: processamento no Claude Code |
| `--result` | fill `#E3F7EA`, stroke `#1E8A4C`, text `#0E4D2A` | flow: resultado/estado final; "Quando usar" |
| `--flags` | fill `#FFF1DB`, stroke `#C27A00`, text `#6B4200` | flags e argumentos |
| `--files` | fill `#DDF5F5`, stroke `#0F8A8A`, text `#0A4F4F` | arquivos impactados |
| `--related` | fill `#FDE6F1`, stroke `#C2307A`, text `#6E1243` | comandos relacionados |
| `--pitfalls` | fill `#FDE4E1`, stroke `#C0392B`, text `#6B1A12` | armadilhas comuns |

Every text/background pair above is at least 4.5:1 (WCAG AA). Spacing on an 8 px grid; boxes 12 px radius, 2 px stroke. Connectors: 2 px `--muted` lines with filled arrowheads; the verb sits on a `--bg` pill centered on the arrow, 600 weight. Sizes at 1600x900: command title 56/700, purpose 24/400, zone headings 18/700 uppercase with 0.08em tracking, box labels 20/600 (16:9 step labels 24/600, dropping to 20/600 only when a label would overflow its box), verbs 16/600. Layout 16:9: zone 1 as a top band; zone 2 a left-to-right chain across the middle; zone 3 a row of three groups (flags, files, related) under it; zone 4 a bottom band split "Quando usar" | "Armadilhas comuns" | "Exemplo". Layout 4:5: the same order stacked, the flow chain vertical.
