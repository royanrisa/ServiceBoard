# === Stage 72: Add Markdown report export ===
# Project: ServiceBoard
def export_report(board, path=None):
    if path is None:
        path = "serviceboard_report.md"
    with open(path, "w") as f:
        f.write("ServiceBoard Report\n")
        f.write("=" * 60 + "\n\n")
        for entry in board:
            status = entry["status"]
            if status == "open":
                s = "Open"
            elif status == "in_progress":
                s = "In Progress"
            else:
                s = "Resolved"
            f.write(f"- [{entry['id']}] {s} | Customer: {entry['customer']} | Priority: {entry['priority']} | Assigned to: {entry.get('assigned_to', 'None')} | Deadline: {entry.get('deadline', 'N/A')}\n")
        f.write("\nTotal entries:\n")
        for entry in board:
            if entry["status"] == "open":
                print(f"Open: {entry['id']}")
