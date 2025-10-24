class searchFilter:

    @staticmethod
    def search_by_range(transactions, start_date, end_date):
<<<<<<< HEAD
        """Return transactions with date in [start_date, end_date)."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        results = []
        for t in transactions:
            if start_date <= t["date"] < end_date:
                results.append(t)
        return results

    @staticmethod
    def find_by_category(transactions, category):
<<<<<<< HEAD
        """Return transactions whose category matches (case-insensitive)."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        results = []
        for t in transactions:
            if t["category"].lower() == category.lower():
                results.append(t)
        return results

    @staticmethod
    def amount_Range_filter(transactions, min_amount, max_amount):
<<<<<<< HEAD
        """Return transactions with amount between min_amount and max_amount."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        results = []
        for t in transactions:
            amount = float(t["amount"])
            if min_amount <= amount <= max_amount:
                results.append(t)
        return results

    @staticmethod
    def sort_by_amount(transactions, reverse=False):
<<<<<<< HEAD
        """Return transactions sorted by amount. reverse=True for descending."""
=======
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        return sorted(transactions, key=lambda t: float(t["amount"]), reverse=reverse)
