"""
Sorting algorithms implementation.
Contains Insertion Sort and Merge Sort algorithms.
"""


def insertion_sort(books: list, key=lambda x: x.isbn) -> list:
    """
    Sort a list of books using Insertion Sort algorithm.
    Used to maintain the Ordered Inventory sorted by ISBN.
    
    Time Complexity: O(n²) worst case, O(n) best case
    Space Complexity: O(1)
    
    Args:
        books (list): List of Book objects to sort
        key (callable, optional): Function to extract comparison key. Defaults to ISBN.
        
    Returns:
        list: Sorted list of books
    """
    sorted_books = books.copy()
    
    for i in range(1, len(sorted_books)):
        current = sorted_books[i]
        j = i - 1
        
        # Move elements greater than current one position ahead
        while j >= 0 and key(sorted_books[j]) > key(current):
            sorted_books[j + 1] = sorted_books[j]
            j -= 1
        
        sorted_books[j + 1] = current
    
    return sorted_books


def merge_sort(books: list, key=lambda x: x.value) -> list:
    """
    Sort a list of books using Merge Sort algorithm.
    Used to generate Global Inventory Report sorted by value (COP).
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        books (list): List of Book objects to sort
        key (callable, optional): Function to extract comparison key. Defaults to value.
        
    Returns:
        list: Sorted list of books
    """
    if len(books) <= 1:
        return books.copy()
    
    # Divide: split the list into two halves
    mid = len(books) // 2
    left = merge_sort(books[:mid], key)
    right = merge_sort(books[mid:], key)
    
    # Conquer: merge the sorted halves
    return _merge(left, right, key)


def _merge(left: list, right: list, key) -> list:
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        left (list): First sorted list
        right (list): Second sorted list
        key (callable): Function to extract comparison key
        
    Returns:
        list: Merged sorted list
    """
    result = []
    i = j = 0
    
    # Compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

