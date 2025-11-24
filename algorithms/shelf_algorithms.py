"""
Shelf assignment algorithms implementation.
Contains Brute Force and Backtracking algorithms for shelf optimization.
"""

from itertools import combinations
from models.book import Book


def find_risky_combinations(books: list, threshold: float = 8.0) -> list:
    """
    Find all combinations of four books that exceed the weight threshold.
    Uses Brute Force algorithm to exhaustively explore all combinations.
    
    Time Complexity: O(n^4) where n is the number of books
    Space Complexity: O(n^4) for storing combinations
    
    Args:
        books (list): List of Book objects
        threshold (float, optional): Weight threshold in kg. Defaults to 8.0.
        
    Returns:
        list: List of tuples, each containing 4 books that exceed the threshold
    """
    risky_combinations = []
    
    # Generate all combinations of 4 books
    for combo in combinations(books, 4):
        total_weight = sum(book.weight for book in combo)
        
        if total_weight > threshold:
            risky_combinations.append(combo)
    
    return risky_combinations


def find_optimal_shelf(books: list, max_capacity: float = 8.0) -> tuple:
    """
    Find the optimal combination of books that maximizes value without exceeding weight capacity.
    Uses Backtracking algorithm to explore and find the best solution.
    
    Time Complexity: O(2^n) worst case
    Space Complexity: O(n) for recursion stack
    
    Args:
        books (list): List of Book objects
        max_capacity (float, optional): Maximum weight capacity in kg. Defaults to 8.0.
        
    Returns:
        tuple: (optimal_books, total_value, total_weight) - Best combination found
    """
    best_combination = []
    best_value = 0
    best_weight = 0
    
    def backtrack(current_index: int, current_books: list, current_weight: float, current_value: float):
        """
        Recursive backtracking function to explore all possible combinations.
        
        Args:
            current_index (int): Current index in the books list
            current_books (list): Current combination of books
            current_weight (float): Current total weight
            current_value (float): Current total value
        """
        nonlocal best_combination, best_value, best_weight
        
        # Base case: processed all books
        if current_index >= len(books):
            # Update best if current solution is better
            if current_value > best_value:
                best_combination = current_books.copy()
                best_value = current_value
                best_weight = current_weight
            return
        
        # Option 1: Don't include current book
        backtrack(current_index + 1, current_books, current_weight, current_value)
        
        # Option 2: Include current book (if it fits)
        book = books[current_index]
        if current_weight + book.weight <= max_capacity:
            current_books.append(book)
            backtrack(
                current_index + 1,
                current_books,
                current_weight + book.weight,
                current_value + book.value
            )
            current_books.pop()  # Backtrack: remove last book
    
    # Start backtracking
    backtrack(0, [], 0.0, 0.0)
    
    return (best_combination, best_value, best_weight)

