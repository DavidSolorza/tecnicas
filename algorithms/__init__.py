"""
Algorithms package for Library Management System.
Contains sorting, searching, and problem-solving algorithms.
"""

from .sorting import insertion_sort, merge_sort
from .searching import linear_search, binary_search
from .shelf_algorithms import find_risky_combinations, find_optimal_shelf
from .recursion import calculate_author_total_value, calculate_author_average_weight

__all__ = [
    'insertion_sort',
    'merge_sort',
    'linear_search',
    'binary_search',
    'find_risky_combinations',
    'find_optimal_shelf',
    'calculate_author_total_value',
    'calculate_author_average_weight'
]

