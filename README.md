# Library Management System (SGB)

A comprehensive Library Management System implemented in Python, demonstrating various data structures, algorithms, and programming techniques covered in the "Programming Techniques" course.

## Project Overview

This system manages a library's inventory, users, loans, reservations, and shelf assignments. It implements all required data structures (Lists, Stacks, Queues), sorting algorithms (Insertion Sort, Merge Sort), search algorithms (Linear Search, Binary Search), problem-solving algorithms (Brute Force, Backtracking), and recursive functions.

## Features

### Data Acquisition and Data Structures
- **Initial Data Loading**: Load inventory from CSV or JSON files (minimum 5 attributes: ISBN, Title, Author, Weight, Value)
- **General Inventory**: Unordered list reflecting the order of data loading
- **Ordered Inventory**: List always maintained in ascending order by ISBN using Insertion Sort
- **Loan History (Stack)**: LIFO structure storing loan history per user, persisted to files
- **Reservations (Queue)**: FIFO structure for waiting lists when books are out of stock, persisted to files

### Sorting Algorithms
- **Insertion Sort**: Maintains the Ordered Inventory sorted by ISBN whenever a new book is added
- **Merge Sort**: Generates Global Inventory Report sorted by value (COP), can be saved to file

### Search Algorithms
- **Linear Search**: Search by Title or Author in the General Inventory (unordered list)
- **Binary Search**: Search by ISBN in the Ordered Inventory (CRITICAL: used to verify reservations when books are returned)

### Shelf Module - Problem Solving Algorithms
- **Brute Force**: Finds all combinations of 4 books that exceed the 8 kg weight threshold
- **Backtracking**: Finds the optimal combination of books that maximizes value without exceeding 8 kg capacity

### Recursion
- **Stack Recursion**: Calculates the total value of all books by a specific author
- **Tail Recursion**: Calculates the average weight of books by a specific author (with execution trace)

### CRUD Operations
Complete Create, Read, Update, Delete operations for:
- Books
- Users
- Shelves
- Loans
- Reservations

## Project Structure

```
.
├── models/                  # Core data models
│   ├── __init__.py
│   ├── book.py             # Book class
│   ├── user.py             # User class
│   └── shelf.py            # Shelf class
├── data_structures/        # Data structure implementations
│   ├── __init__.py
│   ├── stack.py            # Stack (Pila) - LIFO
│   └── queue.py            # Queue (Cola) - FIFO
├── algorithms/             # Algorithm implementations
│   ├── __init__.py
│   ├── sorting.py          # Insertion Sort, Merge Sort
│   ├── searching.py        # Linear Search, Binary Search
│   ├── shelf_algorithms.py # Brute Force, Backtracking
│   └── recursion.py        # Stack & Tail Recursion
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── file_handler.py     # File I/O operations
├── data/                   # Data files
│   ├── initial_books.csv   # Initial inventory (CSV format)
│   ├── initial_books.json  # Initial inventory (JSON format)
│   ├── books.json          # Current inventory (auto-generated)
│   ├── loan_history.json   # Loan history (auto-generated)
│   └── reservations.json   # Reservations (auto-generated)
├── reports/                 # Generated reports
│   └── global_inventory_report.txt
├── library_manager.py      # Main library management class
├── main.py                 # Command-line interface
└── README.md               # This file
```

## Installation

1. **Requirements**: Python 3.7 or higher

2. **No external dependencies**: The project uses only Python standard library

3. **Clone or download** the project to your local machine

## Usage

### Running the System

```bash
python main.py
```

### Main Menu Options

1. **Load Initial Inventory**: Load books from CSV or JSON file
2. **Book Management (CRUD)**: Add, get, update, delete, and list books
3. **User Management (CRUD)**: Add, get, update, delete, and list users
4. **Shelf Management (CRUD)**: Add, get, update, delete, and list shelves
5. **Loan a Book**: Loan a book to a user (updates stock, adds to loan history stack)
6. **Return a Book**: Return a book (checks for reservations using binary search, auto-assigns if found)
7. **Reserve a Book**: Reserve a book when stock is zero (adds to reservation queue)
8. **Search Books**: Search by title or author using linear search
9. **View Loan History**: View user's loan history (from stack, most recent first)
10. **View Reservations**: View reservations for a book (from queue, first in line first)
11. **Shelf Module**: Find risky combinations (brute force) or optimal assignment (backtracking)
12. **Recursion Module**: Calculate author statistics using recursion
13. **Generate Global Inventory Report**: Generate report sorted by value using merge sort
14. **Save Data**: Save all data to files
15. **Load Data**: Load all data from files

### Example Workflow

1. **Start the system**: `python main.py`
2. **Load initial inventory**: Select option 1, enter `data/initial_books.csv` or `data/initial_books.json`
3. **Add a user**: Select option 3, then option 1 to add a new user
4. **Loan a book**: Select option 5, enter user ID and ISBN
5. **Search books**: Select option 8, enter search query
6. **Generate report**: Select option 13 to see global inventory report sorted by value

## Technical Details

### Data Structures

#### Stack (Pila) - LIFO
- Used for loan history per user
- Most recent loan is at the top
- Implemented in `data_structures/stack.py`

#### Queue (Cola) - FIFO
- Used for book reservations
- First person in line gets priority
- Implemented in `data_structures/queue.py`

### Algorithms

#### Insertion Sort
- **Purpose**: Maintain Ordered Inventory sorted by ISBN
- **Time Complexity**: O(n²) worst case, O(n) best case
- **Usage**: Called automatically when a new book is added
- **Location**: `algorithms/sorting.py`

#### Merge Sort
- **Purpose**: Generate Global Inventory Report sorted by value
- **Time Complexity**: O(n log n)
- **Usage**: Called when generating the global report
- **Location**: `algorithms/sorting.py`

#### Linear Search
- **Purpose**: Search by Title or Author in General Inventory
- **Time Complexity**: O(n)
- **Usage**: Search functionality in main menu
- **Location**: `algorithms/searching.py`

#### Binary Search
- **Purpose**: Search by ISBN in Ordered Inventory (CRITICAL)
- **Time Complexity**: O(log n)
- **Usage**: Used when returning books to check for reservations
- **Location**: `algorithms/searching.py`

#### Brute Force (Risky Combinations)
- **Purpose**: Find all combinations of 4 books exceeding 8 kg
- **Time Complexity**: O(n⁴)
- **Usage**: Shelf module option 1
- **Location**: `algorithms/shelf_algorithms.py`

#### Backtracking (Optimal Shelf)
- **Purpose**: Find optimal book combination maximizing value (≤8 kg)
- **Time Complexity**: O(2ⁿ) worst case
- **Usage**: Shelf module option 2
- **Location**: `algorithms/shelf_algorithms.py`

#### Stack Recursion
- **Purpose**: Calculate total value of books by author
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) for recursion stack
- **Location**: `algorithms/recursion.py`

#### Tail Recursion
- **Purpose**: Calculate average weight of books by author
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) for recursion stack (Python doesn't optimize tail recursion)
- **Location**: `algorithms/recursion.py`

## Data Persistence

All data is automatically saved to JSON files:
- `data/books.json`: Current book inventory
- `data/loan_history.json`: All loan histories (stacks)
- `data/reservations.json`: All reservations (queues)

Data is loaded automatically on startup if files exist.

## Object-Oriented Programming

The system is fully implemented using OOP principles:
- **Book Class**: Represents a book with ISBN, title, author, weight, value, stock
- **User Class**: Represents a user with ID, name, email, phone
- **Shelf Class**: Represents a shelf with ID, capacity, and book management
- **LibraryManager Class**: Main system class managing all operations
- **Stack Class**: LIFO data structure implementation
- **Queue Class**: FIFO data structure implementation

## Documentation

All code is fully documented following Python docstring standards:
- Module-level documentation
- Class documentation with attributes
- Method documentation with parameters and return types
- Algorithm complexity analysis

## Testing Recommendations

1. **Load initial inventory** from provided CSV/JSON files
2. **Add users** and test loan/return operations
3. **Test reservations** by setting book stock to 0, then returning
4. **Test search** functionality with various queries
5. **Test shelf algorithms** with different book combinations
6. **Test recursion** with different authors
7. **Generate reports** and verify sorting
8. **Save and load** data to verify persistence

## Requirements Compliance

✅ **Data Acquisition**: CSV/JSON loading with 5+ attributes  
✅ **Two Master Lists**: General (unordered) and Ordered (by ISBN)  
✅ **Stack (Pila)**: Loan history per user, LIFO, persisted  
✅ **Queue (Cola)**: Reservations, FIFO, persisted  
✅ **Insertion Sort**: Maintains Ordered Inventory  
✅ **Merge Sort**: Global report sorted by value  
✅ **Linear Search**: Search by Title/Author  
✅ **Binary Search**: Search by ISBN (CRITICAL for reservations)  
✅ **Brute Force**: Find risky 4-book combinations  
✅ **Backtracking**: Optimal shelf assignment  
✅ **Stack Recursion**: Author total value  
✅ **Tail Recursion**: Author average weight  
✅ **POO**: All classes properly implemented  
✅ **Modularity**: Code separated into modules  
✅ **Documentation**: Complete English documentation  
✅ **CRUD Operations**: Full CRUD for all entities  

## Author

Developed as part of the "Programming Techniques" course project.

## License

This project is for educational purposes.

