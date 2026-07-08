# === Stage 50: Add unit tests for import and export behavior ===
# Project: ServiceBoard
import unittest
from service_board import ServiceBoard, Customer, Assignment, Priority

class TestServiceBoard(unittest.TestCase):
    def setUp(self):
        self.board = ServiceBoard()

    def test_import_customers(self):
        c1 = Customer(name="Alice", email="alice@example.com")
        c2 = Customer(name="Bob", email="bob@example.com")
        self.board.import_customers([c1, c2])
        self.assertEqual(len(self.board.customers), 2)
        self.assertIn("Alice", [c.name for c in self.board.customers])

    def test_import_assignments(self):
        cust = Customer(name="Charlie", email="charlie@example.com")
        self.board.add_customer(cust)
        a1 = Assignment(customer=cust, engineer="Engineer X", priority=Priority.HIGH, deadline="2024-12-31")
        self.board.import_assignments([a1])
        self.assertEqual(len(self.board.assignments), 1)

    def test_import_priorities(self):
        prios = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}
        imported = {p: i for i, p in enumerate(prios.items(), 1)}
        self.assertEqual(imported["LOW"], 1)

    def test_export_assignments(self):
        c = Customer(name="Dave", email="dave@example.com")
        self.board.add_customer(c)
        a = Assignment(customer=c, engineer="Engineer Y", priority=Priority.MEDIUM, deadline="2024-06-30")
        self.board.import_assignments([a])
        exported = self.board.export_assignments()
        self.assertIn("Dave", str(exported))

    def test_export_customers(self):
        c = Customer(name="Eve", email="eve@example.com")
        self.board.add_customer(c)
        exported = self.board.export_customers()
        self.assertIn("Eve", str(exported))
