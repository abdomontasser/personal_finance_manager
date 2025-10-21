from datetime import datetime
import hashlib
import uuid

class User:
    def __init__(self,name,password,currency = "USD"):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now().date().isoformat()
        self.password_hash = password
        self.currency = currency
        print(f"{self.name} created successfully")

    

    def verify_password(self, entered_password):
        return self.password == entered_password
    

    def to_dict(self):
        return {
            "user_id" : self.user_id,
            "name" : self.name,
            "created_at" : self.created_at,
            "password" : self.password_hash,
            "currency" : self.currency
        }
    
