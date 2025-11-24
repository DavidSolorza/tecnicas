"""
Stack (Pila) data structure implementation.
LIFO (Last In, First Out) structure for managing loan history.
"""


class Stack:
    """
    Stack (Pila) implementation using LIFO principle.
    Used for managing loan history where the most recent loan is at the top.
    
    Attributes:
        items (list): List storing stack elements
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item) -> None:
        """
        Add an item to the top of the stack.
        
        Args:
            item: Item to add to the stack
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the stack.
        
        Returns:
            int: Number of items in the stack
        """
        return len(self.items)
    
    def __str__(self) -> str:
        """Return string representation of the stack."""
        return f"Stack({self.items})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the stack."""
        return f"Stack(items={self.items})"
    
    def to_list(self) -> list:
        """
        Convert stack to a list (for serialization).
        
        Returns:
            list: List representation of stack items
        """
        return self.items.copy()
    
    def from_list(self, items: list) -> None:
        """
        Load stack from a list (for deserialization).
        
        Args:
            items (list): List of items to load into the stack
        """
        self.items = items.copy()

