# === Stage 56: Add compact error classes for domain failures ===
# Project: ServiceBoard
class ServiceError(Exception):
    """Base for all service-domain errors."""


class CustomerNotFound(ServiceError):
    def __init__(self, customer_id: str) -> None:
        super().__init__(f"Customer with id '{customer_id}' not found.")
        self.customer_id = customer_id


class AssignmentConflict(ServiceError):
    def __init__(self, request_id: str, assignee: str) -> None:
        super().__init__(
            f"Request {request_id} is already assigned to {assignee!r}."
        )
        self.request_id = request_id
        self.assignee = assignee


class DeadlineExceeded(ServiceError):
    def __init__(self, deadline: datetime) -> None:
        super().__init__(f"Deadline was exceeded at {deadline}.")
        self.deadline = deadline


class ResolutionHistoryOverflow(ServiceError):
    def __init__(self, max_entries: int) -> None:
        super().__init__(
            f"Resolution history exceeds the limit of {max_entries} entries."
        )
        self.max_entries = max_entries


class InvalidPriority(ServiceError):
    def __init__(self, priority: str) -> None:
        super().__init__(f"Invalid priority value: {priority!r}.")
        self.priority = priority
