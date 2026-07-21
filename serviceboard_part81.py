# === Stage 81: Add final README text as a module string with usage examples ===
# Project: ServiceBoard
def usage_example():
    """Demonstrates ServiceBoard in action."""
    from service_board import Customer, Task, Board

    board = Board()
    alice = Customer("Alice", "alice@example.com")
    bob = Customer("Bob", "bob@example.com")
    board.add_customers([alice, bob])

    t1 = Task(
        title="Fix login bug",
        customer=alice,
        assignee=bob,
        priority="high",
        deadline="2025-12-31",
        status="open",
    )
    board.add_task(t1)

    t2 = Task(
        title="Onboard new team member",
        customer=alice,
        assignee=None,
        priority="medium",
        deadline="2026-01-15",
        status="open",
    )
    board.add_task(t2)

    print(f"Total tasks: {board.get_total_tasks()}")
    high = [t for t in board.tasks if t.priority == "high"]
    print(f"High priority tasks: {[t.title for t in high]}")
    open_ = [t for t in board.tasks if t.status == "open"]
    print(f"Open tasks: {len(open_)}")
