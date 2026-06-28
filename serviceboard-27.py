# === Stage 27: Add monthly summary calculations ===
# Project: ServiceBoard
def calculate_monthly_summary(records):
    from collections import defaultdict
    monthly_stats = defaultdict(lambda: {'total': 0, 'resolved': 0, 'avg_priority': 0})
    for r in records:
        key = f"{r['month']}/{r['year']}"
        monthly_stats[key]['total'] += 1
        if r.get('status') == 'resolved':
            monthly_stats[key]['resolved'] += 1
        monthly_stats[key]['avg_priority'] += r.get('priority', 0)
    for key in monthly_stats:
        stats = monthly_stats[key]
        if stats['total'] > 0:
            stats['avg_priority'] /= stats['total']
    return dict(sorted(monthly_stats.items()))
