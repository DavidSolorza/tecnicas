"""
Queue (Cola) data structure implementation.
FIFO (First In, First Out) structure for managing book reservations.
"""


class Queue:
    """
    Queue (Cola) implementation using FIFO principle.
    Used for managing book reservations where the first person in line gets priority.
    
    Attributes:
        items (list): List storing queue elements
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item) -> None:
        """
        Add an item to the end of the queue.
        
        Args:
            item: Item to add to the queue
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """
        Return the first item without removing it.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the queue.
        
        Returns:
            int: Number of items in the queue
        """
        return len(self.items)
    
    def __str__(self) -> str:
        """Return string representation of the queue."""
        return f"Queue({self.items})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the queue."""
        return f"Queue(items={self.items})"
    
    def to_list(self) -> list:
        """
        Convert queue to a list (for serialization).
        
        Returns:
            list: List representation of queue items
        """
        return self.items.copy()
    
    def from_list(self, items: list) -> None:
        """
        Load queue from a list (for deserialization).
        
        Args:
            items (list): List of items to load into the queue
        """
        self.items = items.copy()

