"""
Shelf model class.
Represents a shelf in the library system.
"""


class Shelf:
    """
    Represents a shelf in the library system.
    
    Attributes:
        shelf_id (str): Unique identifier for the shelf
        capacity (float): Maximum weight capacity in kilograms (default: 8 kg)
        books (list): List of books assigned to this shelf
    """
    
    def __init__(self, shelf_id: str, capacity: float = 8.0):
        """
        Initialize a Shelf instance.
        
        Args:
            shelf_id (str): Unique identifier for the shelf
            capacity (float, optional): Maximum weight capacity in kg. Defaults to 8.0.
        """
        self.shelf_id = shelf_id
        self.capacity = capacity
        self.books = []
    
    def __str__(self) -> str:
        """Return string representation of the shelf."""
        return f"Shelf(ID: {self.shelf_id}, Capacity: {self.capacity} kg, Books: {len(self.books)})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the shelf."""
        return f"Shelf(shelf_id='{self.shelf_id}', capacity={self.capacity}, books={len(self.books)})"
    
    def get_total_weight(self) -> float:
        """
        Calculate the total weight of all books on the shelf.
        
        Returns:
            float: Total weight in kilograms
        """
        return sum(book.weight for book in self.books)
    
    def get_total_value(self) -> float:
        """
        Calculate the total value of all books on the shelf.
        
        Returns:
            float: Total value in Colombian pesos
        """
        return sum(book.value for book in self.books)
    
    def can_add_book(self, book) -> bool:
        """
        Check if a book can be added to the shelf without exceeding capacity.
        
        Args:
            book: Book instance to check
            
        Returns:
            bool: True if book can be added, False otherwise
        """
        return (self.get_total_weight() + book.weight) <= self.capacity
    
    def add_book(self, book) -> bool:
        """
        Add a book to the shelf if capacity allows.
        
        Args:
            book: Book instance to add
            
        Returns:
            bool: True if book was added, False otherwise
        """
        if self.can_add_book(book):
            self.books.append(book)
            book.shelf_id = self.shelf_id
            return True
        return False
    
    def remove_book(self, book) -> bool:
        """
        Remove a book from the shelf.
        
        Args:
            book: Book instance to remove
            
        Returns:
            bool: True if book was removed, False otherwise
        """
        if book in self.books:
            self.books.remove(book)
            book.shelf_id = None
            return True
        return False
    
    def to_dict(self) -> dict:
        """
        Convert shelf to dictionary format.
        
        Returns:
            dict: Dictionary representation of the shelf
        """
        return {
            'shelf_id': self.shelf_id,
            'capacity': self.capacity,
            'books': [book.isbn for book in self.books]
        }

