class searchFilter:
    pass


    @staticmethod
    def search_by_range(transactions,start_date,end_date):
        found = False
        for t in transactions:
            if start_date <= t["date"] < end_date:
                print(f"{t["id"]} | {t["date"]} | {t["type"]} | {t["category"]} | {float(t["amount"])}")
                found = True
                
        if not found:
            print("we could seach in this range of dates ")


    
    @staticmethod
    def find_by_category(transactions, category):
        found = False
        for t in transactions:
            if t["category"].lower() == category.lower():
                print("ID | Date | Type | Category | Amount")
                print(f"{t["id"]} | {t["date"]} | {t["type"]} | {t["category"]} | {float(t["amount"])}")
                found = True
                

        if not found:
            print("we don't have this category")

    
               
    
    @staticmethod
    def amount_Range_filter(transactions,min_amount,max_amount):
            found = False
            for t in transactions:
                if int(t["amount"]) >= min_amount and int(t["amount"]) <= max_amount:
                    print(f"{t['id']} | {t['date']} | {t['type']} | {t['category']} | {float(t['amount'])}")
                    found = True
            if not found:
                print("we don't have this range of amounts  ")

                
    
    @staticmethod
    def sort_by_amount(transactions, reverse=False):
        sorted_transactions = sorted(transactions, key=lambda t: float(t["amount"]), reverse=reverse)
        if not sorted_transactions:
            print("No transactions to sort.")
        else:
            for t in sorted_transactions:
                print(f"{t['id']} | {t['date']} | {t['type']} | {t['category']} | {float()}")

