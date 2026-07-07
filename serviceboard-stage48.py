# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ServiceBoard
import unittest
from datetime import date, timedelta
from enum import Enum


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def validate(self) -> bool:
        return "@" in self.email and len(self.name.strip()) > 0


class Assignment:
    def __init__(self, customer: Customer, priority: Priority, deadline: date):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(priority, Priority):
            raise TypeError("priority must be a Priority enum value")
        if isinstance(deadline, str):
            deadline = date.fromisoformat(deadline)
        self.customer = customer
        self.priority = priority
        self.deadline = deadline

    def is_overdue(self) -> bool:
        return date.today() > self.deadline


class ServiceBoard(unittest.TestCase):
    def test_customer_validation_valid(self):
        c = Customer("Alice", "alice@example.com")
        self.assertTrue(c.validate())

    def test_customer_validation_invalid_email(self):
        c = Customer("Bob", "bad-email")
        self.assertFalse(c.validate())

    def test_assignment_creation_with_enum(self):
        c = Customer("Charlie", "charlie@test.com")
        a = Assignment(c, Priority.HIGH, date.today() + timedelta(days=3))
        self.assertEqual(a.priority, Priority.HIGH)

    def test_assignment_creation_with_string_deadline(self):
        c = Customer("Diana", "diana@demo.org")
        a = Assignment(c, Priority.LOW, "2099-12-31")
        self.assertIsInstance(a.deadline, date)


if __name__ == "__main__":
    unittest.main()
