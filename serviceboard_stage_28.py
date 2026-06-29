# === Stage 28: Add overdue item detection based on due dates ===
# Project: ServiceBoard
from datetime import datetime, timedelta

def detect_overdue_items(orders):
    today = datetime.now().date()
    overdue_list = []
    for order in orders:
        due_date = datetime.strptime(order['deadline'], '%Y-%m-%d').date()
        if due_date < today and not order.get('resolved', False):
            days_overdue = (today - due_date).days
            status = "Опоздал на {} дней".format(days_overdue)
            overdue_list.append({**order, 'status': status})
    return overdue_list
