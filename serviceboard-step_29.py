# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ServiceBoard
from datetime import datetime, timedelta
def get_upcoming_items(items: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    upcoming = []
    for item in items:
        if 'deadline' not in item or 'status' not in item:
            continue
        deadline_str = item['deadline']
        try:
            deadline = datetime.fromisoformat(deadline_str.replace('Z', '+00:00'))
        except ValueError:
            continue
        if now <= deadline < cutoff and item['status'] != 'resolved':
            item['days_left'] = (deadline - now).days
            upcoming.append(item)
    return sorted(upcoming, key=lambda x: x.get('deadline', datetime.max))

def get_overdue_items(items: list[dict]) -> list[dict]:
    now = datetime.now()
    overdue = []
    for item in items:
        if 'deadline' not in item or 'status' not in item:
            continue
        try:
            deadline = datetime.fromisoformat(item['deadline'].replace('Z', '+00:00'))
        except ValueError:
            continue
        if now > deadline and item['status'] != 'resolved':
            overdue.append({**item, 'days_overdue': (now - deadline).days})
    return sorted(overdue, key=lambda x: x.get('deadline', datetime.min))
