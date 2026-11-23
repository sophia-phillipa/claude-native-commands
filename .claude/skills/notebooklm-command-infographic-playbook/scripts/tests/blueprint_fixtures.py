"""Loader for the JSON blueprints under fixtures/blueprints/ (shared by the rule and layout tests)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "blueprints"
FIXTURE_NAMES = sorted(path.stem for path in FIXTURE_DIR.glob("*.json"))
WIDE_WARNING_FIXTURES = {"stress-16x9", "worst-16x9"}


def load_fixture(name: str) -> dict[str, Any]:
    return json.loads((FIXTURE_DIR / f"{name}.json").read_text(encoding="utf-8"))
