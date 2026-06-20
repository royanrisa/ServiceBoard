# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ServiceBoard
def update_service_request(board, request_id, updates):
    if request_id not in board['requests']:
        raise ValueError(f"Request {request_id} not found")
    req = board['requests'][request_id]
    for key, value in updates.items():
        if key in ['id', 'created_at']: continue
        if value is None:
            if key in req: del req[key]
        else:
            req[key] = value
    return req
