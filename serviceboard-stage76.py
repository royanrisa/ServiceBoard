# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ServiceBoard
import signal
import sys


def handle_interrupt(signum, frame):
    print("\nInterrupted by user (Ctrl+C). Exiting gracefully...")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)
signal.signal(signal.SIGTERM, handle_interrupt)
