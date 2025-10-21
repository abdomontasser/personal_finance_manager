from collections import defaultdict
from decimal import Decimal
from datetime import datetime

class ReportGenerator:
  def __init__(self, user):
    self.user = user

  def format_money(self, amount):
    return f"${amount:.2f}"

  def dashboard_summary(self, period=None):
    income = sum(t.amount for t in self.user.transactions if t.type == "income")
    expenses = sum(t.amount for t in self.user.transactions if t.type == "expense")
    balance = income - expenses
    net_savings = income - expenses

    categories = defaultdict(Decimal)
    for t in self.user.transactions:
      if t.type == "expense":
        categories[t.category] += t.amount

    total_expenses = sum(categories.values())
    top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n" + "=" * 60)
    print("          PERSONAL FINANCE MANAGER v1.0")
    print("=" * 60)
    print(f"User: {self.user.name}")
    print(f"Period: {period or datetime.now().strftime('%B %Y')}")
    print("-" * 60)
    print(f"Total Income:   {self.format_money(income)}")
    print(f"Total Expenses: {self.format_money(expenses)}")
    print(f"Net Savings:    {self.format_money(net_savings)}")
    print("-" * 60)
    print(f"Current Balance: {self.format_money(balance)}")
    print("-" * 60)
    print("Top Spending Categories:")
    if not top_categories:
        print("No expense data yet.")
    else:
        for i, (cat, amt) in enumerate(top_categories, start=1):
            percent = (amt / total_expenses * 100) if total_expenses else 0
            print(f"{i}. {cat:<15} {self.format_money(amt)} ({percent:.1f}%)")
    print("=" * 60)