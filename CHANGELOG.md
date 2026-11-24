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
- README: screenshots of the `/simplify`, `/memory` and `/rewind` cards, a catalog that links all 78 registered posters, and a wording review.
- README covers only the page. The install, how-it-works, prerequisites, uninstall, configuration, known-issues, tests, development, changelog, contributions, maintainer and license sections are gone, and Uso says the page needs the infographics folder beside it and keeps its dependencies to a minimum. A wording review (Fable 5.2 as advisor) tightened three more lines, and the catalog marks commands still waiting for a poster as "em preparo".
- The register script and its tests are no longer in the repositories; they stay local while the posters are generated.
- The repositories keep one HTML page, the root `comandos-nativos.html`; its source `src/comandos-nativos.html` stays local while the posters are generated. The README Status section is gone, and `CLAUDE.md` is cut to what an editor of the page needs.

### Added

- Command guide page `comandos-nativos.html`, with one card per native Claude Code Desktop slash command.
- GitLab Pages job (`.gitlab-ci.yml`): publishes the page and its poster images when a pipeline is started by hand on the default branch.
- Cards for `/agents`, `/help` and `/whiteboard`; the guide now has 82 cards.
- 78 infographics (`add-dir`, `advisor`, `artifact-capabilities`, `artifact-diagramming`, `auto-mode-setup`, `autocompact`, `batch`, `btw`, `bug`, `claude-api`, `clear`, `code-review`, `color`, `compact`, `config`, `context`, `copy`, `cost`, `dataviz`, `debug`, `deep-research`, `design`, `design-consent`, `design-revoke`, `design-sync`, `diff`, `doctor`, `effort`, `fast`, `feedback`, `fewer-permission-prompts`, `focus`, `fork`, `goal`, `heapdump`, `import`, `init`, `insights`, `list-agents`, `login`, `logout`, `loop`, `mcp`, `memory`, `model`, `output-style`, `permissions`, `plan`, `plugin`, `plugin-authoring`, `recap`, `reload-plugins`, `reload-skills`, `remote-control`, `rename`, `resume`, `review`, `rewind`, `run`, `run-skill-generator`, `sandbox`, `security-review`, `simplify`, `skill-doctor`, `skills`, `slides`, `stats`, `status`, `subtask`, `tasks`, `team-onboarding`, `theme`, `ultrareview`, `update-config`, `usage`, `usage-credits`, `workflow-authoring`, `workflows`), registered in `assets/infographics/manifest.json` with their WebP and 1920 px PNG.
