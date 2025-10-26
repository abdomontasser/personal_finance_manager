from User import User
from Transaction import Transaction
from users_data import manageData
from decimal import Decimal, InvalidOperation
import os
import uuid
from datetime import datetime

class FinanceManager:
    """Main logic handler that connects users, transactions, and storage."""

    def __init__(self):
        """Create a FinanceManager instance and load stored users and transactions."""
        self.data_manager = manageData()
        self.users = self.data_manager.load_users()
        self.transactions = self.data_manager.load_transactions()

    # ----- USERS -----
    def register_user(self, name, password, currency="USD"):
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
                print(f"👋 Welcome back, {name}!")
                return user
        print("❌ Invalid username or password.")
        return None

    # Add transaction
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
        if not txns:
            print("⚠️ No transactions found.")
            return
        
        print("\n=== Your Transactions ===")
        print("Date       | Type     | Category      | Amount  | Description")
        print("-" * 65)
        for t in txns:
            print(f"{t['date']} | {t['type']:<8} | {t['category']:<12} | {float(t['amount']):>7.2f} | {t['description']}")

    def get_user_transactions(self, user_id):
        """Return a list of transaction dicts for the given user_id.

        Args:
            user_id (str): User identifier.

        Returns:
            list: transactions for the user.
        """
        return [t for t in self.transactions if t.get("user_id") == user_id]

    def import_transactions(self, src_path, skip_invalid=True, assign_user_id=None):
        """Import transactions from an external CSV into the app store.

        Args:
            src_path (str): Path to the source CSV file.
            skip_invalid (bool): Skip invalid rows when True.
            assign_user_id (str|None): If provided, assign imported transactions to this user_id.

        Returns:
            dict: result from manageData.import_transactions_from_csv
        """
        if not src_path or not isinstance(src_path, str):
            print("❌ Invalid source path.")
            return {"imported": 0, "skipped": 0, "errors": ["invalid path"]}

        result = self.data_manager.import_transactions_from_csv(src_path, skip_invalid=skip_invalid, assign_user_id=assign_user_id)
        # reload local cache
        self.transactions = self.data_manager.load_transactions()
        if result.get("imported"):
            print(f"✅ Imported {result['imported']} transactions.")
        if result.get("skipped"):
            print(f"⚠️ Skipped {result['skipped']} rows.")
        for e in result.get("errors", [])[:5]:
            print(f"• {e}")
        return result

    def export_transactions(self, dest_path, user_id=None):
        """Export transactions to CSV; optionally filter by user_id.

        Args:
            dest_path (str): Destination CSV filepath.
            user_id (str|None): If provided, only export that user's transactions.

        Returns:
            dict: result from manageData.export_transactions_to_csv
        """
        if not dest_path or not isinstance(dest_path, str):
            print("❌ Invalid destination path.")
            return {"exported": 0, "error": "invalid path"}

        result = self.data_manager.export_transactions_to_csv(dest_path, filter_user_id=user_id)
        if result.get("error"):
            print(f"❌ Export failed: {result['error']}")
        else:
            print(f"✅ Exported {result['exported']} transactions to {dest_path}")
        return result

    # ----- SAVINGS GOALS -----
    def add_savings_goal(self, user_id, goal_name, target_amount, due_date=None):
        """Create and persist a savings goal for a user.

        Args:
            user_id (str): target user id.
            goal_name (str): human name for the goal.
            target_amount (str|float|Decimal): numeric target value.
            due_date (str|None): optional due date YYYY-MM-DD.

        Returns:
            dict|None: created goal dict on success, None on failure.
        """
        if not user_id or not goal_name:
            print("❌ user_id and goal_name are required.")
            return None
        try:
            target = float(target_amount)
            if target <= 0:
                raise ValueError("target must be positive")
        except (ValueError, TypeError):
            print("❌ Invalid target amount.")
            return None

        # find user
        for u in self.users:
            if u.get("user_id") == user_id:
                goals = u.get("goals") or []
                new_goal = {
                    "goal_id": f"GOAL-{str(uuid.uuid4())[:8].upper()}",
                    "name": goal_name,
                    "target": target,
                    "due_date": due_date,
                    "created_at": datetime.now().strftime("%Y-%m-%d")
                }
                goals.append(new_goal)
                u["goals"] = goals
                try:
                    self.data_manager.add_users(self.users)
                    print(f"✅ Savings goal '{goal_name}' created.")
                    return new_goal
                except Exception as e:
                    print(f"Error saving goal: {e}")
                    return None
        print("❌ User not found.")
        return None

    def get_savings_goals(self, user_id):
        """Return list of goals for a user (may be empty)."""
        for u in self.users:
            if u.get("user_id") == user_id:
                return u.get("goals", []) or []
        return []

    def compute_goal_progress(self, user_id, goal_id):
        """Compute progress for a specific goal.

        Progress is computed using transactions for the user since the goal creation date:
        saved = sum(income) - sum(expense) over that range. Returns dict with saved, target, percent.
        """
        goals = self.get_savings_goals(user_id)
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
        if not goal:
            print("❌ Goal not found.")
            return None

        # reload transactions to ensure latest data
        self.transactions = self.data_manager.load_transactions()
        txns = [t for t in self.transactions if t.get("user_id") == user_id]
        created_at = goal.get("created_at")
        if created_at:
            txns = [t for t in txns if t.get("date") >= created_at]

        income = sum(float(t["amount"]) for t in txns if t.get("type") == "income")
        expense = sum(float(t["amount"]) for t in txns if t.get("type") == "expense")
        saved = income - expense
        target = float(goal.get("target", 0)) or 0.0
        percent = (saved / target * 100) if target > 0 else 0.0
        percent = max(0.0, min(percent, 100.0))
        return {"goal_id": goal_id, "name": goal.get("name"), "saved": saved, "target": target, "percent": percent}
