# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ServiceBoard
import csv, datetime

def format_priority(p):
    return {1:'Low',2:'Medium',3:'High'}.get(p,'Unknown')

def fmt_date(d):
    try:
        return d.strftime('%Y-%m-%d %H:%M') if hasattr(d,'strftime') else str(d)
    except Exception:
        return str(d)

def parse_csv(path, sep=','):
    with open(path, newline='') as f:
        reader = csv.reader(f, delimiter=sep)
        rows = list(reader)
    return [dict(zip(rows[0], r)) for r in rows[1:] if any(r)]

def load_board(path):
    data = parse_csv(path)
    board = []
    for row in data:
        board.append({
            'id': row.get('id',''),
            'customer': row.get('customer',''),
            'assigned_to': row.get('assigned_to',''),
            'priority': int(row.get('priority',2)),
            'deadline': datetime.datetime.strptime(row['deadline'],'%Y-%m-%d') if 'deadline' in row else None,
            'status': row.get('status','Open'),
            'resolution_notes': row.get('resolution_notes',''),
        })
    return board

def render_board(board):
    lines = ['ServiceBoard\n']
    for entry in sorted(board, key=lambda x: (x['priority'], -int(x['deadline'].strftime('%Y%m%d')) if x['deadline'] else 0)):
        deadline_str = fmt_date(entry['deadline']) if entry['deadline'] else 'N/A'
        lines.append(f"[{entry['id']}] {entry['customer']} | {format_priority(entry['priority'])} | "
                     f"{entry['assigned_to']:>12s} | Deadline: {deadline_str} | Status: {entry['status']}")
    return '\n'.join(lines)

def filter_by_status(board, status):
    return [e for e in board if e['status'] == status]

def sort_by_deadline_ascending(board):
    return sorted(board, key=lambda x: x['deadline'] or datetime.datetime.max)

def export_csv(board, path):
    with open(path,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['id','customer','assigned_to','priority','deadline','status','resolution_notes'])
        for e in board:
            w.writerow([e['id'],e['customer'],e['assigned_to'],e['priority'],
                        fmt_date(e['deadline']),e['status'],e.get('resolution_notes','')])
