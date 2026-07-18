# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ServiceBoard
def seed_demo_data(board, customer_repo):
    """Populate board and customer repository with deterministic sample data."""
    customers = [
        ("Alice Johnson",  "alice@example.com",  "High Priority"),
        ("Bob Smith",      "bob@example.com",     "Medium Priority"),
        ("Carol Williams", "carol@example.com",   "Low Priority"),
        ("David Brown",    "david@example.com",   "Medium Priority"),
        ("Eve Davis",      "eve@example.com",     "High Priority"),
    ]
    for i, (name, email, priority) in enumerate(customers):
        board.customers.append(Customers(name=name, email=email))

    tasks = [
        ("Fix login bug on mobile", 2024_10_15, "Eve Davis"),
        ("Update API documentation", 2024_12_01, "Bob Smith"),
        ("Deploy v3.2 to staging",   2024_11_20, "Alice Johnson"),
    ]
    for i, (title, deadline_str, owner) in enumerate(tasks):
        board.tasks.append(Tasks(
            title=title,
            priority="High" if i % 2 == 0 else "Medium",
            assigned_to=owner,
            deadline=datetime.strptime(deadline_str, "%Y_%m_%d").date(),
            status="In Progress" if i < 2 else "Done",
        ))

    customer_repo["alice@example.com"] = Customers(name="Alice Johnson", email="alice@example.com")
