# === Stage 67: Add a function that returns key project metrics ===
# Project: ServiceBoard
def project_metrics(board):
    """Return key metrics for a ServiceBoard."""
    total = sum(len(v) for v in board.values())
    open, closed = 0, 0
    late = 0
    for reqs in board.values():
        for r in reqs:
            if "closed" not in r and (r.get("deadline") is None or r["deadline"] < datetime.now()):
                closed += 1
            else:
                open += 1
            deadline = r.get("deadline")
            if deadline and deadline < datetime.now():
                late += 1
    avg_priority = sum(r.get("priority", 0) for reqs in board.values() for r in reqs) / total if total else 0.0
    return {
        "total": total,
        "open": open - closed,
        "closed": closed,
        "late": late,
        "avg_priority": round(avg_priority, 2),
    }
