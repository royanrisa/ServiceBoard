# === Stage 83: Add regression tests for the final demo workflow ===
# Project: ServiceBoard
import pytest
from service_board import Customer, ServiceRequest, Priority


def test_demo_workflow_regression():
    c1 = Customer("Alice", "alice@example.com")
    c2 = Customer("Bob", "bob@example.com")
    s1 = ServiceRequest(
        title="Slow login",
        customer=c1,
        priority=Priority.HIGH,
        deadline="2026-03-15 18:00",
        assignee="Dev Team",
        status="open",
    )
    s1.add_resolution("Root cause: legacy session cache")
    assert s1.status == "open"
    assert len(s1.resolutions) == 1
    assert c2.name not in [r["assignee"] for r in s1.resolutions]

    c3 = Customer("Carol", "carol@example.com")
    s2 = ServiceRequest(
        title="Printer jam",
        customer=c3,
        priority=Priority.MEDIUM,
        deadline="2026-04-01 10:00",
        assignee="Facilities",
        status="resolved",
    )
    s2.add_resolution("Replaced drum unit")
    assert s2.status == "resolved"

    board = [s1, s2]
    high_count = sum(1 for s in board if s.priority == Priority.HIGH)
    assert high_count == 1


if __name__ == "__main__":
    test_demo_workflow_regression()
