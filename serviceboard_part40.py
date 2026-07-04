# === Stage 40: Add plain text report export ===
# Project: ServiceBoard
def export_report(self, filename="report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for req in self.requests.values():
            f.write(f"ID:{req.id} | Cust:{req.customer_name} | Assignee:{req.assignee}\n")
            f.write(f"  Priority:{req.priority} | Deadline:{req.deadline}\n")
            if req.history:
                for event in req.history:
                    f.write(f"  - {event['timestamp']}: {event['status']} by {event.get('user', 'system')}\n")
