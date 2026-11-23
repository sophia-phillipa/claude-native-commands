# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and the
project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- README rewritten for a company audience: screenshots of the guide in `docs/screenshots/` and a gallery of registered posters.
- The repository is public, with a fresh history. Working notes (`dossier/`, and `work/` except `work/infographic-contracts.md`) stay local and gitignored, and the skill reads the NotebookLM notebook URL from a gitignored `references/notebook.local.md`.
- Command guide card text corrected against the 2026-11-23 source recheck: 58 wording fixes, the reload-skills and rewind notes, two docs links and the `/doctor` app field.
- Card arguments checked against the docs signatures: `/model`, `/effort` and `/goal` show their argument as optional, and `/simplify`, `/doctor`, `/context`, `/design-sync` and `/claude-in-chrome` list the optional argument they take.
- README: screenshots of the `/simplify`, `/memory` and `/rewind` cards, a catalog that links all 17 registered posters, and a wording review.
- README covers only the page. The install, how-it-works, prerequisites, uninstall, configuration, known-issues, tests, development, changelog, contributions, maintainer and license sections are gone, and usage is now opening the file.
- The register script and its tests are no longer in the repositories; they stay local while the posters are generated.

### Added

- Command guide page `comandos-nativos.html`, generated from `src/comandos-nativos.html`, with one card per native Claude Code Desktop slash command.
- Cards for `/agents`, `/help` and `/whiteboard`; the guide now has 82 cards.
- 17 infographics (`autocompact`, `btw`, `clear`, `code-review`, `compact`, `context`, `logout`, `loop`, `memory`, `model`, `recap`, `resume`, `review`, `rewind`, `security-review`, `simplify`, `status`), registered in `assets/infographics/manifest.json` with their WebP and 1920 px PNG.
