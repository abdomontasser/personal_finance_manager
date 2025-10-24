import json
import csv  
import os 

class manageData:
    def __init__(self,folder = "Data",users_file = 'data.json',transaciton_file = "transactions.csv"):
        self.data_folder = folder
        self.users_file = os.path.join(folder,users_file)
        self.transaction_file = os.path.join(folder,transaciton_file)
        self.ensure_folder_exsists()
        self.ensure_user_file()


    def ensure_folder_exsists(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
        else:
            print(f"{self.data_folder} Created sucessfully")


    def ensure_user_file(self):
        if not os.path.exists(self.users_file):
            with open(self.users_file,"w") as f:
                json.dump([],f,sort_keys=True)
            print("user file created")

        if not os.path.exists(self.transaction_file):
            with open(self.transaction_file,"w",newline="")as f:
                writer = csv.writer(f)
                writer.writerow(["transaction_id","user_id", "type", "amount", "category", "date", "description","payment_method"])
            print("Transcation file created")


    # return data of users 
    def load_users(self):
        with open(self.users_file,"r") as f:
            return json.load(f)

    # Add Data of users 
    def add_users(self,users_list):
        with open(self.users_file,"w") as f:
            return json.dump(users_list,f,indent=4) 



    def load_transactions(self):
        with open(self.transaction_file,"r") as f:
            reader = csv.DictReader(f)
            return list(reader)
        

    def add_transactions(self,transactions):
        with open(self.transaction_file,"w") as f:
            fieldnames = ["transaction_id","user_id", "type", "amount", "category", "date", "description","payment_method"]
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
