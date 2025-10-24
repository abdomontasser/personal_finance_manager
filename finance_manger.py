from User import User
from Transaction import Transaction
from users_data import manageData
<<<<<<< HEAD
from decimal import Decimal, InvalidOperation

class FinanceManager:
    """Main logic handler that connects users, transactions, and storage."""

    def __init__(self):
        """Create a FinanceManager instance and load stored users and transactions."""
=======

class FinanceManager:
    """Main logic handler that connects users, transactions, and storage"""

    def __init__(self):
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        self.data_manager = manageData()
        self.users = self.data_manager.load_users()
        self.transactions = self.data_manager.load_transactions()

    # ----- USERS -----
    def register_user(self, name, password, currency="USD"):
<<<<<<< HEAD
        """Register a new user after validating required fields.

        Args:
            name (str): Username.
            password (str): Password string.
            currency (str): Currency code.
        """
        if not name or not password:
            print("❌ Name and password are required.")
            return
        user = User(name, password, currency)
        self.users.append(user.to_dict())
        try:
            self.data_manager.add_users(self.users)
            print(f"✅ User '{name}' registered successfully!")
        except Exception as e:
            print(f"Error saving user: {e}")

    def login(self, name, password):
        """Validate credentials and return the user dict on success.

        Args:
            name (str): Username.
            password (str): Password.

        Returns:
            dict|None: user dict if authenticated, else None.
        """
        for user in self.users:
            if user.get("name") == name and user.get("password") == password:
=======
        user = User(name, password, currency)
        self.users.append(user.to_dict())
        self.data_manager.add_users(self.users)
        print(f"✅ User '{name}' registered successfully!")

    def login(self, name, password):
        for user in self.users:
            if user["name"] == name and user["password"] == password:
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
                print(f"👋 Welcome back, {name}!")
                return user
        print("❌ Invalid username or password.")
        return None

    # Add transaction
<<<<<<< HEAD
    def add_transaction(self, user_id, t_type, amount, category, description, payment_method, date):
        """Validate and add a transaction for a user, persisting to storage.

        Args:
            user_id (str): ID of the user creating the transaction.
            t_type (str): 'income' or 'expense'.
            amount (str|float|Decimal): Transaction amount.
            category (str): Transaction category.
            description (str): Description text.
            payment_method (str): Payment method string.
            date (str): Date string YYYY-MM-DD.
        """
        if t_type not in ("income", "expense"):
            print("❌ Transaction type must be 'income' or 'expense'.")
            return
        try:
            # validate amount
            amt = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            print("❌ Invalid amount. Please enter a numeric value.")
            return

        try:
            txn = Transaction(user_id, t_type, amt, category, description, payment_method, date)
            self.transactions.append(txn.to_dict())
            self.data_manager.add_transactions(self.transactions)
            print("💾 Transaction added successfully!")
        except Exception as e:
            print(f"Error adding transaction: {e}")

    # View Transaction 
    def view_transactions(self, user_id):
        """Print all transactions for the specified user_id.

        Args:
            user_id (str): User identifier to filter transactions.
        """
        txns = [t for t in self.transactions if t.get("user_id") == user_id]
=======
    def add_transaction(self, user_id, t_type, amount, category, description,payment_method,date):
        txn = Transaction(user_id, t_type, amount, category, description,payment_method,date)
        self.transactions.append(txn.to_dict())
        self.data_manager.add_transactions(self.transactions)
        print("💾 Transaction added successfully!")

    # View Transaction 
    def view_transactions(self, user_id):
        txns = [t for t in self.transactions if t["user_id"] == user_id]
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        if not txns:
            print("⚠️ No transactions found.")
            return
        for t in txns:
            print(f"[{t['date']}] {t['category']} - {t['amount']} ({t['type']})")

    def get_user_transactions(self, user_id):
<<<<<<< HEAD
        """Return a list of transaction dicts for the given user_id.

        Args:
            user_id (str): User identifier.

        Returns:
            list: transactions for the user.
        """
        return [t for t in self.transactions if t.get("user_id") == user_id]
=======
        return [t for t in self.transactions if t["user_id"] == user_id]
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
