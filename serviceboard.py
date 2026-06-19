# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ServiceBoard
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import random
from typing import List, Optional

@dataclass
class Customer:
    id: int
    name: str
    email: str

@dataclass
class Ticket:
    id: int
    customer_id: int
    title: str
    priority: int  # 1=Low, 2=Medium, 3=High
    deadline: datetime
    status: str = "Open"
    assigned_to: Optional[int] = None
    resolution_history: List[str] = field(default_factory=list)

class ServiceBoard:
    def __init__(self):
        self.customers: dict[int, Customer] = {}
        self.tickets: dict[int, Ticket] = {}
        self.next_customer_id = 1
        self.next_ticket_id = 1
        
    def add_demo_data(self):
        # Create customers
        for i in range(5):
            cust = Customer(id=self.next_customer_id, 
                           name=f"Client {self.next_customer_id}", 
                           email=f"user{i}@example.com")
            self.customers[self.next_customer_id] = cust
            self.next_customer_id += 1
            
        # Create tickets with varied priorities and deadlines
        today = datetime.now()
        for i in range(10):
            priority = random.choice([1, 2, 3])
            days_until_deadline = random.randint(1, 30)
            deadline = today + timedelta(days=days_until_deadline)
            
            ticket = Ticket(id=self.next_ticket_id,
                           customer_id=random.choice(list(self.customers.keys())),
                           title=f"Request #{self.next_ticket_id}",
                           priority=priority,
                           deadline=deadline)
                           
            # Assign to a random customer if possible
            if self.customers:
                ticket.assigned_to = random.choice(list(self.customers.keys()))
                
            self.tickets[self.next_ticket_id] = ticket
            self.next_ticket_id += 1
            
        return len(self.customers), len(self.tickets)
