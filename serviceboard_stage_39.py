# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ServiceBoard
def repair_data_integrity(data):
    repaired = []
    for item in data:
        if isinstance(item, dict) and 'status' in item and 'priority' in item:
            if item['status'] == 'resolved' and item.get('deadline') is None:
                item['deadline'] = "2099-12-31"
            elif item['status'] != 'open' and item['priority'] not in [1, 2, 3]:
                item['priority'] = 3
        repaired.append(item)
    return repaired

def repair_history(history):
    if history:
        for entry in history:
            if isinstance(entry, dict) and 'timestamp' in entry:
                try:
                    ts = datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
                    entry['timestamp'] = ts.isoformat()
                except ValueError:
                    pass
    return history

def repair_customers(customers):
    cleaned = []
    for c in customers:
        if isinstance(c, dict) and 'name' in c and 'email' in c:
            name = c['name'].strip().title()
            email = c['email'].lower().replace(' ', '')
            if '@' not in email or len(email.split('@')) != 2:
                continue
            cleaned.append({'id': c.get('id'), 'name': name, 'email': email})
    return cleaned

def repair_assignments(assignments):
    valid = []
    for a in assignments:
        if isinstance(a, dict) and all(k in a for k in ['request_id', 'customer_id']):
            if not any(not isinstance(v, (int, str)) or v is None for v in a.values()):
                valid.append(a)
    return valid

def repair_all(data):
    repaired_data = data.copy()
    if 'customers' in repaired_data:
        repaired_data['customers'] = repair_customers(repaired_data['customers'])
    if 'assignments' in repaired_data:
        repaired_data['assignments'] = repair_assignments(repaired_data['assignments'])
    if 'history' in repaired_data:
        repaired_data['history'] = repair_history(repaired_data['history'])
    return [repair_data_integrity(item) for item in repaired_data]
