import json
import csv  
import os 
import uuid
from decimal import Decimal, InvalidOperation
from datetime import datetime

class manageData:
    def __init__(self,folder = "Data",users_file = 'data.json',transaciton_file = "transactions.csv"):
        """Initialize storage paths and ensure data files/folders exist.

        Args:
            folder (str): Data folder path.
            users_file (str): Users filename inside data folder.
            transaciton_file (str): Transactions filename inside data folder.
        """
        self.data_folder = folder
        self.users_file = os.path.join(folder,users_file)
        self.transaction_file = os.path.join(folder,transaciton_file)
        self.ensure_folder_exsists()
        self.ensure_user_file()


    def ensure_folder_exsists(self):
        """Create the data folder if it does not exist. Logs OSError on failure."""
        try:
            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)
            else:
                print(f"{self.data_folder} Created sucessfully")
        except OSError as e:
            print(f"Error creating data folder '{self.data_folder}': {e}")


    def ensure_user_file(self):
        """Create users JSON and transactions CSV files if they do not exist."""
        try:
            if not os.path.exists(self.users_file):
                with open(self.users_file,"w") as f:
                    json.dump([],f,sort_keys=True)
                print("user file created")
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error creating users file '{self.users_file}': {e}")

        try:
            if not os.path.exists(self.transaction_file):
                with open(self.transaction_file,"w",newline="")as f:
                    writer = csv.writer(f)
                    writer.writerow(["transaction_id","user_id", "type", "amount", "category", "date", "description","payment_method"])
                print("Transcation file created")
        except OSError as e:
            print(f"Error creating transactions file '{self.transaction_file}': {e}")


    def load_users(self):
        """Load and return the list of users from the users JSON file.
        
        Returns:
            list: list of user dicts, or [] on error.
        """
        try:
            with open(self.users_file,"r") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading users from '{self.users_file}': {e}")
            return []

    def add_users(self,users_list):
        """Overwrite the users file with the provided users_list.

        Args:
            users_list (list): List of user dictionaries to save.
        """
        try:
            with open(self.users_file,"w") as f:
                json.dump(users_list,f,indent=4)
        except OSError as e:
            print(f"Error writing users to '{self.users_file}': {e}")

    def load_transactions(self):
        """Load transactions from the CSV file and return as list of dicts.

        Returns:
            list: list of transaction dicts, or [] on error.
        """
        try:
            with open(self.transaction_file, "r") as f:
                reader = csv.DictReader(f)
                transactions = []
                for row in reader:
                    # Convert amount from string to float
                    try:
                        row['amount'] = float(row['amount'])
                    except (ValueError, TypeError):
                        print(f"Warning: Invalid amount in transaction {row.get('transaction_id')}")
                        continue
                    transactions.append(row)
                return transactions
        except OSError as e:
            print(f"Error reading transactions from '{self.transaction_file}': {e}")
            return []
        except csv.Error as e:
            print(f"CSV parsing error in '{self.transaction_file}': {e}")
            return []
        

    def add_transactions(self,transactions):
        """Write the list of transaction dicts to the CSV file.

        Args:
            transactions (list): List of transaction dictionaries to write.
        """
        try:
            with open(self.transaction_file,"w",newline="") as f:
                fieldnames = ["transaction_id","user_id", "type", "amount", "category", "date", "description","payment_method"]
                writer = csv.DictWriter(f,fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(transactions)
        except OSError as e:
            print(f"Error writing transactions to '{self.transaction_file}': {e}")
        except csv.Error as e:
            print(f"CSV writing error to '{self.transaction_file}': {e}")

    def import_transactions_from_csv(self, src_path, skip_invalid=True, assign_user_id=None):
        """Import transactions from an external CSV file and merge into storage.

        Args:
            src_path (str): Path to the source CSV file.
            skip_invalid (bool): If True, skip invalid rows instead of aborting.
            assign_user_id (str|None): If provided, override each imported row's user_id with this value.

        Returns:
            dict: { "imported": int, "skipped": int, "errors": [str, ...] }
        """
        required_cols = {"user_id", "type", "amount", "category", "date", "description", "payment_method"}
        imported = 0
        skipped = 0
        errors = []

        if not os.path.isfile(src_path):
            errors.append(f"Source file not found: {src_path}")
            return {"imported": 0, "skipped": 0, "errors": errors}

        try:
            with open(src_path, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if not required_cols.issubset(set(reader.fieldnames or [])):
                    errors.append("Source CSV missing required columns.")
                    return {"imported": 0, "skipped": 0, "errors": errors}

                current = self.load_transactions() or []
                existing_ids = {t.get("transaction_id") for t in current}

                for i, row in enumerate(reader, start=1):
                    try:
                        # Basic validation
                        if row.get("type") not in ("income", "expense"):
                            raise ValueError("invalid type")
                        # Normalize/validate amount
                        amt = Decimal(str(row.get("amount", "")).strip())
                        amount_val = float(amt)
                        # Use assign_user_id if provided, otherwise use CSV value
                        user_id_val = assign_user_id if assign_user_id else row.get("user_id")
                        if not user_id_val:
                            raise KeyError("missing user_id")
                        # Ensure date present
                        if not row.get("date"):
                            row["date"] = datetime.now().strftime("%Y-%m-%d")
                        # Ensure transaction_id exists and is unique
                        tid = row.get("transaction_id") or f"IMP-{str(uuid.uuid4())[:8].upper()}"
                        if tid in existing_ids:
                            # generate new id to avoid collision
                            tid = f"IMP-{str(uuid.uuid4())[:8].upper()}"
                        existing_ids.add(tid)
                        # Append cleaned row
                        current.append({
                            "transaction_id": tid,
                            "user_id": user_id_val,
                            "type": row["type"],
                            "amount": amount_val,
                            "category": row.get("category", ""),
                            "date": row["date"],
                            "description": row.get("description", ""),
                            "payment_method": row.get("payment_method", "")
                        })
                        imported += 1
                    except (InvalidOperation, ValueError, KeyError) as ve:
                        skipped += 1
                        msg = f"Row {i}: {ve}"
                        errors.append(msg)
                        if not skip_invalid:
                            return {"imported": imported, "skipped": skipped, "errors": errors}
        except (OSError, csv.Error) as e:
            errors.append(str(e))
            return {"imported": imported, "skipped": skipped, "errors": errors}

        # Persist merged transactions
        try:
            self.add_transactions(current)
        except Exception as e:
            errors.append(f"Failed writing merged transactions: {e}")
            return {"imported": imported, "skipped": skipped, "errors": errors}

        return {"imported": imported, "skipped": skipped, "errors": errors}

    def export_transactions_to_csv(self, dest_path, filter_user_id=None):
        """Export stored transactions to a CSV file.

        Args:
            dest_path (str): Destination path for the CSV file to create/overwrite.
            filter_user_id (str|None): If provided, only export transactions for this user.

        Returns:
            dict: { "exported": int, "error": str|None }
        """
        try:
            txns = self.load_transactions() or []
            if filter_user_id:
                txns = [t for t in txns if t.get("user_id") == filter_user_id]

            fieldnames = ["transaction_id","user_id", "type", "amount", "category", "date", "description","payment_method"]
            # Ensure destination folder exists
            dest_dir = os.path.dirname(dest_path) or "."
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir, exist_ok=True)

            with open(dest_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(txns)

            return {"exported": len(txns), "error": None}
        except (OSError, csv.Error) as e:
            return {"exported": 0, "error": str(e)}
