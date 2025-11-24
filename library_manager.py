"""
Library Management System (SGB) - Main Module
Comprehensive library management system with all required features.
"""

import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from models.book import Book
from models.user import User
from models.shelf import Shelf
from data_structures.stack import Stack
from data_structures.queue import Queue
from algorithms.sorting import insertion_sort, merge_sort
from algorithms.searching import linear_search, binary_search
from algorithms.shelf_algorithms import find_risky_combinations, find_optimal_shelf
from algorithms.recursion import calculate_author_total_value, calculate_author_average_weight
from utils.file_handler import (
    load_books_from_csv, load_books_from_json, save_books_to_json,
    save_loan_history, load_loan_history,
    save_reservations, load_reservations,
    save_report_to_file
)


class LibraryManager:
    """
    Main Library Management System class.
    Manages books, users, shelves, loans, and reservations.
    """
    
    def __init__(self):
        """Initialize the Library Management System."""
        # Two master lists as required
        self.general_inventory = []  # Unordered list (order of loading)
        self.ordered_inventory = []  # Always sorted by ISBN (ascending)
        
        # Data structures
        self.loan_history = {}  # Dict[user_id, Stack] - LIFO for loan history
        self.reservations = {}  # Dict[isbn, Queue] - FIFO for reservations
        
        # Additional management
        self.users = {}  # Dict[user_id, User]
        self.shelves = {}  # Dict[shelf_id, Shelf]
        
        # File paths
        self.books_file = "data/books.json"
        self.loan_history_file = "data/loan_history.json"
        self.reservations_file = "data/reservations.json"
    
    # ==================== DATA ACQUISITION ====================
    
    def load_initial_inventory(self, filepath: str, file_format: str = 'json') -> int:
        """
        Load initial inventory from CSV or JSON file.
        
        Args:
            filepath (str): Path to the data file
            file_format (str, optional): File format ('csv' or 'json'). Defaults to 'json'.
            
        Returns:
            int: Number of books loaded
        """
        try:
            if file_format.lower() == 'csv':
                books = load_books_from_csv(filepath)
            else:
                books = load_books_from_json(filepath)
            
            # Add to general inventory (unordered)
            self.general_inventory.extend(books)
            
            # Add to ordered inventory and maintain sort
            self.ordered_inventory.extend(books)
            self.ordered_inventory = insertion_sort(self.ordered_inventory)
            
            return len(books)
        except Exception as e:
            print(f"Error cargando inventario: {e}")
            return 0
    
    def save_data(self) -> None:
        """Save all data to files."""
        try:
            # Create data directory if it doesn't exist
            os.makedirs("data", exist_ok=True)
            
            # Save books
            save_books_to_json(self.general_inventory, self.books_file)
            
            # Save loan history
            save_loan_history(self.loan_history, self.loan_history_file)
            
            # Save reservations
            save_reservations(self.reservations, self.reservations_file)
            
            print("Datos guardados exitosamente.")
        except Exception as e:
            print(f"Error guardando datos: {e}")
    
    def load_data(self) -> None:
        """Load all data from files."""
        try:
            # Load books
            if os.path.exists(self.books_file):
                books = load_books_from_json(self.books_file)
                self.general_inventory = books
                self.ordered_inventory = insertion_sort(books.copy())
            
            # Load loan history
            self.loan_history = load_loan_history(self.loan_history_file)
            
            # Load reservations
            self.reservations = load_reservations(self.reservations_file)
            
            print("Datos cargados exitosamente.")
        except Exception as e:
            print(f"Error cargando datos: {e}")
    
    # ==================== BOOK MANAGEMENT (CRUD) ====================
    
    def add_book(self, isbn: str, title: str, author: str, weight: float, 
                 value: float, stock: int = 1) -> bool:
        """
        Add a new book to the system.
        
        Args:
            isbn (str): ISBN of the book
            title (str): Title of the book
            author (str): Author of the book
            weight (float): Weight in kilograms
            value (float): Value in Colombian pesos
            stock (int, optional): Initial stock. Defaults to 1.
            
        Returns:
            bool: True if book was added, False if ISBN already exists
        """
        # Check if book already exists
        if binary_search(self.ordered_inventory, isbn) != -1:
            return False
        
        book = Book(isbn, title, author, weight, value, stock)
        
        # Add to general inventory (unordered)
        self.general_inventory.append(book)
        
        # Add to ordered inventory and maintain sort using insertion sort
        self.ordered_inventory.append(book)
        self.ordered_inventory = insertion_sort(self.ordered_inventory)
        
        return True
    
    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Get a book by ISBN using binary search.
        
        Args:
            isbn (str): ISBN to search for
            
        Returns:
            Optional[Book]: Book object if found, None otherwise
        """
        index = binary_search(self.ordered_inventory, isbn)
        if index != -1:
            return self.ordered_inventory[index]
        return None
    
    def search_books(self, query: str, search_by: str = 'title') -> List[Book]:
        """
        Search books by title or author using linear search.
        
        Args:
            query (str): Search query
            search_by (str, optional): 'title' or 'author'. Defaults to 'title'.
            
        Returns:
            List[Book]: List of matching books
        """
        return linear_search(self.general_inventory, query, search_by)
    
    def update_book(self, isbn: str, **kwargs) -> bool:
        """
        Update book information.
        
        Args:
            isbn (str): ISBN of the book to update
            **kwargs: Fields to update (title, author, weight, value, stock)
            
        Returns:
            bool: True if book was updated, False if not found
        """
        book = self.get_book_by_isbn(isbn)
        if not book:
            return False
        
        # Update fields
        if 'title' in kwargs:
            book.title = kwargs['title']
        if 'author' in kwargs:
            book.author = kwargs['author']
        if 'weight' in kwargs:
            book.weight = kwargs['weight']
        if 'value' in kwargs:
            book.value = kwargs['value']
        if 'stock' in kwargs:
            book.stock = kwargs['stock']
        
        # Re-sort ordered inventory
        self.ordered_inventory = insertion_sort(self.ordered_inventory)
        
        return True
    
    def delete_book(self, isbn: str) -> bool:
        """
        Delete a book from the system.
        
        Args:
            isbn (str): ISBN of the book to delete
            
        Returns:
            bool: True if book was deleted, False if not found
        """
        book = self.get_book_by_isbn(isbn)
        if not book:
            return False
        
        # Remove from both inventories
        self.general_inventory.remove(book)
        self.ordered_inventory.remove(book)
        
        # Remove reservations if any
        if isbn in self.reservations:
            del self.reservations[isbn]
        
        return True
    
    def list_all_books(self) -> List[Book]:
        """
        List all books in the general inventory.
        
        Returns:
            List[Book]: List of all books
        """
        return self.general_inventory.copy()
    
    # ==================== USER MANAGEMENT (CRUD) ====================
    
    def add_user(self, user_id: str, name: str, email: str, phone: str = "") -> bool:
        """
        Add a new user to the system.
        
        Args:
            user_id (str): Unique user identifier
            name (str): User's name
            email (str): User's email
            phone (str, optional): User's phone number
            
        Returns:
            bool: True if user was added, False if user_id already exists
        """
        if user_id in self.users:
            return False
        
        user = User(user_id, name, email, phone)
        self.users[user_id] = user
        
        # Initialize loan history stack for user
        if user_id not in self.loan_history:
            self.loan_history[user_id] = Stack()
        
        return True
    
    def get_user(self, user_id: str) -> Optional[User]:
        """
        Get a user by ID.
        
        Args:
            user_id (str): User identifier
            
        Returns:
            Optional[User]: User object if found, None otherwise
        """
        return self.users.get(user_id)
    
    def update_user(self, user_id: str, **kwargs) -> bool:
        """
        Update user information.
        
        Args:
            user_id (str): User identifier
            **kwargs: Fields to update (name, email, phone)
            
        Returns:
            bool: True if user was updated, False if not found
        """
        user = self.get_user(user_id)
        if not user:
            return False
        
        if 'name' in kwargs:
            user.name = kwargs['name']
        if 'email' in kwargs:
            user.email = kwargs['email']
        if 'phone' in kwargs:
            user.phone = kwargs['phone']
        
        return True
    
    def delete_user(self, user_id: str) -> bool:
        """
        Delete a user from the system.
        
        Args:
            user_id (str): User identifier
            
        Returns:
            bool: True if user was deleted, False if not found
        """
        if user_id not in self.users:
            return False
        
        del self.users[user_id]
        
        # Keep loan history but remove from active users
        if user_id in self.loan_history:
            # Optionally clear history: del self.loan_history[user_id]
            pass
        
        return True
    
    def list_all_users(self) -> List[User]:
        """
        List all users.
        
        Returns:
            List[User]: List of all users
        """
        return list(self.users.values())
    
    # ==================== SHELF MANAGEMENT (CRUD) ====================
    
    def add_shelf(self, shelf_id: str, capacity: float = 8.0) -> bool:
        """
        Add a new shelf to the system.
        
        Args:
            shelf_id (str): Unique shelf identifier
            capacity (float, optional): Weight capacity in kg. Defaults to 8.0.
            
        Returns:
            bool: True if shelf was added, False if shelf_id already exists
        """
        if shelf_id in self.shelves:
            return False
        
        shelf = Shelf(shelf_id, capacity)
        self.shelves[shelf_id] = shelf
        return True
    
    def get_shelf(self, shelf_id: str) -> Optional[Shelf]:
        """
        Get a shelf by ID.
        
        Args:
            shelf_id (str): Shelf identifier
            
        Returns:
            Optional[Shelf]: Shelf object if found, None otherwise
        """
        return self.shelves.get(shelf_id)
    
    def update_shelf(self, shelf_id: str, capacity: float = None) -> bool:
        """
        Update shelf information.
        
        Args:
            shelf_id (str): Shelf identifier
            capacity (float, optional): New capacity in kg
            
        Returns:
            bool: True if shelf was updated, False if not found
        """
        shelf = self.get_shelf(shelf_id)
        if not shelf:
            return False
        
        if capacity is not None:
            shelf.capacity = capacity
        
        return True
    
    def delete_shelf(self, shelf_id: str) -> bool:
        """
        Delete a shelf from the system.
        
        Args:
            shelf_id (str): Shelf identifier
            
        Returns:
            bool: True if shelf was deleted, False if not found
        """
        if shelf_id not in self.shelves:
            return False
        
        # Remove shelf_id from books on this shelf
        for book in self.general_inventory:
            if book.shelf_id == shelf_id:
                book.shelf_id = None
        
        del self.shelves[shelf_id]
        return True
    
    def list_all_shelves(self) -> List[Shelf]:
        """
        List all shelves.
        
        Returns:
            List[Shelf]: List of all shelves
        """
        return list(self.shelves.values())
    
    # ==================== LOAN MANAGEMENT ====================
    
    def loan_book(self, user_id: str, isbn: str) -> bool:
        """
        Loan a book to a user.
        
        Args:
            user_id (str): User identifier
            isbn (str): ISBN of the book to loan
            
        Returns:
            bool: True if loan was successful, False otherwise
        """
        # Check if user exists
        if user_id not in self.users:
            return False
        
        # Get book
        book = self.get_book_by_isbn(isbn)
        if not book or book.stock <= 0:
            return False
        
        # Decrease stock
        book.stock -= 1
        
        # Add to loan history (Stack - LIFO)
        if user_id not in self.loan_history:
            self.loan_history[user_id] = Stack()
        
        loan_record = {
            'isbn': isbn,
            'date': datetime.now().isoformat(),
            'title': book.title
        }
        self.loan_history[user_id].push(loan_record)
        
        return True
    
    def return_book(self, user_id: str, isbn: str) -> bool:
        """
        Return a book from a user.
        CRITICAL: Uses binary search to check for pending reservations.
        
        Args:
            user_id (str): User identifier
            isbn (str): ISBN of the book to return
            
        Returns:
            bool: True if return was successful, False otherwise
        """
        # Check if user exists and has loan history
        if user_id not in self.loan_history:
            return False
        
        # Find book using binary search (CRITICAL requirement)
        index = binary_search(self.ordered_inventory, isbn)
        if index == -1:
            return False
        
        book = self.ordered_inventory[index]
        
        # Increase stock
        book.stock += 1
        
        # Check for pending reservations (CRITICAL requirement)
        if isbn in self.reservations and not self.reservations[isbn].is_empty():
            # Assign to first person in queue (FIFO)
            reservation = self.reservations[isbn].dequeue()
            reserved_user_id = reservation['user_id']
            
            # Automatically loan to reserved user
            self.loan_book(reserved_user_id, isbn)
            print(f"Libro {isbn} asignado automáticamente al usuario reservado {reserved_user_id}")
        
        return True
    
    def get_user_loan_history(self, user_id: str) -> List[dict]:
        """
        Get loan history for a user (from stack).
        
        Args:
            user_id (str): User identifier
            
        Returns:
            List[dict]: List of loan records (most recent first - LIFO)
        """
        if user_id not in self.loan_history:
            return []
        
        # Convert stack to list (most recent at end)
        return self.loan_history[user_id].to_list()
    
    # ==================== RESERVATION MANAGEMENT ====================
    
    def reserve_book(self, user_id: str, isbn: str) -> bool:
        """
        Reserve a book (only if stock is zero).
        Uses Queue (FIFO) for waiting list.
        
        Args:
            user_id (str): User identifier
            isbn (str): ISBN of the book to reserve
            
        Returns:
            bool: True if reservation was successful, False otherwise
        """
        # Check if user exists
        if user_id not in self.users:
            return False
        
        # Get book
        book = self.get_book_by_isbn(isbn)
        if not book:
            return False
        
        # Only allow reservation if stock is zero
        if book.stock > 0:
            return False
        
        # Add to reservation queue (FIFO)
        if isbn not in self.reservations:
            self.reservations[isbn] = Queue()
        
        reservation = {
            'user_id': user_id,
            'isbn': isbn,
            'date': datetime.now().isoformat()
        }
        self.reservations[isbn].enqueue(reservation)
        
        return True
    
    def get_reservations(self, isbn: str) -> List[dict]:
        """
        Get reservations for a book.
        
        Args:
            isbn (str): ISBN of the book
            
        Returns:
            List[dict]: List of reservations (first in line first - FIFO)
        """
        if isbn not in self.reservations:
            return []
        
        return self.reservations[isbn].to_list()
    
    # ==================== SHELF MODULE ====================
    
    def find_risky_shelf_combinations(self, threshold: float = 8.0) -> List[Tuple]:
        """
        Find all combinations of 4 books that exceed weight threshold.
        Uses Brute Force algorithm.
        
        Args:
            threshold (float, optional): Weight threshold in kg. Defaults to 8.0.
            
        Returns:
            List[Tuple]: List of risky combinations
        """
        return find_risky_combinations(self.general_inventory, threshold)
    
    def find_optimal_shelf_assignment(self, max_capacity: float = 8.0) -> Tuple:
        """
        Find optimal book combination for a shelf.
        Uses Backtracking algorithm.
        
        Args:
            max_capacity (float, optional): Maximum weight capacity. Defaults to 8.0.
            
        Returns:
            Tuple: (optimal_books, total_value, total_weight)
        """
        return find_optimal_shelf(self.general_inventory, max_capacity)
    
    # ==================== RECURSION MODULE ====================
    
    def get_author_total_value(self, author: str) -> float:
        """
        Calculate total value of books by an author using Stack Recursion.
        
        Args:
            author (str): Author name
            
        Returns:
            float: Total value in Colombian pesos
        """
        return calculate_author_total_value(self.general_inventory, author)
    
    def get_author_average_weight(self, author: str) -> float:
        """
        Calculate average weight of books by an author using Tail Recursion.
        
        Args:
            author (str): Author name
            
        Returns:
            float: Average weight in kilograms
        """
        return calculate_author_average_weight(self.general_inventory, author)
    
    # ==================== REPORTS ====================
    
    def generate_global_inventory_report(self) -> str:
        """
        Generate global inventory report sorted by value using Merge Sort.
        
        Returns:
            str: Formatted report
        """
        # Sort by value using Merge Sort
        sorted_books = merge_sort(self.general_inventory, key=lambda x: x.value)
        
        report = "=" * 80 + "\n"
        report += "REPORTE GLOBAL DE INVENTARIO (Ordenado por Valor - COP)\n"
        report += "=" * 80 + "\n\n"
        report += f"{'ISBN':<15} {'Título':<30} {'Autor':<25} {'Valor (COP)':<15} {'Stock':<10}\n"
        report += "-" * 80 + "\n"
        
        total_value = 0
        for book in sorted_books:
            report += f"{book.isbn:<15} {book.title[:29]:<30} {book.author[:24]:<25} "
            report += f"${book.value:,.0f} {book.stock:<10}\n"
            total_value += book.value * book.stock
        
        report += "-" * 80 + "\n"
        report += f"Valor Total del Inventario: ${total_value:,.0f} COP\n"
        report += f"Total de Libros: {len(sorted_books)}\n"
        report += "=" * 80 + "\n"
        
        return report
    
    def save_global_report(self, filepath: str = "reports/global_inventory_report.txt") -> None:
        """
        Generate and save global inventory report to file.
        
        Args:
            filepath (str, optional): Path to save the report. Defaults to "reports/global_inventory_report.txt".
        """
        os.makedirs("reports", exist_ok=True)
        
        report = self.generate_global_inventory_report()
        save_report_to_file(report, filepath)
        print(f"Reporte guardado en {filepath}")

