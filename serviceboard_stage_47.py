# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ServiceBoard
def run_demo():
    board = ServiceBoard()
    board.add_customer("Alice", "alice@example.com")
    board.add_customer("Bob", "bob@example.com")
    
    alice = board.get_customer_by_name("Alice")
    bob = board.get_customer_by_name("Bob")
    
    req1 = board.create_request(alice, "Server down in Zone A", priority="high", deadline="2025-03-01")
    req2 = board.create_request(bob, "Slow response on API v2", priority="medium", deadline="2025-04-15")
    
    board.assign(req1, alice)
    board.assign(req2, bob)
    
    print(f"Total requests: {board.get_total_requests()}")
    print(f"Pending high-priority: {board.count_pending_by_priority('high')}")
    
    req3 = board.create_request(alice, "Network latency in Zone C", priority="critical", deadline="2025-02-28")
    board.assign(req3, alice)
    
    print(f"\nAll requests:")
    for r in board.get_all_requests():
        status_icon = "✅" if r.status == "resolved" else "⏳"
        print(f"{status_icon} [{r.id}] {r.title} - Customer: {r.customer_name}, Priority: {r.priority}, Deadline: {r.deadline}")

run_demo()
