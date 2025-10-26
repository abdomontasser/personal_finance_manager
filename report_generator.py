class ReportGenerator:
    """Handles financial summaries and statistics."""

    @staticmethod
    def dashboard(transactions, user_id):
        """Print a dashboard summary (income, expense, balance) for a user."""
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
        """Print transactions for the specified month (format: YYYY-MM)."""
        month_txns = [t for t in transactions if t["user_id"] == user_id and t["date"].startswith(month)]
        print(f"\n📅 Report for {month}")
        for t in month_txns:
            print(f"{t['date']} - {t['category']} : {t['amount']} ({t['type']})")

    @staticmethod
    def category_breakdown(transactions, user_id):
        """Print expense totals grouped by category for the user."""
        user_txns = [t for t in transactions if t["user_id"] == user_id]
        categories = {}
        for t in user_txns:
            if t["type"] == "expense":
                categories[t["category"]] = categories.get(t["category"], 0) + float(t["amount"])
        print("\n💸 Expense Breakdown by Category:")
        for cat, total in categories.items():
            print(f"{cat}: {total}")

    @staticmethod
    def calculate_financial_health(transactions, user_id):
        """Calculate financial health score (0-100) based on multiple metrics.
        
        Metrics:
        1. Savings Rate (40 points): % of income saved
        2. Expense Stability (20 points): consistency in monthly expenses
        3. Income Stability (20 points): consistency in monthly income
        4. Expense Diversity (20 points): spread across expense categories
        """
        user_txns = [t for t in transactions if t["user_id"] == user_id]
        if not user_txns:
            return {"score": 0, "details": "No transactions found"}

        # Calculate total income and expenses
        income = sum(float(t["amount"]) for t in user_txns if t["type"] == "income")
        expenses = sum(float(t["amount"]) for t in user_txns if t["type"] == "expense")
        
        # 1. Savings Rate (40 points)
        savings_rate = ((income - expenses) / income * 100) if income > 0 else 0
        savings_score = min(40, (savings_rate / 30) * 40)  # 30% savings rate = full points
        
        # 2. Expense Stability (20 points)
        monthly_expenses = {}
        for t in user_txns:
            if t["type"] == "expense":
                month = t["date"][:7]  # YYYY-MM
                monthly_expenses[month] = monthly_expenses.get(month, 0) + float(t["amount"])
        
        if len(monthly_expenses) > 1:
            expense_variance = (max(monthly_expenses.values()) - min(monthly_expenses.values())) / max(monthly_expenses.values())
            expense_stability = 20 * (1 - min(1, expense_variance))
        else:
            expense_stability = 10  # Not enough data
            
        # 3. Income Stability (20 points)
        monthly_income = {}
        for t in user_txns:
            if t["type"] == "income":
                month = t["date"][:7]
                monthly_income[month] = monthly_income.get(month, 0) + float(t["amount"])
        
        if len(monthly_income) > 1:
            income_variance = (max(monthly_income.values()) - min(monthly_income.values())) / max(monthly_income.values())
            income_stability = 20 * (1 - min(1, income_variance))
        else:
            income_stability = 10  # Not enough data
            
        # 4. Expense Diversity (20 points)
        expense_categories = {}
        for t in user_txns:
            if t["type"] == "expense":
                expense_categories[t["category"]] = expense_categories.get(t["category"], 0) + float(t["amount"])
        
        category_count = len(expense_categories)
        diversity_score = min(20, category_count * 4)  # 5+ categories = full points
        
        # Calculate total score
        total_score = round(savings_score + expense_stability + income_stability + diversity_score)
        
        return {
            "score": total_score,
            "details": {
                "savings_rate": round(savings_rate, 1),
                "savings_score": round(savings_score, 1),
                "expense_stability": round(expense_stability, 1),
                "income_stability": round(income_stability, 1),
                "diversity_score": round(diversity_score, 1)
            }
        }
