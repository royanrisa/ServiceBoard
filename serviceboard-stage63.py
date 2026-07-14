# === Stage 63: Add relationships between records where useful ===
# Project: ServiceBoard
import sqlite3

conn = sqlite3.connect("service_board.db")
c = conn.cursor()

# Add relationships between records where useful: customers, assignments, priorities, deadlines, and resolution history.
customers = [
    ("Acme Corp", "engineering"),
    ("Globex Industries", "operations"),
    ("Initech", "finance"),
    ("Umbrella Corp", "research"),
]

assignments = [
    ("ticket-101", "customer-acme", "engineer-zoe"),
    ("ticket-102", "customer-globex", "engineer-mike"),
    ("ticket-103", "customer-initech", "engineer-zoe"),
]

priorities = [
    ("ticket-101", "high"),
    ("ticket-102", "medium"),
    ("ticket-103", "low"),
]

deadlines = [
    ("ticket-101", 60),
    ("ticket-102", 45),
    ("ticket-103", 90),
]

resolution_history = [
    ("ticket-101", "resolved"),
    ("ticket-102", "in-progress"),
    ("ticket-103", "pending"),
]

c.executemany("INSERT INTO customers (name, dept) VALUES (?, ?)", customers)
c.executemany("INSERT INTO assignments (id, customer_id, engineer_id) VALUES (?, ?, ?)", assignments)
c.executemany("INSERT INTO priorities (ticket_id, level) VALUES (?, ?)", priorities)
c.executemany("INSERT INTO deadlines (ticket_id, deadline_days) VALUES (?, ?)", deadlines)
c.executemany("INSERT INTO resolution_history (ticket_id, status) VALUES (?, ?)", resolution_history)

conn.commit()
