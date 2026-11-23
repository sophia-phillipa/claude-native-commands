# Design system for the command infographics

**Vector fallback only.** Not used by the normal NotebookLM flow, which takes its look from the Studio recipe. The tokens are the contract's section 10; this file expands them into layouts, contrast, print rules and the brief. The vector template (`references/infographic-vector.html`) follows the same values. Light canvas only.

## 1. Tokens

| Token | Value | Role |
| --- | --- | --- |
| `--bg` | `#F7F8FC` | canvas |
| `--ink` | `#1A1C29` | main text |
| `--muted` | `#4A4F66` | secondary text, connectors, verb pill text |
| `--line` | `#D5D9E6` | hairlines only (decorative, carries no text or meaning) |
| `--identity` | `#3B2F8F`, text `#FFFFFF` | zone 1 band |
| `--input` | fill `#E3F0FF`, stroke `#1F6FD1`, text `#0B3B75` | flow: input |
| `--processing` | fill `#EEE7FF`, stroke `#6B46D9`, text `#3A1F8F` | flow: processing in Claude Code |
| `--result` | fill `#E3F7EA`, stroke `#1E8A4C`, text `#0E4D2A` | flow: result; "Quando usar" |
| `--flags` | fill `#FFF1DB`, stroke `#C27A00`, text `#6B4200` | flags and arguments |
| `--files` | fill `#DDF5F5`, stroke `#0F8A8A`, text `#0A4F4F` | impacted files |
| `--related` | fill `#FDE6F1`, stroke `#C2307A`, text `#6E1243` | related commands |
| `--pitfalls` | fill `#FDE4E1`, stroke `#C0392B`, text `#6B1A12` | "Armadilhas comuns" |

Fonts: `system-ui, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`. Commands, flags and file names: `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.

## 2. Contrast (computed with the WCAG 2.x relative-luminance formula)

Text pairs, required 4.5:1 (WCAG 2.2 AA, 1.4.3):

| Text | On | Ratio | Result |
| --- | --- | --- | --- |
| `--ink` `#1A1C29` | `--bg` `#F7F8FC` | 15.93 | pass |
| `--muted` `#4A4F66` | `--bg` `#F7F8FC` | 7.61 | pass |
| `#FFFFFF` | `--identity` `#3B2F8F` | 10.56 | pass |
| `#0B3B75` | input fill `#E3F0FF` | 9.58 | pass |
| `#3A1F8F` | processing fill `#EEE7FF` | 9.88 | pass |
| `#0E4D2A` | result fill `#E3F7EA` | 8.87 | pass |
| `#6B4200` | flags fill `#FFF1DB` | 7.84 | pass |
| `#0A4F4F` | files fill `#DDF5F5` | 8.22 | pass |
| `#6E1243` | related fill `#FDE6F1` | 9.70 | pass |
| `#6B1A12` | pitfalls fill `#FDE4E1` | 9.74 | pass |

Non-text pairs, required 3:1 (WCAG 2.2 1.4.11) where the stroke or connector carries meaning:

| Element | On | Ratio | Result |
| --- | --- | --- | --- |
| input stroke `#1F6FD1` | `--bg` | 4.65 | pass |
| processing stroke `#6B46D9` | `--bg` | 5.65 | pass |
| result stroke `#1E8A4C` | `--bg` | 4.13 | pass |
| flags stroke `#C27A00` | `--bg` | 3.26 | pass |
| files stroke `#0F8A8A` | `--bg` | 3.94 | pass |
| related stroke `#C2307A` | `--bg` | 4.95 | pass |
| pitfalls stroke `#C0392B` | `--bg` | 5.12 | pass |
| connector `--muted` | `--bg` | 7.61 | pass |
| hairline `--line` | `--bg` | 1.33 | decorative only; never the sole cue for anything |

Rules that follow: a verb pill uses `--ink` (15.93) or `--muted` (7.61) text on `--bg`; no text goes on `--line`; a box keeps its text colour from its own row above, never a neighbour's.

## 3. Spacing and shape

- Spacing on an 8 px grid: 8, 16, 24, 32, 48, 64. Box padding 16 or 24 px; gaps between zones 32 or 48 px.
- Boxes: 12 px radius, 2 px stroke in the token's stroke colour.
- Connectors: 2 px `--muted` lines with filled arrowheads.
- Verb pill: height 32 px, horizontal padding 16 px, `--bg` fill, 16 px / 600 text, centred on the connector.

## 4. Type scale (1600x900)

| Role | Size / weight | Note |
| --- | --- | --- |
| command title | 56 / 700 | the command as typed, monospace |
| purpose | 24 / 400 | `identity.purpose` |
| zone heading | 18 / 700 | uppercase with 0.08 em tracking in the vector; in the image keep the listed case |
| box label | 20 / 600 | |
| verb | 16 / 600 | |
| code (flags, files, examples) | 18 / 400 | monospace |

Only the 1600x900 scale comes from the contract. The 4:5 canvas (1080x1350) keeps the same pixel sizes, so labels wrap onto two lines instead of shrinking; this is a design choice of this skill, not a contract value.

## 5. Layouts

**16:9 (1600x900).** Four zones, top to bottom:

1. Zone 1, identity band full width, `--identity` fill: zone heading, command title, category, purpose.
2. Zone 2, a left-to-right chain across the middle: 3 to 5 boxes by `layer` colour; each arrow carries its verb pill.
3. Zone 3, a row of three groups under the chain: flags (`--flags`), impacted files (`--files`), related commands (`--related`). A group with no items in the blueprint is left out together with its heading; no empty-state text is invented.
4. Zone 4, a bottom band of three columns: "Quando usar" (`--result`) | "Armadilhas comuns" (`--pitfalls`) | "Exemplo" (`--bg` fill, `--muted` stroke, monospace `--ink` text).

**4:5 (1080x1350).** The same four zones in the same order, stacked. The flow chain runs top to bottom, and each verb pill sits on its vertical arrow. Zone 3 groups stack one above another. Zone 4 stacks its three cards.

Zone 4 has no heading of its own: the contract's `ui` object has no zone 4 title. Do not render "Contraste prático" or any other zone 4 title; it is not in the closed list, and the vector check would report it as unexpected text.

## 6. Print

- `@page { size: 1600px 900px; margin: 0; }` for 16:9; `1080px 1350px` for 4:5. The size equals the canvas.
- The canvas is one element of that exact size with `overflow: hidden` and no page break inside it.
- `-webkit-print-color-adjust: exact; print-color-adjust: exact;` so the fills print.
- Controls hidden in `@media print`.
- Acceptance: `render-fallback` writes a PDF of exactly one page; more than one page fails the print check.

## 7. WCAG AA checklist for the vector

- Every text pair in section 2 at or above 4.5:1; every meaningful stroke at or above 3:1.
- Controls (zoom in, zoom out, reset) are icon-only with an `aria-label` and a visible focus ring (2 px `--ink` outline, 2 px offset).
- Icon-only controls carry no visible letters; tooltips repeat only closed-list strings.
- No information is carried by colour alone: each group keeps its heading and each arrow keeps its verb pill, so the colour only adds to the text.

## 8. Design brief for the vector fallback

Used only by the fallback (SKILL.md, Emergency fallback). The prose is English; every label it quotes is PT-BR and is copied exactly from the closed list.

> Design brief: one infographic on a light canvas (#F7F8FC), in the aspect given by the prompt (16:9 landscape, or 4:5 portrait). Four zones, in this order. Zone 1 is a full-width top band in deep indigo (#3B2F8F) with white text: the zone heading "Identidade e gatilho", the command as a large title, the category, and one line of purpose. Zone 2 is a left-to-right chain across the middle, headed "Fluxo de execução": 3 to 5 rounded boxes joined by arrows, each arrow with its verb in a small light pill on the line. Input boxes are blue (fill #E3F0FF, stroke #1F6FD1, text #0B3B75); processing boxes are violet (fill #EEE7FF, stroke #6B46D9, text #3A1F8F); the result box is green (fill #E3F7EA, stroke #1E8A4C, text #0E4D2A). Zone 3, headed "Conexões e variações", is a row of three groups: flags in amber (fill #FFF1DB, stroke #C27A00), impacted files in teal (fill #DDF5F5, stroke #0F8A8A), related commands in pink (fill #FDE6F1, stroke #C2307A). Zone 4 is a bottom band of three cards: "Quando usar" in green (fill #E3F7EA, stroke #1E8A4C), "Armadilhas comuns" in red (fill #FDE4E1, stroke #C0392B), and "Exemplo" in a neutral card with a muted border and monospace text. Use a clean system sans-serif for text and a monospace face for commands, flags and file names. Corners 12 px, strokes 2 px, spacing on an 8 px grid. Show nothing except the labels given: no logo, no watermark, no caption, no decorative words, no extra title, no numbers that are not in the labels.
