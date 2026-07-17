# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ServiceBoard
def reset_demo_data(service_board):
    """Reset all data to demo state for manual testing."""
    service_board.customers = [
        {"id": 1, "name": "Alice Johnson", "email": "alice@example.com"},
        {"id": 2, "name": "Bob Smith", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com"},
    ]
    service_board.employees = [
        {"id": 1, "name": "Eve Wilson", "role": "Senior Engineer"},
        {"id": 2, "name": "Frank Lee", "role": "Junior Developer"},
    ]
    for i in range(5):
        service_board.assignments.append({
            "id": i + 1,
            "customer_id": (i % len(service_board.customers)) + 1,
            "employee_id": (i % len(service_board.employees)) + 1,
            "priority": ["Low", "Medium", "High"][i % 3],
            "status": ["Open", "In Progress", "Resolved"][i % 3] if i < 3 else "Pending",
            "deadline": "2024-12-" + str(30 - (i * 5)),
            "resolution_history": [],
        })
    service_board.assignments[0]["status"] = "Resolved"
    service_board.assignments[0]["resolution_history"].append({
        "timestamp": "2024-11-01T10:00",
        "employee_id": 1,
        "note": "Issue resolved successfully.",
    })
