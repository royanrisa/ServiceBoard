# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ServiceBoard
def delete_request(request_id, confirm=False):
    if request_id in requests:
        req = requests[request_id]
        if confirm and input(f"Удалить заявку {req['id']} ({req['customer']})? (y/n): ").lower() != 'y':
            return False
        del requests[request_id]
        print(f"Заявка {request_id} удалена.")
        return True
    else:
        print(f"Заявка {request_id} не найдена.")
        return False
