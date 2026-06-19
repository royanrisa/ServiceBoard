# === Stage 4: Implement create operations for the primary records ===
# Project: ServiceBoard
class ServiceBoard:
    def __init__(self):
        self._customers = {}
        self._assignments = []
    
    def create_customer(self, name, email):
        if name in self._customers:
            raise ValueError(f"Customer {name} already exists")
        self._customers[name] = {"email": email, "created_at": datetime.now()}
        return self._customers[name]

    def assign_task(self, customer_name, task_id, priority="medium", deadline=None):
        if customer_name not in self._customers:
            raise ValueError(f"Customer {customer_name} does not exist")
        assignment = {"id": len(self._assignments) + 1, "customer": customer_name, "task_id": task_id, "priority": priority, "deadline": deadline, "status": "open", "history": []}
        self._assignments.append(assignment)
        return assignment

    def resolve_task(self, assignment_id):
        for i, a in enumerate(self._assignments):
            if a["id"] == assignment_id:
                a["status"] = "resolved"
                a["history"].append({"action": "resolved", "timestamp": datetime.now()})
                return True
        raise ValueError(f"Assignment {assignment_id} not found")
