from finance_manger import FinanceManager
from report_generator import ReportGenerator
from Search_filter import searchFilter
from datetime import datetime

class App:
    """Console application entrypoint for interacting with the FinanceManager."""
    
    def __init__(self):
        """Initialize the App with a FinanceManager and no current_user."""
        self.manager = FinanceManager()
        self.current_user = None

    def run(self):
        """Main loop showing the top-level menu and routing user choices."""
        while True:
            print("\n==== Personal Finance Manager ====")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("Invalid option!")

    def register(self):
        """Collect input and register a new user after basic validation."""
        name = input("Enter name: ").strip()
        password = input("Enter password: ").strip()
        if not name or not password:
            print("❌ Name and password cannot be empty.")
            return
        currency = input("Enter currency (default USD): ").strip() or "USD"
        self.manager.register_user(name, password, currency)

    def login(self):
        """Prompt for credentials and start user menu on successful login."""
        name = input("Username: ").strip()
        password = input("Password: ").strip()
        user = self.manager.login(name, password)
        if user:
            self.current_user = user
            self.user_menu()

    def user_menu(self):
        """Show authenticated user menu and handle actions."""
        while True:
            print(f"\n==== Welcome {self.current_user['name']} ====")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Reports")
            print("4. Search & Filter")
            print("5. Import/Export")
            print("6. Savings Goals")
            print("7. Logout")
            choice = input("Choose: ")

            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.manager.view_transactions(self.current_user["user_id"])
            elif choice == "3":
                self.reports_menu()
            elif choice == "4":
                self.search_menu()
            elif choice == "5":
                self.import_export_menu()
            elif choice == "6":
                self.savings_menu()
            elif choice == "7":
                print("Logging out...")
                break
            else:
                print("Invalid option!")

    def savings_menu(self):
        """Manage savings goals: list, add, view progress."""
        while True:
            print("\n=== Savings Goals ===")
            print("1. List goals")
            print("2. Add goal")
            print("3. View goal progress")
            print("4. Back")
            choice = input("Choose: ")

            if choice == "1":
                goals = self.manager.get_savings_goals(self.current_user["user_id"])
                if not goals:
                    print("No goals found.")
                else:
                    for g in goals:
                        print(f"{g['goal_id']} | {g['name']} | target: {g['target']} | due: {g.get('due_date')}")
            elif choice == "2":
                name = input("Goal name: ").strip()
                target = input("Target amount: ").strip()
                due = input("Due date (YYYY-MM-DD, optional): ").strip() or None
                self.manager.add_savings_goal(self.current_user["user_id"], name, target, due)
            elif choice == "3":
                gid = input("Enter goal_id: ").strip()
                prog = self.manager.compute_goal_progress(self.current_user["user_id"], gid)
                if prog:
                    print(f"Goal: {prog['name']} — saved {prog['saved']:.2f} / {prog['target']:.2f} ({prog['percent']:.1f}%)")
            elif choice == "4":
                return
            else:
                print("Invalid choice!")
            return

        print("✅ Operation completed.")

    def add_transaction(self):
        """Prompt inputs for a transaction, validate, and forward to manager."""
        t_type = input("Type (income/expense): ").strip().lower()
        if t_type not in ("income", "expense"):
            print("❌ Invalid type. Use 'income' or 'expense'.")
            return

        amount_input = input("Amount: ").strip()
        try:
            amount = float(amount_input)
        except ValueError:
            print("❌ Invalid amount. Please enter a numeric value.")
            return

        category = input("Category: ").strip()
        if not category:
            print("❌ Category cannot be empty.")
            return

        desc = input("Description: ").strip()
        payment_method = input("Payment method: ").strip()
        date_input = input("Enter date in format (YYYY-MM-DD) (leave empty for today): ").strip()
        if date_input:
            try:
                # validate format
                parsed = datetime.strptime(date_input, "%Y-%m-%d")
                date = parsed.strftime("%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD.")
                return
        else:
            date = datetime.now().strftime("%Y-%m-%d")

        self.manager.add_transaction(self.current_user["user_id"], t_type, amount, category, desc, payment_method, date)

    def reports_menu(self):
        """Show report options and call ReportGenerator methods."""
        txns = self.manager.get_user_transactions(self.current_user["user_id"])
        print("\n1. Dashboard Summary")
        print("2. Monthly Report")
        print("3. Category Breakdown")
        choice = input("Choose: ")

        if choice == "1":
            ReportGenerator.dashboard(txns, self.current_user["user_id"])
        elif choice == "2":
            month = input("Enter month (YYYY-MM): ")
            ReportGenerator.monthly_report(txns, self.current_user["user_id"], month)
        elif choice == "3":
            ReportGenerator.category_breakdown(txns, self.current_user["user_id"])

    def search_menu(self):
        """Provide search/filter options and print matching transactions."""
        txns = self.manager.get_user_transactions(self.current_user["user_id"])
        print("\n1. Filter by Category")
        print("2. Filter by Date Range")
        print("3. Filter by Amount Range")
        print("4. Sort by Amount")
        choice = input("Choose: ")

        if choice == "1":
            cat = input("Enter category: ")
            results = searchFilter.find_by_category(txns, cat)
        elif choice == "2":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            results = searchFilter.search_by_range(txns, start, end)
        elif choice == "3":
            try:
                min_a = float(input("Min amount: "))
                max_a = float(input("Max amount: "))
            except ValueError:
                print("❌ Invalid amount range.")
                return
            results = searchFilter.amount_Range_filter(txns, min_a, max_a)
        elif choice == "4":
            reverse = input("Sort descending? (y/n): ").lower() == "y"
            results = searchFilter.sort_by_amount(txns, reverse)
        else:
            print("Invalid choice!")
            return

        if results:
            print("\n=== Search Results ===")
            print("ID | Date | Type | Category | Amount")
            for t in results:
                print(f"{t['transaction_id']} | {t['date']} | {t['type']} | {t['category']} | {float(t['amount'])}")
        else:
            print("No results found.")


if __name__ == "__main__":
    App().run()
