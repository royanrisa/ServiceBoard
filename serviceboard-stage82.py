# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: ServiceBoard
def demo():
    board = ServiceBoard()
    c1 = Customer("Alice", "alice@example.com")
    c2 = Customer("Bob", "bob@example.com")
    board.add_customer(c1)
    board.add_customer(c2)
    a1 = Assignment(
        title="Fix login bug",
        customer=c1,
        assignee="Dev Team A",
        priority=Priority.HIGH,
        deadline=datetime(2025, 4, 30),
        status=Status.OPEN,
    )
    a2 = Assignment(
        title="Update dashboard UI",
        customer=c2,
        assignee="Design Team B",
        priority=Priority.MEDIUM,
        deadline=datetime(2025, 5, 15),
        status=Status.IN_PROGRESS,
    )
    a3 = Assignment(
        title="Migrate DB schema",
        customer=c1,
        assignee="Dev Team A",
        priority=Priority.LOW,
        deadline=datetime(2026, 1, 1),
        status=Status.CLOSED,
    )
    board.add_assignment(a1)
    board.add_assignment(a2)
    board.add_assignment(a3)

    print("=== ServiceBoard Demo ===")
    for a in sorted(board.assignments, key=lambda x: x.priority.value):
        history = " | ".join(f"{h.action}({h.time})" for h in a.history)
        if history:
            print(f"[{a.status.name}] {a.title}")
            print(f"  Customer: {a.customer.name}, Assignee: {a.assignee}, Priority: {a.priority.name}")
            print(f"  Deadline: {a.deadline.date()}, History: {history}")
        else:
            print(f"[{a.status.name}] {a.title}")
            print(f"  Customer: {a.customer.name}, Assignee: {a.assignee}, Priority: {a.priority.name}")
            print(f"  Deadline: {a.deadline.date()}, History: (none)")
    print("Total customers:", len(board.customers))
    print("Total assignments:", len(board.assignments))
