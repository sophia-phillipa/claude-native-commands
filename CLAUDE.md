# CLAUDE.md

Guidance for Claude Code in this repository. The project is a guide to the native Claude Code Desktop slash commands, delivered as one HTML page.

## What ships

- `comandos-nativos.html`: the page. It opens straight from disk and reads the poster images from `assets/infographics/` beside it.
- `assets/infographics/<slug>/`: `infographic.webp` and `infographic-1920.png` for each command that has a poster, plus the poster's sources (`blueprint.json`, `nota.md`, `roteiro.md`, `qa-report.json`).
- `.claude/skills/notebooklm-command-infographic-playbook/`: the skill that guides poster generation in NotebookLM.
- `.gitlab-ci.yml`: the GitLab Pages job. It publishes the page as `index.html` with the poster images, only when a pipeline is started by hand on the default branch; pushes publish nothing.

## Editing the page

- If a local `src/comandos-nativos.html` exists, it is the source: edit it, then rebuild the root page as the first 254 bytes of the current root page, the source, and `\n</html>\n`. Otherwise, edit `comandos-nativos.html` directly.
- Card data lives in the page's inline script: `COMMANDS` plus the arrays `NEW_COMMANDS`, `LOTE7_COMMANDS`, `LOTE8_COMMANDS`, `LOTE9_COMMANDS` and `LOTE10_COMMANDS`, and the maps `ICONS`, `CONTEXTS`, `CATEGORIES`, `MOTION` and `DOCS`. Every card needs 3 examples and an entry in `CATEGORIES`, `CONTEXTS`, `ICONS` and `MOTION`.
- The block between `INFOGRAPHICS:BEGIN` and `INFOGRAPHICS:END`, and `assets/infographics/manifest.json`, are written when a poster is registered. Do not edit them by hand.
- After a change, run `node --check` on the inline script, then open the page at 375 and 1280 px: no console errors and no horizontal scroll.

## Text

- Card text and `README.md` are in Brazilian Portuguese; code, identifiers and comments are in English.
- `README.md` is the only README and describes only the page. Keep its current sections and add no install, prerequisites, uninstall, configuration, how-it-works, status, known-issues, tests, development, changelog, contributions, maintainer or license section.
