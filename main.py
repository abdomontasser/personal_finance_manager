from finance_manger import FinanceManager
from report_generator import ReportGenerator
from Search_filter import searchFilter

class App:
    
    def __init__(self):
        self.manager = FinanceManager()
        self.current_user = None

    def run(self):
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
        name = input("Enter name: ")
        password = input("Enter password: ")
        currency = input("Enter currency (default USD): ") or "USD"
        self.manager.register_user(name, password, currency)

    def login(self):
        name = input("Username: ")
        password = input("Password: ")
        user = self.manager.login(name, password)
        if user:
            self.current_user = user
            self.user_menu()

    def user_menu(self):
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
        t_type = input("Type (income/expense): ")
        amount = input("Amount: ")
        category = input("Category: ")
        desc = input("Description: ")
        payment_method = input("payment method")
        date = input("Enter date in format (YYYY-MM-DD)")
        self.manager.add_transaction(self.current_user["user_id"], t_type, amount, category, desc,payment_method,date)

    def reports_menu(self):
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
            min_a = float(input("Min amount: "))
            max_a = float(input("Max amount: "))
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
