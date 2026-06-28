# === Stage 24: Add grouped summaries by category or status ===
# Project: ServiceBoard
def generate_grouped_summary(board_data):
    from collections import defaultdict
    groups = defaultdict(list)
    for item in board_data:
        key = f"{item.get('category', 'Uncategorized')} - {item.get('status', 'Unknown')}"
        groups[key].append(item)
    
    summary_lines = ["# Grouped Summary", ""]
    for category, items in sorted(groups.items()):
        if not items: continue
        statuses = set(i['status'] for i in items)
        priorities = [i.get('priority', 'Normal') for i in items]
        deadlines = [i.get('deadline', '') or '-' for i in items]
        
        summary_lines.append(f"## {category}")
        summary_lines.append(f"- **Statuses**: {', '.join(statuses)}")
        summary_lines.append(f"- **Priorities**: {', '.join(set(priorities))}")
        summary_lines.append(f"- **Total Items**: {len(items)}")
        
        if deadlines:
            min_deadline = min(d for d in deadlines if d != '-')
            max_deadline = max(d for d in deadlines if d != '-')
            summary_lines.append(f"- **Deadlines Range**: {min_deadline} to {max_deadline}")
        else:
            summary_lines.append("- **Deadlines**: No dates set")
        
        summary_lines.append("")
    
    return "\n".join(summary_lines)
