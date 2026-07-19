# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ServiceBoard
def generate_validation_report(boards):
    warnings, errors = [], []
    for board in boards:
        if not isinstance(board, dict):
            errors.append(f"Board is not a dictionary")
            continue
        required_keys = ["id", "customer_id", "assignee_id"]
        missing = [k for k in required_keys if k not in board]
        if missing:
            errors.append(f"Board {board.get('id')} missing keys: {missing}")
        else:
            warnings.append(f"Board {board['id']} has all required fields")

    return {"warnings": warnings, "errors": errors}
