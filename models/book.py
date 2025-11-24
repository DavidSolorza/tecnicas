"""
Book model class.
Represents a book in the library system with ISBN, title, author, weight, and value.
"""


class Book:
    """
    Represents a book in the library system.
    
    Attributes:
        isbn (str): International Standard Book Number
        title (str): Title of the book
        author (str): Author of the book
        weight (float): Weight of the book in kilograms
        value (float): Value of the book in Colombian pesos (COP)
        stock (int): Number of available copies
        shelf_id (str, optional): ID of the shelf where the book is located
    """
    
    def __init__(self, isbn: str, title: str, author: str, weight: float, 
                 value: float, stock: int = 1, shelf_id: str = None):
        """
        Initialize a Book instance.
        
        Args:
            isbn (str): International Standard Book Number
            title (str): Title of the book
            author (str): Author of the book
            weight (float): Weight of the book in kilograms
            value (float): Value of the book in Colombian pesos (COP)
            stock (int, optional): Number of available copies. Defaults to 1.
            shelf_id (str, optional): ID of the shelf where the book is located
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.weight = weight
        self.value = value
        self.stock = stock
        self.shelf_id = shelf_id
    
    def __str__(self) -> str:
        """Return string representation of the book."""
        return f"Book(ISBN: {self.isbn}, Title: {self.title}, Author: {self.author})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the book."""
        return (f"Book(isbn='{self.isbn}', title='{self.title}', "
                f"author='{self.author}', weight={self.weight}, "
                f"value={self.value}, stock={self.stock})")
    
    def __eq__(self, other) -> bool:
        """Check if two books have the same ISBN."""
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False
    
    def __lt__(self, other) -> bool:
        """Compare books by ISBN for sorting."""
        if isinstance(other, Book):
            return self.isbn < other.isbn
        return NotImplemented
    
    def to_dict(self) -> dict:
        """
        Convert book to dictionary format.
        
        Returns:
            dict: Dictionary representation of the book
        """
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'weight': self.weight,
            'value': self.value,
            'stock': self.stock,
            'shelf_id': self.shelf_id
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """
        Create a Book instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing book data
            
        Returns:
            Book: New Book instance
        """
        return cls(
            isbn=data.get('isbn', ''),
            title=data.get('title', ''),
            author=data.get('author', ''),
            weight=float(data.get('weight', 0)),
            value=float(data.get('value', 0)),
            stock=int(data.get('stock', 1)),
            shelf_id=data.get('shelf_id')
        )

