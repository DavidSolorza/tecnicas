"""
Searching algorithms implementation.
Contains Linear Search and Binary Search algorithms.
"""


def linear_search(books: list, query: str, search_by: str = 'title') -> list:
    """
    Search for books using Linear Search algorithm.
    Used to search by Title or Author in the General Inventory (unordered list).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        books (list): List of Book objects to search
        query (str): Search query (title or author name)
        search_by (str, optional): Field to search by ('title' or 'author'). Defaults to 'title'.
        
    Returns:
        list: List of matching Book objects
    """
    results = []
    query_lower = query.lower()
    
    for book in books:
        if search_by == 'title':
            if query_lower in book.title.lower():
                results.append(book)
        elif search_by == 'author':
            if query_lower in book.author.lower():
                results.append(book)
    
    return results


def binary_search(books: list, isbn: str) -> int:
    """
    Search for a book by ISBN using Binary Search algorithm.
    CRITICAL: Used to verify if a returned book has pending reservations.
    The inventory must be sorted by ISBN before calling this function.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        books (list): List of Book objects sorted by ISBN
        isbn (str): ISBN to search for
        
    Returns:
        int: Index of the book if found, -1 otherwise
    """
    left = 0
    right = len(books) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if books[mid].isbn == isbn:
            return mid
        elif books[mid].isbn < isbn:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

