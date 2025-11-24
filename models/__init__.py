"""
Models package for Library Management System.
Contains core data classes: Book, User, Shelf.
"""

from .book import Book
from .user import User
from .shelf import Shelf

__all__ = ['Book', 'User', 'Shelf']

