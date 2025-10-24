from User import User
from Transaction import Transaction
from users_data import manageData

class FinanceManager:
    """Main logic handler that connects users, transactions, and storage"""

    def __init__(self):
        self.data_manager = manageData()
        self.users = self.data_manager.load_users()
        self.transactions = self.data_manager.load_transactions()

    # ----- USERS -----
    def register_user(self, name, password, currency="USD"):
        user = User(name, password, currency)
        self.users.append(user.to_dict())
        self.data_manager.add_users(self.users)
        print(f"✅ User '{name}' registered successfully!")

    def login(self, name, password):
        for user in self.users:
            if user["name"] == name and user["password"] == password:
                print(f"👋 Welcome back, {name}!")
                return user
        print("❌ Invalid username or password.")
        return None

    # Add transaction
    def add_transaction(self, user_id, t_type, amount, category, description,payment_method,date):
        txn = Transaction(user_id, t_type, amount, category, description,payment_method,date)
        self.transactions.append(txn.to_dict())
        self.data_manager.add_transactions(self.transactions)
        print("💾 Transaction added successfully!")

    # View Transaction 
    def view_transactions(self, user_id):
        txns = [t for t in self.transactions if t["user_id"] == user_id]
        if not txns:
            print("⚠️ No transactions found.")
            return
        for t in txns:
            print(f"[{t['date']}] {t['category']} - {t['amount']} ({t['type']})")

    def get_user_transactions(self, user_id):
        return [t for t in self.transactions if t["user_id"] == user_id]
