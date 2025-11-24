"""
File handling utilities for loading and saving data.
Supports CSV and JSON formats for books, loan history, and reservations.
"""

import csv
import json
import os
from datetime import datetime
from typing import List, Dict, Any
from models.book import Book
from data_structures.stack import Stack
from data_structures.queue import Queue


def load_books_from_csv(filepath: str) -> List[Book]:
    """
    Load books from a CSV file.
    
    Expected CSV format:
    ISBN,Title,Author,Weight,Value,Stock
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        List[Book]: List of Book objects loaded from the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file format is invalid
    """
    books = []
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            try:
                book = Book(
                    isbn=row['ISBN'].strip(),
                    title=row['Title'].strip(),
                    author=row['Author'].strip(),
                    weight=float(row['Weight']),
                    value=float(row['Value']),
                    stock=int(row.get('Stock', 1))
                )
                books.append(book)
            except (KeyError, ValueError) as e:
                raise ValueError(f"Invalid CSV format in row: {row}. Error: {e}")
    
    return books


def load_books_from_json(filepath: str) -> List[Book]:
    """
    Load books from a JSON file.
    
    Expected JSON format:
    [
        {
            "isbn": "...",
            "title": "...",
            "author": "...",
            "weight": ...,
            "value": ...,
            "stock": ...
        },
        ...
    ]
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        List[Book]: List of Book objects loaded from the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file format is invalid
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"JSON file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    books = []
    for item in data:
        books.append(Book.from_dict(item))
    
    return books


def save_books_to_json(books: List[Book], filepath: str) -> None:
    """
    Save books to a JSON file.
    
    Args:
        books (List[Book]): List of Book objects to save
        filepath (str): Path to save the JSON file
    """
    data = [book.to_dict() for book in books]
    
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def save_loan_history(loan_history: Dict[str, Stack], filepath: str) -> None:
    """
    Save loan history (stack) to a JSON file.
    
    Args:
        loan_history (Dict[str, Stack]): Dictionary mapping user_id to Stack of loans
        filepath (str): Path to save the JSON file
    """
    data = {}
    for user_id, stack in loan_history.items():
        data[user_id] = stack.to_list()
    
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_loan_history(filepath: str) -> Dict[str, Stack]:
    """
    Load loan history from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        Dict[str, Stack]: Dictionary mapping user_id to Stack of loans
    """
    if not os.path.exists(filepath):
        return {}
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    loan_history = {}
    for user_id, items in data.items():
        stack = Stack()
        stack.from_list(items)
        loan_history[user_id] = stack
    
    return loan_history


def save_reservations(reservations: Dict[str, Queue], filepath: str) -> None:
    """
    Save reservations (queue) to a JSON file.
    
    Args:
        reservations (Dict[str, Queue]): Dictionary mapping ISBN to Queue of reservations
        filepath (str): Path to save the JSON file
    """
    data = {}
    for isbn, queue in reservations.items():
        data[isbn] = queue.to_list()
    
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_reservations(filepath: str) -> Dict[str, Queue]:
    """
    Load reservations from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        Dict[str, Queue]: Dictionary mapping ISBN to Queue of reservations
    """
    if not os.path.exists(filepath):
        return {}
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    reservations = {}
    for isbn, items in data.items():
        queue = Queue()
        queue.from_list(items)
        reservations[isbn] = queue
    
    return reservations


def save_report_to_file(report: str, filepath: str) -> None:
    """
    Save a report to a text file.
    
    Args:
        report (str): Report content to save
        filepath (str): Path to save the text file
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(report)

