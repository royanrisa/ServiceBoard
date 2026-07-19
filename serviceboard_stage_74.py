# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ServiceBoard
def snapshot_diff(before, after):
    """Compare two state dicts and return a human-readable diff string."""
    if before is None:
        return "Created"
    if after is None:
        return "Deleted"
    changes = []
    for key in set(list(before.keys()) + list(after.keys())):
        b, a = before.get(key), after.get(key)
        if b != a and (b is not None or a is not None):
            old = repr(b) if b is not None else "(None)"
            new = repr(a) if a is not None else "(None)"
            changes.append(f"  {key}: {old} -> {new}")
    return "\n".join(changes) if changes else "No changes."
