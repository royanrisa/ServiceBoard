# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ServiceBoard
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional, List

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class Customer:
    id: int
    name: str
    email: str

@dataclass
class AssignmentStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"

@dataclass
class ResolutionHistoryItem:
    timestamp: date
    status: AssignmentStatus
    notes: Optional[str] = None

@dataclass
class ServiceRequest:
    id: int
    customer_id: int
    title: str
    description: str
    priority: Priority
    deadline: date
    assigned_to: Optional[int] = None  # Customer ID or internal user ID placeholder
    status: AssignmentStatus = AssignmentStatus.PENDING
    resolution_history: List[ResolutionHistoryItem] = field(default_factory=list)

@dataclass
class ServiceBoardState:
    requests: List[ServiceRequest] = field(default_factory=list)
    next_request_id: int = 1
