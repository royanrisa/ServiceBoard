# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ServiceBoard
import unittest
from service_board.models import ServiceBoard, Customer, Assignment


class TestServiceBoardEdgeCases(unittest.TestCase):

    def setUp(self):
        self.board = ServiceBoard()

    def test_update_nonexistent_task_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.board.update("T-001", {"status": "resolved"})

    def test_delete_nonexistent_task_raises_key_error(self):
        with self.assertRaises(KeyError):
            del self.board["T-999"]

    def test_update_removes_old_assignment(self):
        customer = Customer(name="Alice")
        assignment = Assignment(task_id="T-001", assignee=customer, status="open")
        self.board.add_customer(customer)
        self.board.add_task("T-001", "Fix login bug")
        self.board.assign("T-001", customer)

        new_assignment = Assignment(task_id="T-001", assignee=customer, status="in_progress")
        self.board.update("T-001", {"assignee": new_assignment})

        task = self.board.get_task("T-001")
        self.assertEqual(task["assignee"].status, "in_progress")

    def test_delete_preserves_other_tasks(self):
        customer = Customer(name="Bob")
        assignment = Assignment(task_id="T-002", assignee=customer, status="open")
        self.board.add_customer(customer)
        self.board.add_task("T-001", "Task one")
        self.board.add_task("T-002", "Task two")

        del self.board["T-001"]

        with self.assertRaises(KeyError):
            _ = self.board.get_task("T-001")
        task_two = self.board.get_task("T-002")
        self.assertEqual(task_two["title"], "Task two")

    def test_overwrite_assignment_status_via_update(self):
        customer = Customer(name="Charlie")
        assignment = Assignment(task_id="T-003", assignee=customer, status="open")
        self.board.add_customer(customer)
        self.board.add_task("T-003", "Urgent fix")

        new_assignment = Assignment(task_id="T-003", assignee=customer, status="resolved")
        result = self.board.update("T-003", {"assignee": new_assignment})
        task = self.board.get_task("T-003")
        self.assertEqual(task["assignee"].status, "resolved")


if __name__ == "__main__":
    unittest.main()
