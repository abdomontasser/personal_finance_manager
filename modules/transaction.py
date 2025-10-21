import uuid
from datetime import datetime
from decimal import Decimal

class Transaction:
  def __init__(self, user_id, type_, amount, category, description, payment_method, date=None):
    self.transaction_id = f"TXN-{str(uuid.uuid4())[:8].upper()}"
    self.user_id = user_id
    self.type = type_
    self.amount = Decimal(amount)
    self.category = category
    self.date = date or datetime.now().strftime("%Y-%m-%d")
    self.description = description
    self.payment_method = payment_method
    
  def to_dict(self):
    return {
      "transaction_id": self.transaction_id,
      "user_id": self.user_id,
      "type": self.type,
      "amount": float(self.amount),
      "category": self.category,
      "date": self.date,
      "description": self.description,
      "payment_method": self.payment_method
    }
  
  def __str__(self):
    return f"{self.date} | {self.type:<7} | {self.category:<10} | {self.amount:>8} | {self.description} ({self.payment_method})"

