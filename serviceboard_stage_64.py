# === Stage 64: Add validation for relationship references ===
# Project: ServiceBoard
def validate_references(self):
    """Check that FK references exist in their target collections."""
    errors = []
    
    for customer in self.customers:
        if customer.id and customer.id not in [c.id for c in self.customers]:
            errors.append(f"Customer {customer.id} referenced by assignment does not exist")
    
    for assignment in self.assignments:
        if assignment.customer_id:
            cid = assignment.customer_id
            if cid not in [c.id for c in self.customers]:
                errors.append(f"Assignment customer_id {cid} references non-existent customer")
        
        if assignment.assigned_to and assignment.assigned_to not in [a.assigned_to for a in self.assignments]:
            errors.append(f"Assignment assigned_to {assignment.assigned_to} does not exist")
    
    return len(errors) == 0, errors
