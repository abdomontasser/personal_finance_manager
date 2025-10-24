class searchFilter:

    @staticmethod
    def search_by_range(transactions, start_date, end_date):
        """Return transactions with date in [start_date, end_date)."""
        results = []
        for t in transactions:
            if start_date <= t["date"] < end_date:
                results.append(t)
        return results

    @staticmethod
    def find_by_category(transactions, category):
        """Return transactions whose category matches (case-insensitive)."""
        results = []
        for t in transactions:
            if t["category"].lower() == category.lower():
                results.append(t)
        return results

    @staticmethod
    def amount_Range_filter(transactions, min_amount, max_amount):
        """Return transactions with amount between min_amount and max_amount."""
        results = []
        for t in transactions:
            amount = float(t["amount"])
            if min_amount <= amount <= max_amount:
                results.append(t)
        return results

    @staticmethod
    def sort_by_amount(transactions, reverse=False):
        """Return transactions sorted by amount. reverse=True for descending."""
        return sorted(transactions, key=lambda t: float(t["amount"]), reverse=reverse)
