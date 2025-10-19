import uuid 

class User:
  def __init__(self, name, password, currency="USD"):
    self.name =name 
    self.password = password
    self.currency = currency
    self.id = str(uuid.uuid4())
    self.transactions = []

  def add_transaction(self, transaction):
    self.transactions.append(transaction)

  def verify_password(self, entered_password):
    return self.password == entered_password
  def convert(self):
    return {
      "user_id": self.user_id,
      "name": self.name,
      "password": self.password,
      "currency": self.currency,
      "transactions": [t.convert() for t in self.transactions]
    }