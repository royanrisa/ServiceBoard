# === Stage 25: Add daily summary calculations ===
# Project: ServiceBoard
def calculate_daily_summary(board_data):
    from collections import defaultdict
    today = datetime.date.today()
    daily_stats = defaultdict(lambda: {'total': 0, 'resolved': 0, 'overdue': 0})
    for req in board_data['requests']:
        date_key = req.get('date_created', str(today))
        if isinstance(date_key, datetime.datetime):
            date_key = date_key.date()
        daily_stats[date_key]['total'] += 1
        if req.get('status') == 'resolved':
            daily_stats[date_key]['resolved'] += 1
        deadline = req.get('deadline', today)
        if isinstance(deadline, datetime.datetime):
            deadline = deadline.date()
        elif not isinstance(deadline, str):
            continue
        try:
            if date_key < deadline and req['status'] != 'resolved':
                daily_stats[date_key]['overdue'] += 1
        except TypeError:
            pass
    summary_list = []
    for date in sorted(daily_stats.keys()):
        stats = daily_stats[date]
        summary_list.append({
            'date': date,
            'total_requests': stats['total'],
            'resolved_count': stats['resolved'],
            'pending_overdue': stats.get('overdue', 0)
        })
    return summary_list
