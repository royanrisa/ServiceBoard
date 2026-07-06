# === Stage 46: Add a schema version field and migration helper ===
# Project: ServiceBoard
import re, json, os


class Schema:
    VERSION = 5


def migrate(db_path):
    """Apply schema migrations to the JSON service board file."""
    db_path = db_path or "service_board.json"
    if not os.path.exists(db_path):
        return {"status": "no_db", "version": 0}

    with open(db_path) as f:
        data = json.load(f)

    current_version = data.get("version", 1)
    migrations = {
        2: lambda d: (d.update({"schemaVersion": 2}), True),
        3: lambda d: (d.update({"schemaVersion": 3}), True),
        4: lambda d: (d.update({"schemaVersion": 4}), True),
    }

    for v in range(2, current_version + 1):
        if v not in migrations:
            continue
        func = migrations[v]
        result, ok = func(data)
        if ok and "schemaVersion" not in data:
            data["schemaVersion"] = v
        if ok:
            break

    with open(db_path, "w") as f:
        json.dump({"version": Schema.VERSION, **data}, f, indent=2)

    return {"status": "migrated", "version": Schema.VERSION}


def validate_board(board):
    errors = []
    if not isinstance(board, dict):
        return ["board must be a dict"]
    for key in ["customers", "assignments"]:
        if key not in board:
            errors.append(f"missing '{key}'")

    for i, cust in enumerate(board.get("customers", [])):
        if not all(k in cust for k in ("name", "email")):
            errors.append(f"customer[{i}] missing fields")

    return errors


if __name__ == "__main__":
    print(migrate())
