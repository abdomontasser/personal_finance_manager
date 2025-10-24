from finance_manger import FinanceManager
from report_generator import ReportGenerator
from Search_filter import searchFilter
<<<<<<< HEAD
from datetime import datetime

class App:
    """Console application entrypoint for interacting with the FinanceManager."""
    
    def __init__(self):
        """Initialize the App with a FinanceManager and no current_user."""
=======

class App:
    
    def __init__(self):
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        self.manager = FinanceManager()
        self.current_user = None

    def run(self):
<<<<<<< HEAD
        """Main loop showing the top-level menu and routing user choices."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
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
<<<<<<< HEAD
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
=======
        name = input("Enter name: ")
        password = input("Enter password: ")
        currency = input("Enter currency (default USD): ") or "USD"
        self.manager.register_user(name, password, currency)

    def login(self):
        name = input("Username: ")
        password = input("Password: ")
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        user = self.manager.login(name, password)
        if user:
            self.current_user = user
            self.user_menu()

    def user_menu(self):
<<<<<<< HEAD
        """Show authenticated user menu and handle actions."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        while True:
            print(f"\n==== Welcome {self.current_user['name']} ====")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Reports")
            print("4. Search & Filter")
            print("5. Logout")
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
                print("Logging out...")
                break
            else:
                print("Invalid option!")

    def add_transaction(self):
<<<<<<< HEAD
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
=======
        t_type = input("Type (income/expense): ")
        amount = input("Amount: ")
        category = input("Category: ")
        desc = input("Description: ")
        payment_method = input("payment method")
        date = input("Enter date in format (YYYY-MM-DD)")
        self.manager.add_transaction(self.current_user["user_id"], t_type, amount, category, desc,payment_method,date)

    def reports_menu(self):
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
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
<<<<<<< HEAD
        """Provide search/filter options and print matching transactions."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
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
<<<<<<< HEAD
            try:
                min_a = float(input("Min amount: "))
                max_a = float(input("Max amount: "))
            except ValueError:
                print("❌ Invalid amount range.")
                return
=======
            min_a = float(input("Min amount: "))
            max_a = float(input("Max amount: "))
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
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
