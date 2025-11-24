"""
Recursive functions implementation.
Contains Stack Recursion and Tail Recursion examples.
"""


def calculate_author_total_value(books: list, author: str, index: int = 0) -> float:
    """
    Calculate the total value of all books by a specific author using Stack Recursion.
    This function uses the call stack to accumulate values recursively.
    
    Time Complexity: O(n) where n is the number of books
    Space Complexity: O(n) for recursion stack
    
    Args:
        books (list): List of Book objects
        author (str): Author name to filter by
        index (int, optional): Current index in the list. Defaults to 0.
        
    Returns:
        float: Total value of books by the author in Colombian pesos
    """
    # Base case: reached end of list
    if index >= len(books):
        return 0.0
    
    # Recursive case: check current book and add to total
    current_value = 0.0
    if books[index].author.lower() == author.lower():
        current_value = books[index].value
    
    # Recursive call: process next book and accumulate
    return current_value + calculate_author_total_value(books, author, index + 1)


def calculate_author_average_weight(books: list, author: str, index: int = 0, 
                                    total_weight: float = 0.0, count: int = 0) -> float:
    """
    Calculate the average weight of books by a specific author using Tail Recursion.
    This function demonstrates tail recursion by passing accumulated values as parameters.
    
    Time Complexity: O(n) where n is the number of books
    Space Complexity: O(n) for recursion stack (Python doesn't optimize tail recursion)
    
    Args:
        books (list): List of Book objects
        author (str): Author name to filter by
        index (int, optional): Current index in the list. Defaults to 0.
        total_weight (float, optional): Accumulated total weight. Defaults to 0.0.
        count (int, optional): Count of books by the author. Defaults to 0.
        
    Returns:
        float: Average weight of books by the author in kilograms
    """
    # Base case: reached end of list
    if index >= len(books):
        if count == 0:
            return 0.0
        average = total_weight / count
        print(f"Resultado de recursión de cola: Peso total = {total_weight:.2f} kg, "
              f"Conteo = {count}, Promedio = {average:.2f} kg")
        return average
    
    # Recursive case: update accumulators if book matches author
    current_weight = total_weight
    current_count = count
    
    if books[index].author.lower() == author.lower():
        current_weight += books[index].weight
        current_count += 1
        print(f"Procesando libro {index + 1}: '{books[index].title}' "
              f"(Peso: {books[index].weight:.2f} kg, "
              f"Acumulado: {current_weight:.2f} kg, Conteo: {current_count})")
    
    # Tail recursive call: pass accumulated values
    return calculate_author_average_weight(
        books, author, index + 1, current_weight, current_count
    )

