from datetime import datetime
import hashlib
import uuid

class User:
    def __init__(self,name,password,currency = "USD"):
<<<<<<< HEAD
        """Create a User instance with a generated UUID and store credentials.

        Note: password is stored as-is in this version.
        """
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now().date().isoformat()
        # store as-is for now; consider hashing later
=======
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now().date().isoformat()
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        self.password_hash = password
        self.currency = currency
        print(f"{self.name} created successfully")

<<<<<<< HEAD
    def verify_password(self, entered_password):
        """Verify a provided password against the stored password hash.

        Args:
            entered_password (str): Password to verify.

        Returns:
            bool: True if the password matches.
        """
        return self.password_hash == entered_password
    
    def to_dict(self):
        """Return a serializable dict for this user."""
=======
    

    def verify_password(self, entered_password):
        return self.password == entered_password
    

    def to_dict(self):
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
        return {
            "user_id" : self.user_id,
            "name" : self.name,
            "created_at" : self.created_at,
            "password" : self.password_hash,
            "currency" : self.currency
        }
<<<<<<< HEAD

=======
    
>>>>>>> efabfae6a36f20ce0b535a2e9956c85b44d2e04c
