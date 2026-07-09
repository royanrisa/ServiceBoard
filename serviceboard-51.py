# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ServiceBoard
import unittest


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        from service_board import ServiceBoard
        self.board = ServiceBoard()
        for data in [
            {"customer": "Alice", "priority": 1, "status": "open"},
            {"customer": "Bob", "priority": 2, "status": "assigned"},
            {"customer": "Charlie", "priority": 3, "status": "closed"},
        ]:
            self.board.add_request(data)

    def test_search_by_customer(self):
        results = self.board.search("Alice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer"], "Alice")

    def test_filter_by_priority(self):
        results = self.board.filter(priority=2)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer"], "Bob")

    def test_filter_by_status(self):
        results = self.board.filter(status="closed")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer"], "Charlie")

    def test_combined_search_and_filter(self):
        results = self.board.search("Bob").filter(priority=2)
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
