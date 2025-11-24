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
    Clase principal del Sistema de Gestión de Bibliotecas.
    
    Esta clase gestiona todos los aspectos del sistema:
    - Libros: Inventario general (desordenado) e inventario ordenado (por ISBN)
    - Usuarios: Registro y gestión de usuarios
    - Estanterías: Gestión de estanterías y asignación de libros
    - Préstamos: Historial usando Stack (Pila - LIFO)
    - Reservas: Lista de espera usando Queue (Cola - FIFO)
    """
    
    def __init__(self):
        """
        Inicializa el Sistema de Gestión de Bibliotecas.
        
        Crea todas las estructuras de datos necesarias:
        - Dos listas maestras de libros (requerimiento del proyecto)
        - Estructuras de datos: Stack para préstamos, Queue para reservas
        - Diccionarios para usuarios y estanterías
        """
        # REQUERIMIENTO: Dos listas maestras de libros
        self.general_inventory = []  # Lista desordenada (refleja el orden de carga)
        self.ordered_inventory = []  # Lista siempre ordenada por ISBN (ascendente)
        
        # Estructuras de datos requeridas
        self.loan_history = {}  # Dict[user_id, Stack] - Pila LIFO para historial de préstamos
        self.reservations = {}  # Dict[isbn, Queue] - Cola FIFO para reservas
        
        # Gestión adicional (CRUD requerido)
        self.users = {}  # Dict[user_id, User] - Almacena todos los usuarios
        self.shelves = {}  # Dict[shelf_id, Shelf] - Almacena todas las estanterías
        
        # Rutas de archivos para persistencia de datos
        self.books_file = "data/books.json"
        self.loan_history_file = "data/loan_history.json"
        self.reservations_file = "data/reservations.json"
    
    # ==================== ADQUISICIÓN DE DATOS ====================
    # REQUERIMIENTO: El sistema debe cargar inventario desde archivos CSV o JSON
    
    def load_initial_inventory(self, filepath: str, file_format: str = 'json') -> int:
        """
        Carga el inventario inicial desde un archivo CSV o JSON.
        
        REQUERIMIENTO: Debe leer archivos con al menos 5 atributos por libro:
        ISBN, Título, Autor, Peso (Kg), Valor (COP)
        
        Args:
            filepath (str): Ruta al archivo de datos
            file_format (str, optional): Formato del archivo ('csv' o 'json'). Defaults to 'json'.
            
        Returns:
            int: Número de libros cargados
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
    
    # ==================== GESTIÓN DE LIBROS (CRUD) ====================
    # REQUERIMIENTO: CRUD completo para libros (Create, Read, Update, Delete)
    
    def add_book(self, isbn: str, title: str, author: str, weight: float, 
                 value: float, stock: int = 1) -> bool:
        """
        Agrega un nuevo libro al sistema.
        
        REQUERIMIENTO: Usa Insertion Sort para mantener el Inventario Ordenado
        siempre ordenado por ISBN cada vez que se agrega un libro.
        
        Args:
            isbn (str): ISBN del libro
            title (str): Título del libro
            author (str): Autor del libro
            weight (float): Peso en kilogramos
            value (float): Valor en pesos colombianos (COP)
            stock (int, optional): Stock inicial. Defaults to 1.
            
        Returns:
            bool: True si el libro fue agregado, False si el ISBN ya existe
        """
        # Verificar si el libro ya existe usando Binary Search
        if binary_search(self.ordered_inventory, isbn) != -1:
            return False
        
        book = Book(isbn, title, author, weight, value, stock)
        
        # Agregar al inventario general (desordenado - refleja orden de carga)
        self.general_inventory.append(book)
        
        # REQUERIMIENTO: Agregar al inventario ordenado y mantener ordenado con Insertion Sort
        self.ordered_inventory.append(book)
        self.ordered_inventory = insertion_sort(self.ordered_inventory)
        
        return True
    
    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Obtiene un libro por ISBN usando búsqueda binaria.
        
        REQUERIMIENTO CRÍTICO: Binary Search se usa para verificar reservas
        cuando se devuelve un libro.
        
        Args:
            isbn (str): ISBN a buscar
            
        Returns:
            Optional[Book]: Objeto Book si se encuentra, None en caso contrario
        """
        index = binary_search(self.ordered_inventory, isbn)
        if index != -1:
            return self.ordered_inventory[index]
        return None
    
    def search_books(self, query: str, search_by: str = 'title') -> List[Book]:
        """
        Busca libros por título o autor usando búsqueda lineal.
        
        REQUERIMIENTO: Linear Search se usa en el Inventario General (desordenado)
        para buscar por Título o Autor.
        
        Args:
            query (str): Consulta de búsqueda
            search_by (str, optional): 'title' o 'author'. Defaults to 'title'.
            
        Returns:
            List[Book]: Lista de libros que coinciden
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
    
    # ==================== GESTIÓN DE PRÉSTAMOS ====================
    # REQUERIMIENTO: Historial de préstamos usando Stack (Pila - LIFO)
    
    def loan_book(self, user_id: str, isbn: str) -> bool:
        """
        Presta un libro a un usuario.
        
        REQUERIMIENTO: Al prestar un libro, se apila el ISBN y la fecha de préstamo
        en el historial del usuario usando Stack (LIFO - Last In, First Out).
        El historial se almacena en archivo y puede ser cargado posteriormente.
        
        Args:
            user_id (str): Identificador del usuario
            isbn (str): ISBN del libro a prestar
            
        Returns:
            bool: True si el préstamo fue exitoso, False en caso contrario
        """
        # Verificar si el usuario existe
        if user_id not in self.users:
            return False
        
        # Obtener el libro
        book = self.get_book_by_isbn(isbn)
        if not book or book.stock <= 0:
            return False
        
        # Disminuir el stock
        book.stock -= 1
        
        # REQUERIMIENTO: Agregar al historial usando Stack (Pila - LIFO)
        if user_id not in self.loan_history:
            self.loan_history[user_id] = Stack()
        
        loan_record = {
            'isbn': isbn,
            'date': datetime.now().isoformat(),
            'title': book.title
        }
        self.loan_history[user_id].push(loan_record)  # Push en la pila
        
        return True
    
    def return_book(self, user_id: str, isbn: str) -> bool:
        """
        Devuelve un libro de un usuario.
        
        REQUERIMIENTO CRÍTICO: Usa Binary Search para verificar si un libro devuelto
        tiene reservas pendientes en la Cola de Espera. Si es así, debe asignarse
        automáticamente a la persona que ha solicitado la reserva según la prioridad (FIFO).
        
        Args:
            user_id (str): Identificador del usuario
            isbn (str): ISBN del libro a devolver
            
        Returns:
            bool: True si la devolución fue exitosa, False en caso contrario
        """
        # Verificar si el usuario existe y tiene historial de préstamos
        if user_id not in self.loan_history:
            return False
        
        # REQUERIMIENTO CRÍTICO: Buscar libro usando Binary Search
        index = binary_search(self.ordered_inventory, isbn)
        if index == -1:
            return False
        
        book = self.ordered_inventory[index]
        
        # Aumentar el stock
        book.stock += 1
        
        # REQUERIMIENTO CRÍTICO: Verificar reservas pendientes usando Binary Search
        # Si hay reservas, asignar automáticamente según prioridad FIFO
        if isbn in self.reservations and not self.reservations[isbn].is_empty():
            # Asignar a la primera persona en la cola (FIFO - First In, First Out)
            reservation = self.reservations[isbn].dequeue()
            reserved_user_id = reservation['user_id']
            
            # Prestar automáticamente al usuario reservado
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
    
    # ==================== GESTIÓN DE RESERVAS ====================
    # REQUERIMIENTO: Lista de espera usando Queue (Cola - FIFO)
    
    def reserve_book(self, user_id: str, isbn: str) -> bool:
        """
        Reserva un libro (solo si el stock es cero).
        
        REQUERIMIENTO: Implementa la Lista de Espera para libros agotados como una Cola (FIFO).
        Solo se puede encolar un usuario para reserva si el libro tiene stock cero.
        Las solicitudes de reservas se almacenan en un archivo y pueden ser cargadas posteriormente.
        
        Args:
            user_id (str): Identificador del usuario
            isbn (str): ISBN del libro a reservar
            
        Returns:
            bool: True si la reserva fue exitosa, False en caso contrario
        """
        # Verificar si el usuario existe
        if user_id not in self.users:
            return False
        
        # Obtener el libro
        book = self.get_book_by_isbn(isbn)
        if not book:
            return False
        
        # REQUERIMIENTO: Solo permitir reserva si el stock es cero
        if book.stock > 0:
            return False
        
        # REQUERIMIENTO: Agregar a la cola de reservas (FIFO - First In, First Out)
        if isbn not in self.reservations:
            self.reservations[isbn] = Queue()
        
        reservation = {
            'user_id': user_id,
            'isbn': isbn,
            'date': datetime.now().isoformat()
        }
        self.reservations[isbn].enqueue(reservation)  # Encolar en la cola
        
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
    
    # ==================== MÓDULO DE ESTANTERÍA ====================
    # REQUERIMIENTO: Algoritmos de resolución de problemas (Fuerza Bruta y Backtracking)
    
    def find_risky_shelf_combinations(self, threshold: float = 8.0) -> List[Tuple]:
        """
        Encuentra todas las combinaciones de 4 libros que exceden el umbral de peso.
        
        REQUERIMIENTO: Fuerza Bruta (Estantería Deficiente)
        Implementa un algoritmo que encuentre y liste todas las combinaciones posibles
        de cuatro libros que, al sumar su peso en Kg, superen un umbral de "riesgo" de 8 Kg
        (que es lo máximo que soporta un estante de libros).
        El algoritmo debe explorar exhaustivamente todas las combinaciones.
        
        Args:
            threshold (float, optional): Umbral de peso en kg. Defaults to 8.0.
            
        Returns:
            List[Tuple]: Lista de combinaciones riesgosas
        """
        return find_risky_combinations(self.general_inventory, threshold)
    
    def find_optimal_shelf_assignment(self, max_capacity: float = 8.0) -> Tuple:
        """
        Encuentra la combinación óptima de libros para una estantería.
        
        REQUERIMIENTO: Backtracking (Estantería Óptima)
        Implementa un algoritmo que encuentre la combinación de libros que maximice
        el valor total (COP) sin exceder la capacidad máxima de peso (8 Kg) de un estante.
        El algoritmo debe demostrar la exploración y su ejecución.
        
        Args:
            max_capacity (float, optional): Capacidad máxima de peso. Defaults to 8.0.
            
        Returns:
            Tuple: (libros_óptimos, valor_total, peso_total)
        """
        return find_optimal_shelf(self.general_inventory, max_capacity)
    
    # ==================== MÓDULO DE RECURSIÓN ====================
    # REQUERIMIENTO: Recursión de Pila y Recursión de Cola
    
    def get_author_total_value(self, author: str) -> float:
        """
        Calcula el valor total de todos los libros de un autor específico.
        
        REQUERIMIENTO: Recursión de Pila
        Implementa una función recursiva que calcule el Valor Total de todos los libros
        de un autor específico usando recursión de pila (stack recursion).
        
        Args:
            author (str): Nombre del autor
            
        Returns:
            float: Valor total en pesos colombianos
        """
        return calculate_author_total_value(self.general_inventory, author)
    
    def get_author_average_weight(self, author: str) -> float:
        """
        Calcula el peso promedio de la colección de un autor.
        
        REQUERIMIENTO: Recursión de Cola
        Implementa una función recursiva que calcule el Peso Promedio de la colección
        de un autor, demostrando la lógica de la recursión de cola (tail recursion) por consola.
        
        Args:
            author (str): Nombre del autor
            
        Returns:
            float: Peso promedio en kilogramos
        """
        return calculate_author_average_weight(self.general_inventory, author)
    
    # ==================== REPORTES ====================
    # REQUERIMIENTO: Reporte Global ordenado por valor usando Merge Sort
    
    def generate_global_inventory_report(self) -> str:
        """
        Genera un reporte global de inventario ordenado por valor.
        
        REQUERIMIENTO: Ordenamiento por Mezcla (Merge Sort)
        Este algoritmo debe usarse para generar un Reporte Global de inventario,
        ordenado por el atributo Valor (COP). El reporte generado también debe
        poder almacenarse en un archivo.
        
        Returns:
            str: Reporte formateado
        """
        # REQUERIMIENTO: Ordenar por valor usando Merge Sort
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

