# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ServiceBoard
def generate_changelog(activity_log):
    """Generate a compact changelog from an activity log."""
    changes = []
    for entry in activity_log:
        if entry.get("type") == "add":
            changes.append(f"+ {entry['description']}")
        elif entry.get("type") == "modify":
            changes.append(f"- {entry['description']}")
        elif entry.get("type") == "remove":
            changes.append(f"~ {entry['description']}")
    return "\n".join(changes) if changes else ""
