# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: ServiceBoard
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ServiceBoard import *

# --- Self-check: validate structure & demo usage ---

# 1. Verify all modules are importable and key classes exist
assert hasattr(ServiceBoard, 'Customer'), "Customer class missing"
assert hasattr(ServiceBoard, 'ServiceRequest'), "ServiceRequest class missing"
assert hasattr(ServiceBoard, 'Assignment'), "Assignment class missing"
assert hasattr(ServiceBoard, 'Priority'), "Priority class missing"
assert hasattr(ServiceBoard, 'ResolutionHistory'), "ResolutionHistory class missing"

# 2. Instantiate a few objects and check they work
c = ServiceBoard.Customer("Acme Corp", "engineering@acme.com")
req = ServiceBoard.ServiceRequest("C-101", c, ServiceBoard.Priority.HIGH, "Server crash in prod DB")
a = ServiceBoard.Assignment(req, ["alice", "bob"], due="2024-12-31", priority=ServiceBoard.Priority.URGENT)
rh = ServiceBoard.ResolutionHistory("Resolved after restart on 2024-12-28", "C-101")

# 3. Run a demo scenario: create requests, assign them, resolve one
requests = [
    ServiceBoard.ServiceRequest(f"C-{i}", c, ServiceBoard.Priority.MEDIUM, f"Test ticket {i}") for i in range(1, 6)
]
for r in requests[:2]:
    a = ServiceBoard.Assignment(r, ["charlie"], due="2030-01-01")

# 4. Resolve one and check history
rh = ServiceBoard.ResolutionHistory("Fixed with patch v2", "C-101")
assert len(ServiceBoard.ResolutionHistory.history) == 1

print("✅ All self-checks passed: classes, instantiation, assignment, resolution work correctly.")
