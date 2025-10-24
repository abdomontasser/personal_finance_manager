class ReportGenerator:
<<<<<<< HEAD
    """Handles financial summaries and statistics."""

    @staticmethod
    def dashboard(transactions, user_id):
        """Print a dashboard summary (income, expense, balance) for a user."""
=======
    """Handles financial summaries and statistics"""

    @staticmethod
    def dashboard(transactions, user_id):
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        user_txns = [t for t in transactions if t["user_id"] == user_id]
        income = sum(float(t["amount"]) for t in user_txns if t["type"] == "income")
        expense = sum(float(t["amount"]) for t in user_txns if t["type"] == "expense")
        balance = income - expense
        print("\n=== Dashboard Summary ===")
        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print(f"Balance: {balance}")

    @staticmethod
    def monthly_report(transactions, user_id, month):
<<<<<<< HEAD
        """Print transactions for the specified month (format: YYYY-MM)."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        month_txns = [t for t in transactions if t["user_id"] == user_id and t["date"].startswith(month)]
        print(f"\n📅 Report for {month}")
        for t in month_txns:
            print(f"{t['date']} - {t['category']} : {t['amount']} ({t['type']})")

    @staticmethod
    def category_breakdown(transactions, user_id):
<<<<<<< HEAD
        """Print expense totals grouped by category for the user."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        user_txns = [t for t in transactions if t["user_id"] == user_id]
        categories = {}
        for t in user_txns:
            if t["type"] == "expense":
                categories[t["category"]] = categories.get(t["category"], 0) + float(t["amount"])
        print("\n💸 Expense Breakdown by Category:")
        for cat, total in categories.items():
            print(f"{cat}: {total}")
