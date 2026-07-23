# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: ServiceBoard
def _remove_duplicate_services(self):
    """Remove duplicate entries from self.services."""
    seen = set()
    cleaned = []
    for entry in list(self.services.values()):
        key = (entry.customer_name, entry.service_type)
        if key not in seen:
            seen.add(key)
            cleaned.append(entry)
    self.services.clear()
    for entry in cleaned:
        self.services[entry.id] = entry

def _validate_entry(self):
    """Validate a new service entry."""
    errors = []
    if not entry.customer_name or len(entry.customer_name.strip()) < 2:
        errors.append("Customer name must be at least 2 characters.")
    if not entry.service_type or len(entry.service_type.strip()) < 3:
        errors.append("Service type must be at least 3 characters.")
    if entry.deadline and (entry.deadline - datetime.now()).total_seconds() <= 0:
        errors.append("Deadline has already passed.")
    return errors

def _format_history_entry(self, event):
    """Format a history entry for display."""
    return f"[{event.timestamp.strftime('%Y-%m-%d %H:%M')}] {event.action} by {event.user_name}" if hasattr(event, 'timestamp') else str(event)

def _get_services_by_priority(self, priority):
    """Return services sorted by the given priority level."""
    return [entry for entry in self.services.values() if entry.priority == priority]

def _get_services_by_customer(self, customer_name):
    """Return all services for a specific customer."""
    return [entry for entry in self.services.values() if entry.customer_name.lower() == customer_name.lower()]

def _calculate_resolution_rate(self):
    """Calculate the resolution rate of completed services."""
    total = len([e for e in self.services.values() if e.status == "completed"])
    resolved = len([e for e in self.services.values() if e.status == "resolved"])
    return (resolved / total * 100) if total > 0 else 0

def _export_services_to_csv(self, filename):
    """Export services to a CSV file."""
    import csv
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for entry in self.services.values():
            writer.writerow([entry.id, entry.customer_name, entry.service_type, entry.priority, entry.deadline, entry.status])

def _clear_all_services(self):
    """Remove all services and reset the board."""
    self.services.clear()
    self.history = []
