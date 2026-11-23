# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and the
project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- The repository is public, with a fresh history. Working notes (`dossier/`, and `work/` except `work/infographic-contracts.md`) stay local and gitignored, and the skill reads the NotebookLM notebook URL from a gitignored `references/notebook.local.md`.
- Command guide card text corrected against the 2026-11-23 source recheck: 58 wording fixes, the reload-skills and rewind notes, two docs links and the `/doctor` app field.

### Added

- Command guide page `comandos-nativos.html`, generated from `src/comandos-nativos.html`, with one card per native Claude Code Desktop slash command.
- Cards for `/agents`, `/help` and `/whiteboard`; the guide now has 82 cards.
- Infographic pipeline `infographic-register-tool.py`, with the barriers `check-blueprint`, `check-qa` and `register`.
- 15 infographics (`autocompact`, `btw`, `clear`, `code-review`, `compact`, `context`, `logout`, `loop`, `memory`, `model`, `recap`, `resume`, `review`, `rewind`, `status`), registered in `assets/infographics/manifest.json` with their WebP and 1920 px PNG.
- 229 pytest tests under `.claude/skills/notebooklm-command-infographic-playbook/scripts/tests`.
