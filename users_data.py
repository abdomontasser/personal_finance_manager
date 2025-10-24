import json
import csv  
import os 

class manageData:
    def __init__(self,folder = "Data",users_file = 'data.json',transaciton_file = "transactions.csv"):
        """Initialize storage paths and ensure data files/folders exist.

        Args:
            folder (str): Data folder path.
            users_file (str): Users filename inside data folder.
            transaciton_file (str): Transactions filename inside data folder.
        """
        self.data_folder = folder
        self.users_file = os.path.join(folder,users_file)
        self.transaction_file = os.path.join(folder,transaciton_file)
        self.ensure_folder_exsists()
        self.ensure_user_file()


    def ensure_folder_exsists(self):
        """Create the data folder if it does not exist. Logs OSError on failure."""
        try:
            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)
            else:
                print(f"{self.data_folder} Created sucessfully")
        except OSError as e:
            print(f"Error creating data folder '{self.data_folder}': {e}")


    def ensure_user_file(self):
        """Create users JSON and transactions CSV files if they do not exist."""
        try:
            if not os.path.exists(self.users_file):
                with open(self.users_file,"w") as f:
                    json.dump([],f,sort_keys=True)
                print("user file created")
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error creating users file '{self.users_file}': {e}")

        try:
            if not os.path.exists(self.transaction_file):
                with open(self.transaction_file,"w",newline="")as f:
                    writer = csv.writer(f)
                    writer.writerow(["transaction_id","user_id", "type", "amount", "category", "date", "description","payment_method"])
                print("Transcation file created")
        except OSError as e:
            print(f"Error creating transactions file '{self.transaction_file}': {e}")


    def load_users(self):
        """Load and return the list of users from the users JSON file.
        
        Returns:
            list: list of user dicts, or [] on error.
        """
        try:
            with open(self.users_file,"r") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading users from '{self.users_file}': {e}")
            return []

    def add_users(self,users_list):
        """Overwrite the users file with the provided users_list.

        Args:
            users_list (list): List of user dictionaries to save.
        """
        try:
            with open(self.users_file,"w") as f:
                json.dump(users_list,f,indent=4)
        except OSError as e:
            print(f"Error writing users to '{self.users_file}': {e}")

    def load_transactions(self):
        """Load transactions from the CSV file and return as list of dicts.

        Returns:
            list: list of transaction dicts, or [] on error.
        """
        try:
            with open(self.transaction_file,"r") as f:
                reader = csv.DictReader(f)
                return list(reader)
        except OSError as e:
            print(f"Error reading transactions from '{self.transaction_file}': {e}")
            return []
        except csv.Error as e:
            print(f"CSV parsing error in '{self.transaction_file}': {e}")
            return []
        

    def add_transactions(self,transactions):
        """Write the list of transaction dicts to the CSV file.

        Args:
            transactions (list): List of transaction dictionaries to write.
        """
        try:
            with open(self.transaction_file,"w",newline="") as f:
                fieldnames = ["transaction_id","user_id", "type", "amount", "category", "date", "description","payment_method"]
                writer = csv.DictWriter(f,fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(transactions)
        except OSError as e:
            print(f"Error writing transactions to '{self.transaction_file}': {e}")
        except csv.Error as e:
            print(f"CSV writing error to '{self.transaction_file}': {e}")
