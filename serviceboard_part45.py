# === Stage 45: Add restore from backup with validation ===
# Project: ServiceBoard
def restore_backup(self, path: str) -> bool:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Backup file not found: {path}")
        with open(path, "r") as f:
            raw = json.load(f)
        required_keys = {"customers", "assignments"}
        if not all(k in raw for k in required_keys):
            print("Warning: backup missing expected keys; partial restore may fail.")
        self.customers.clear()
        for cid, info in raw.get("customers", {}).items():
            try:
                self.add_customer(cid, **info)
            except Exception as e:
                print(f"Failed to restore customer {cid}: {e}")
        valid_assignees = set(self.customer_ids())
        assignments = raw.get("assignments", [])
        restored = 0
        for a in assignments:
            try:
                cust_id = a["customer"]
                if cust_id not in valid_assignees:
                    print(f"Skipping assignment {a['id']}: customer {cust_id} missing.")
                    continue
                self.add_assignment(cust_id, **{k: v for k, v in a.items() if k != "customer"})
                restored += 1
            except Exception as e:
                print(f"Failed to restore assignment {a.get('id', '?')}: {e}")
        return restored > 0 or len(self.customers) == 0
