# === Stage 55: Add a setting to disable colorized output ===
# Project: ServiceBoard
import sys


def disable_color():
    """Disable ANSI color codes in terminal output."""
    if hasattr(sys.stdout, "isatty") and sys.stdout.isatty():
        sys.stdout.reconfigure(encoding="utf-8")
        # Force plain text by setting the TERM environment variable
        import os
        os.environ["TERM"] = "dumb"
