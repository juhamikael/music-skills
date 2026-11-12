"""The MCP server starts without the mastering dependencies.

Core-tier use (lyrics, albums, Suno prompts) installs only ``mcp`` and
``pyyaml``. The mastering tools check for numpy, scipy, soundfile and
pyloudnorm when they are called (``_helpers._check_mastering_deps``), so no
module the server imports at startup may import them at module level.

Each check runs in a fresh interpreter with those packages blocked, because
the test environment has them installed and already imported.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[3]
SERVER_DIR = PROJECT_ROOT / "servers" / "bitwize-music-server"

pytestmark = pytest.mark.skipif(
    importlib.util.find_spec("mcp") is None,
    reason="the real MCP SDK is needed to start the server",
)

_BLOCK_HEAVY_DEPS = textwrap.dedent(
    """
    import sys

    BLOCKED = ("numpy", "scipy", "soundfile", "pyloudnorm")

    class _Blocker:
        def find_spec(self, name, path=None, target=None):
            if name.split(".")[0] in BLOCKED:
                raise ModuleNotFoundError(f"No module named {name!r}", name=name)
            return None

    sys.meta_path.insert(0, _Blocker())
    sys.path.insert(0, sys.argv[1])
    sys.path.insert(0, sys.argv[2])
    """
)


def _run(body: str) -> dict[str, object]:
    script = _BLOCK_HEAVY_DEPS + textwrap.dedent(body)
    proc = subprocess.run(  # noqa: S603 — fixed interpreter and script
        [sys.executable, "-c", script, str(SERVER_DIR), str(PROJECT_ROOT)],
        capture_output=True,
        text=True,
        check=False,
        cwd=SERVER_DIR,
    )
    assert proc.returncode == 0, proc.stderr
    result: dict[str, object] = json.loads(proc.stdout.strip().splitlines()[-1])
    return result


def test_server_imports_without_mastering_deps() -> None:
    result = _run(
        """
        import json
        import server  # noqa: F401
        loaded = sorted(m for m in sys.modules if m.split(".")[0] in BLOCKED)
        print(json.dumps({"loaded": loaded}))
        """
    )
    assert result["loaded"] == []


def test_mastering_tools_report_missing_deps() -> None:
    result = _run(
        """
        import asyncio
        import json
        import server  # noqa: F401
        from handlers.processing import audio

        album = json.loads(asyncio.run(audio.master_album("x")))
        single = json.loads(asyncio.run(audio.analyze_audio("x")))
        print(json.dumps({"album": album, "single": single}))
        """
    )
    album = result["album"]
    assert isinstance(album, dict)
    assert album["failed_stage"] == "pre_flight"
    assert "Missing mastering dependencies" in album["failure_detail"]["reason"]
    single = result["single"]
    assert isinstance(single, dict)
    assert "Missing mastering dependencies" in single["error"]
