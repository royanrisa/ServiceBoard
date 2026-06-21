# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ServiceBoard
def format_service_request(req):
    status = f"[{req['status']}] {req['id']} | {req['customer_name']:15} | {req['assignee']:12} | P:{req['priority']:>3}"
    if req.get('deadline'):
        status += f" | Due: {req['deadline'][:10]}"
    return status

def format_resolution_history(history):
    lines = []
    for entry in history:
        action, date, details = entry['action'], entry['date'], entry['details']
        color = "✓" if action == 'resolved' else ("⚠" if action == 'escalated' else "-")
        lines.append(f"{color} {date}: {action.upper()} - {details}")
    return "\n".join(lines)

def print_board_header():
    print("=" * 80)
    print(" SERVICE REQUEST BOARD ".center(76, "="))
    print("=" * 80)
