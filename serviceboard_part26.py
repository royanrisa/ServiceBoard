# === Stage 26: Add weekly summary calculations ===
# Project: ServiceBoard
def calculate_weekly_summary(data):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    weekly_stats = {
        "week_range": f"{week_start} to {week_end}",
        "total_requests": 0,
        "resolved_count": 0,
        "pending_count": 0,
        "avg_resolution_days": 0.0,
        "overdue_count": 0
    }

    for req in data:
        weekly_stats["total_requests"] += 1
        
        if req.get("status") == "resolved":
            weekly_stats["resolved_count"] += 1
            resolved_date = date.fromisoformat(req["resolved_at"])
            days_to_resolve = (resolved_date - date.fromisoformat(req["created_at"]).date()).days
            weekly_stats["avg_resolution_days"] += days_to_resolve
        
        if req.get("status") == "pending":
            weekly_stats["pending_count"] += 1
            
        created_date = date.fromisoformat(req["created_at"])
        deadline_date = date.fromisoformat(req["deadline"])
        
        if req.get("status") != "resolved" and deadline_date < today:
            weekly_stats["overdue_count"] += 1

    if weekly_stats["total_requests"] > 0:
        weekly_stats["avg_resolution_days"] /= weekly_stats["resolved_count"]

    return weekly_stats
