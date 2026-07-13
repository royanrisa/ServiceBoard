# === Stage 61: Add performance timing for core list and search operations ===
# Project: ServiceBoard
import time


def benchmark_service_board():
    """Performance timing for core list and search operations."""
    start = time.perf_counter()
    board = load_service_board()
    elapsed = time.perf_counter() - start
    print(f"Loaded {len(board)} service requests in {elapsed:.6f}s")

    # List all records by priority order
    sorted_requests = sort_by_priority(board)
    list_start = time.perf_counter()
    _ = [r for r in sorted_requests if r["status"] == "open"]
    list_elapsed = time.perf_counter() - list_start
    print(f"Filtered open requests (list): {list_elapsed:.6f}s")

    # Search by customer name
    search_start = time.perf_counter()
    results_customer = [r for r in board if r["customer"] == "John Doe"]
    search_elapsed = time.perf_counter() - search_start
    print(f"Search by customer 'John Doe': {search_elapsed:.6f}s, found {len(results_customer)}")

    # Search by priority and deadline range
    search_advanced_start = time.perf_counter()
    urgent_open = [r for r in board if r["priority"] == "high" and r["deadline"] < datetime.now().date()]
    search_advanced_elapsed = time.perf_counter() - search_advanced_start
    print(f"Advanced search (urgent+overdue): {search_advanced_elapsed:.6f}s, found {len(urgent_open)}")

    # Resolution history aggregation
    hist_start = time.perf_counter()
    resolution_counts = {}
    for r in board:
        status = r["status"]
        resolution_counts[status] = resolution_counts.get(status, 0) + 1
    hist_elapsed = time.perf_counter() - hist_start
    print(f"Resolution history aggregation: {hist_elapsed:.6f}s")

    # Average assignment duration for open items
    avg_start = time.perf_counter()
    if sorted_requests:
        durations = [r["assignment_duration_days"] for r in sorted_requests]
        avg_dur = sum(durations) / len(durations)
    else:
        avg_dur = 0.0
    avg_elapsed = time.perf_counter() - avg_start
    print(f"Average assignment duration (open): {avg_dur:.2f} days, computed in {avg_elapsed:.6f}s")

    # Memory usage snapshot
    import sys
    mem_before = sys.getsizeof(board)
    sorted_mem = sys.getsizeof(sorted_requests)
    search_results_mem = sys.getsizeof(results_customer)
    print(f"Memory: board={mem_before:,} bytes, sorted={sorted_mem:,}, filtered={search_results_mem:,}")


if __name__ == "__main__":
    benchmark_service_board()
