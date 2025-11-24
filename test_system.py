"""
Quick test script to verify the Library Management System functionality.
Run this to test basic operations.
"""

from library_manager import LibraryManager


def test_system():
    """Test basic system functionality."""
    print("=" * 80)
    print("TESTING LIBRARY MANAGEMENT SYSTEM")
    print("=" * 80)
    
    manager = LibraryManager()
    
    # Test 1: Load initial inventory
    print("\n[TEST 1] Loading initial inventory...")
    try:
        count = manager.load_initial_inventory("data/initial_books.json", "json")
        print(f"✓ Loaded {count} books successfully")
    except Exception as e:
        print(f"✗ Error loading inventory: {e}")
        return
    
    # Test 2: Add user
    print("\n[TEST 2] Adding user...")
    if manager.add_user("U001", "John Doe", "john@example.com", "1234567890"):
        print("✓ User added successfully")
    else:
        print("✗ Failed to add user")
    
    # Test 3: Search books (Linear Search)
    print("\n[TEST 3] Searching books by author (Linear Search)...")
    results = manager.search_books("Orwell", "author")
    print(f"✓ Found {len(results)} books by George Orwell")
    for book in results:
        print(f"  - {book.title}")
    
    # Test 4: Get book by ISBN (Binary Search)
    print("\n[TEST 4] Getting book by ISBN (Binary Search)...")
    book = manager.get_book_by_isbn("978-0-345678-90-1")
    if book:
        print(f"✓ Found book: {book.title}")
    else:
        print("✗ Book not found")
    
    # Test 5: Loan a book
    print("\n[TEST 5] Loaning a book...")
    if manager.loan_book("U001", "978-0-345678-90-1"):
        print("✓ Book loaned successfully")
    else:
        print("✗ Failed to loan book")
    
    # Test 6: View loan history (Stack)
    print("\n[TEST 6] Viewing loan history (Stack - LIFO)...")
    history = manager.get_user_loan_history("U001")
    print(f"✓ Loan history has {len(history)} record(s)")
    for loan in reversed(history):
        print(f"  - {loan['title']} (ISBN: {loan['isbn']})")
    
    # Test 7: Reserve a book (Queue)
    print("\n[TEST 7] Reserving a book (Queue - FIFO)...")
    # First, set stock to 0
    manager.update_book("978-0-123456-78-9", stock=0)
    if manager.reserve_book("U001", "978-0-123456-78-9"):
        print("✓ Book reserved successfully")
    else:
        print("✗ Failed to reserve book")
    
    # Test 8: Generate Global Report (Merge Sort)
    print("\n[TEST 8] Generating Global Inventory Report (Merge Sort)...")
    report = manager.generate_global_inventory_report()
    print("✓ Report generated successfully")
    print("\nFirst 5 lines of report:")
    print("\n".join(report.split("\n")[:5]))
    
    # Test 9: Find risky combinations (Brute Force)
    print("\n[TEST 9] Finding risky combinations (Brute Force)...")
    risky = manager.find_risky_combinations(8.0)
    print(f"✓ Found {len(risky)} risky combinations of 4 books")
    if risky:
        combo = risky[0]
        total_weight = sum(b.weight for b in combo)
        print(f"  Example: Total weight = {total_weight:.2f} kg")
    
    # Test 10: Find optimal shelf (Backtracking)
    print("\n[TEST 10] Finding optimal shelf assignment (Backtracking)...")
    optimal, value, weight = manager.find_optimal_shelf_assignment(8.0)
    print(f"✓ Optimal assignment found:")
    print(f"  Books: {len(optimal)}, Value: ${value:,.0f} COP, Weight: {weight:.2f} kg")
    
    # Test 11: Recursion - Stack Recursion
    print("\n[TEST 11] Calculating author total value (Stack Recursion)...")
    total_value = manager.get_author_total_value("George Orwell")
    print(f"✓ Total value of George Orwell's books: ${total_value:,.0f} COP")
    
    # Test 12: Recursion - Tail Recursion
    print("\n[TEST 12] Calculating author average weight (Tail Recursion)...")
    avg_weight = manager.get_author_average_weight("George Orwell")
    print(f"✓ Average weight: {avg_weight:.2f} kg")
    
    # Test 13: Save data
    print("\n[TEST 13] Saving data...")
    try:
        manager.save_data()
        print("✓ Data saved successfully")
    except Exception as e:
        print(f"✗ Error saving data: {e}")
    
    print("\n" + "=" * 80)
    print("ALL TESTS COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    test_system()

