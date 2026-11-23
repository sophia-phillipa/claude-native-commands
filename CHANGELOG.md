# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and the
project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- The repository is public, with a fresh history. Working notes (`dossier/`, and `work/` except `work/infographic-contracts.md`) stay local and gitignored, and the skill reads the NotebookLM notebook URL from a gitignored `references/notebook.local.md`.

### Added

- Command guide page `comandos-nativos.html`, generated from `src/comandos-nativos.html`, with one card per native Claude Code Desktop slash command.
- Infographic pipeline `infographic-register-tool.py`, with the barriers `check-blueprint`, `check-qa` and `register`.
- 12 infographics (`autocompact`, `btw`, `clear`, `code-review`, `compact`, `context`, `logout`, `loop`, `memory`, `recap`, `review`, `status`), registered in `assets/infographics/manifest.json` with their WebP and 1920 px PNG.
- 229 pytest tests under `.claude/skills/notebooklm-command-infographic-playbook/scripts/tests`.
