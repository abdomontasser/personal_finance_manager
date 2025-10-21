import os
import json
import csv
from modules.user import User
from modules.transaction import Transaction

class FinanceManager:
    def __init__(self, data_path="data/users.json", csv_path="data/transactions.csv"):
        self.data_path = data_path
        self.csv_path = csv_path
        self.users = []
        self.current_user = None
        self.load_data()

    def register_user(self, name, password, currency="USD"):
        user = User(name, password, currency)
        self.users.append(user)
        self.save_data()
        print(f"✅ User '{name}' registered successfully!")

    def login_user(self, name, password):
        for user in self.users:
            if user.name == name and user.verify_password(password):
                self.current_user = user
                print(f"👋 Welcome back, {name}!")
                return True
        print("❌ Invalid username or password.")
        return False

    def switch_user(self):
        self.current_user = None
        print("🔄 User switched. Please log in again.")

    def save_data(self):

        os.makedirs("data", exist_ok=True)


        with open(self.data_path, "w") as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4)


        with open(self.csv_path, "w", newline="") as f:
            fieldnames = ["transaction_id", "user_id", "type", "amount", "category", "date", "description", "payment_method"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users:
                for t in user.transactions:
                    writer.writerow(t.to_dict())

    def load_data(self):

        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                data = json.load(f)
                for u in data:
                    user = User(u["name"], u["password"], u["currency"])
                    user.user_id = u["user_id"]
                    for t in u["transactions"]:
                        tr = Transaction(
                            t["user_id"],
                            t["type"],
                            t["amount"],
                            t["category"],
                            t["description"],
                            t["payment_method"],
                            t["date"]
                        )
                        user.transactions.append(tr)
                    self.users.append(user)
