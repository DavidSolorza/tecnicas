"""
User model class.
Represents a user in the library system.
"""


class User:
    """
    Represents a user in the library system.
    
    Attributes:
        user_id (str): Unique identifier for the user
        name (str): Name of the user
        email (str): Email address of the user
        phone (str): Phone number of the user
    """
    
    def __init__(self, user_id: str, name: str, email: str, phone: str = ""):
        """
        Initialize a User instance.
        
        Args:
            user_id (str): Unique identifier for the user
            name (str): Name of the user
            email (str): Email address of the user
            phone (str, optional): Phone number of the user
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
    
    def __str__(self) -> str:
        """Return string representation of the user."""
        return f"User(ID: {self.user_id}, Name: {self.name})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the user."""
        return f"User(user_id='{self.user_id}', name='{self.name}', email='{self.email}')"
    
    def __eq__(self, other) -> bool:
        """Check if two users have the same user_id."""
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False
    
    def to_dict(self) -> dict:
        """
        Convert user to dictionary format.
        
        Returns:
            dict: Dictionary representation of the user
        """
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        """
        Create a User instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing user data
            
        Returns:
            User: New User instance
        """
        return cls(
            user_id=data.get('user_id', ''),
            name=data.get('name', ''),
            email=data.get('email', ''),
            phone=data.get('phone', '')
        )

