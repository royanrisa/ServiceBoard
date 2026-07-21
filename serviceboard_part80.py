# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: ServiceBoard
def print_board_summary(board):
    """Display a clean, user-facing summary of all active requests."""
    if not board.requests:
        print("ServiceBoard is currently empty.")
        return
    print(f"\n{'='*50}")
    print("  SERVICE REQUEST BOARD")
    print(f"{'='*50}")
    for req in sorted(board.requests, key=lambda r: (r.priority, r.deadline)):
        status_emoji = {"open": "🔵", "assigned": "🟡", "resolved": "✅", "overdue": "⚠️"}.get(req.status, "❓")
        print(f"\n  {status_emoji} [{req.id}] {req.title}")
        print(f"      Customer: {req.customer}")
        print(f"      Assigned to: {req.assigned_by or 'Unassigned'} | Priority: {req.priority}")
        if req.resolution_history:
            last = req.resolution_history[-1]
            print(f"      Status: {last.status} (resolved by {last.resolved_by})")
        else:
            print(f"      Deadline: {req.deadline.strftime('%Y-%m-%d') or 'None'} | Resolution history: none yet.")
    print(f"\n{'='*50}")
