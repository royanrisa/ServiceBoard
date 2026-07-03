# === Stage 38: Add data integrity checks for broken references ===
# Project: ServiceBoard
def validate_integrity(data):
    errors = []
    for req in data['requests']:
        cid = req.get('customer_id')
        aid = req.get('assigned_to')
        if cid and cid not in [c['id'] for c in data['customers']]:
            errors.append(f"Request {req['id']}: customer_id {cid} not found")
        if aid and aid not in [u['id'] for u in data['users']]:
            errors.append(f"Request {req['id']}: assigned_to {aid} not found")
    return len(errors) == 0, errors
