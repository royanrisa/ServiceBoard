# === Stage 66: Add export of a short status dashboard ===
# Project: ServiceBoard
def export_dashboard(boards):
    """Export a compact status dashboard from all boards."""
    total = sum(len(b) for b in boards)
    active, overdue = 0, 0
    by_priority = {}
    resolution_history = []
    for board in boards:
        for req in board:
            active += 1
            if req["deadline"] and req["deadline"] < datetime.now():
                overdue += 1
            p = req.get("priority", "normal")
            by_priority[p] = by_priority.get(p, 0) + 1
            resolution_history.append({
                "request_id": req["id"],
                "customer": req["customer"],
                "assigned_to": req["assigned_to"],
                "status": req["status"],
                "resolved_at": req.get("resolved_at"),
            })
    return {
        "total_requests": total,
        "active": active,
        "overdue": overdue,
        "by_priority": by_priority,
        "resolution_history": resolution_history[-20:],  # last 20 resolved items
    }
