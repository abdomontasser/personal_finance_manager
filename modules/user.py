import uuid 

class User:
  def __init__(self, name, password, currency="USD"):
    self.name =name 
    self.password = password
    self.currency = currency
    self.id = str(uuid.uuid4())

  def convert(self):
    return {
      "name": self.name,
      "password": self.password,
      "currency": self.currency,
      "user_id": self.id
    }