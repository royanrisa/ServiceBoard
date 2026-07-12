# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ServiceBoard
def bulk_delete(request, service_board):
    """Delete multiple services only when confirmation is enabled."""
    if request.method == "POST" and request.is_form():
        confirm = request.get("confirm_bulk_delete", "").lower()
        if confirm != "yes":
            return _render_alert(service_board, "Please confirm bulk deletion.", alert_type="danger")

        selected_ids = [int(id) for id in request.get_list("service_id")]
        if not selected_ids:
            return _render_alert(service_board, "Select services to delete first.", alert_type="warning")

        deleted_count = 0
        remaining = []
        for service in service_board.services:
            if int(service.id) in selected_ids:
                service.resolve(comment=f"Bulk-deleted on {datetime.now():%Y-%m-%d %H:%M}")
                deleted_count += 1
            else:
                remaining.append(service)

        service_board.services = remaining
        return _render_alert(
            service_board,
            f"Deleted {deleted_count} service(s).",
            alert_type="success",
            extra=f"All {len(service_board.services)} services remain.",
        )

    # GET: show confirmation summary
    selected_ids = [int(id) for id in request.get_list("service_id")]
    if not selected_ids:
        return _render_alert(
            service_board,
            "Select services to delete. Use the checkbox column or bulk-select toolbar.",
            alert_type="info",
        )

    count = sum(1 for s in service_board.services if int(s.id) in selected_ids)
    pending = [s for s in service_board.services if int(s.id) in selected_ids]
    return _render_alert(
        service_board,
        f"About to delete {count} service(s): {[s.title for s in pending]}",
        alert_type="warning",
        extra="Click 'Confirm Deletion' above or use the toolbar button.",
    )
