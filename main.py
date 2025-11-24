"""
Library Management System - Main Entry Point
Interactive command-line interface for the library system.
"""

from library_manager import LibraryManager
import os


def print_menu():
    """Print the main menu."""
    print("\n" + "=" * 80)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECAS (SGB)")
    print("=" * 80)
    print("1.  Cargar Inventario Inicial")
    print("2.  Gestión de Libros (CRUD)")
    print("3.  Gestión de Usuarios (CRUD)")
    print("4.  Gestión de Estanterías (CRUD)")
    print("5.  Prestar un Libro")
    print("6.  Devolver un Libro")
    print("7.  Reservar un Libro")
    print("8.  Buscar Libros")
    print("9.  Ver Historial de Préstamos")
    print("10. Ver Reservas")
    print("11. Módulo de Estantería (Combinaciones Riesgosas y Asignación Óptima)")
    print("12. Módulo de Recursión (Estadísticas por Autor)")
    print("13. Generar Reporte Global de Inventario")
    print("14. Guardar Datos")
    print("15. Cargar Datos")
    print("0.  Salir")
    print("=" * 80)


def book_management_menu(manager: LibraryManager):
    """Book CRUD operations menu."""
    while True:
        print("\n--- GESTIÓN DE LIBROS ---")
        print("1. Agregar Libro")
        print("2. Buscar Libro por ISBN")
        print("3. Actualizar Libro")
        print("4. Eliminar Libro")
        print("5. Listar Todos los Libros")
        print("0. Volver al Menú Principal")
        
        choice = input("\nSeleccione una opción: ").strip()
        
        if choice == '1':
            isbn = input("ISBN: ").strip()
            title = input("Título: ").strip()
            author = input("Autor: ").strip()
            try:
                weight = float(input("Peso (kg): ").strip())
                value = float(input("Valor (COP): ").strip())
                stock = int(input("Stock: ").strip() or "1")
                
                if manager.add_book(isbn, title, author, weight, value, stock):
                    print("¡Libro agregado exitosamente!")
                else:
                    print("Error: Ya existe un libro con este ISBN.")
            except ValueError:
                print("Error: Entrada inválida.")
        
        elif choice == '2':
            isbn = input("ISBN: ").strip()
            book = manager.get_book_by_isbn(isbn)
            if book:
                print(f"\n{book}")
                print(f"  Peso: {book.weight} kg")
                print(f"  Valor: ${book.value:,.0f} COP")
                print(f"  Stock: {book.stock}")
            else:
                print("Libro no encontrado.")
        
        elif choice == '3':
            isbn = input("ISBN: ").strip()
            print("Ingrese nuevos valores (presione Enter para omitir):")
            title = input("Título: ").strip() or None
            author = input("Autor: ").strip() or None
            weight = input("Peso (kg): ").strip() or None
            value = input("Valor (COP): ").strip() or None
            stock = input("Stock: ").strip() or None
            
            kwargs = {}
            if title:
                kwargs['title'] = title
            if author:
                kwargs['author'] = author
            if weight:
                kwargs['weight'] = float(weight)
            if value:
                kwargs['value'] = float(value)
            if stock:
                kwargs['stock'] = int(stock)
            
            if manager.update_book(isbn, **kwargs):
                print("¡Libro actualizado exitosamente!")
            else:
                print("Error: Libro no encontrado.")
        
        elif choice == '4':
            isbn = input("ISBN: ").strip()
            if manager.delete_book(isbn):
                print("¡Libro eliminado exitosamente!")
            else:
                print("Error: Libro no encontrado.")
        
        elif choice == '5':
            books = manager.list_all_books()
            print(f"\nTotal de libros: {len(books)}")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
        
        elif choice == '0':
            break


def user_management_menu(manager: LibraryManager):
    """User CRUD operations menu."""
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Listar Todos los Usuarios")
        print("0. Volver al Menú Principal")
        
        choice = input("\nSeleccione una opción: ").strip()
        
        if choice == '1':
            user_id = input("ID de Usuario: ").strip()
            name = input("Nombre: ").strip()
            email = input("Correo Electrónico: ").strip()
            phone = input("Teléfono (opcional): ").strip()
            
            if manager.add_user(user_id, name, email, phone):
                print("¡Usuario agregado exitosamente!")
            else:
                print("Error: Ya existe un usuario con este ID.")
        
        elif choice == '2':
            user_id = input("ID de Usuario: ").strip()
            user = manager.get_user(user_id)
            if user:
                print(f"\n{user}")
                print(f"  Correo: {user.email}")
                print(f"  Teléfono: {user.phone}")
            else:
                print("Usuario no encontrado.")
        
        elif choice == '3':
            user_id = input("ID de Usuario: ").strip()
            print("Ingrese nuevos valores (presione Enter para omitir):")
            name = input("Nombre: ").strip() or None
            email = input("Correo Electrónico: ").strip() or None
            phone = input("Teléfono: ").strip() or None
            
            kwargs = {}
            if name:
                kwargs['name'] = name
            if email:
                kwargs['email'] = email
            if phone:
                kwargs['phone'] = phone
            
            if manager.update_user(user_id, **kwargs):
                print("¡Usuario actualizado exitosamente!")
            else:
                print("Error: Usuario no encontrado.")
        
        elif choice == '4':
            user_id = input("ID de Usuario: ").strip()
            if manager.delete_user(user_id):
                print("¡Usuario eliminado exitosamente!")
            else:
                print("Error: Usuario no encontrado.")
        
        elif choice == '5':
            users = manager.list_all_users()
            print(f"\nTotal de usuarios: {len(users)}")
            for i, user in enumerate(users, 1):
                print(f"{i}. {user}")
        
        elif choice == '0':
            break


def shelf_management_menu(manager: LibraryManager):
    """Shelf CRUD operations menu."""
    while True:
        print("\n--- GESTIÓN DE ESTANTERÍAS ---")
        print("1. Agregar Estantería")
        print("2. Buscar Estantería")
        print("3. Actualizar Estantería")
        print("4. Eliminar Estantería")
        print("5. Listar Todas las Estanterías")
        print("0. Volver al Menú Principal")
        
        choice = input("\nSeleccione una opción: ").strip()
        
        if choice == '1':
            shelf_id = input("ID de Estantería: ").strip()
            try:
                capacity = float(input("Capacidad (kg, por defecto 8.0): ").strip() or "8.0")
                if manager.add_shelf(shelf_id, capacity):
                    print("¡Estantería agregada exitosamente!")
                else:
                    print("Error: Ya existe una estantería con este ID.")
            except ValueError:
                print("Error: Entrada inválida.")
        
        elif choice == '2':
            shelf_id = input("ID de Estantería: ").strip()
            shelf = manager.get_shelf(shelf_id)
            if shelf:
                print(f"\n{shelf}")
                print(f"  Peso Total: {shelf.get_total_weight():.2f} kg")
                print(f"  Valor Total: ${shelf.get_total_value():,.0f} COP")
                print(f"  Libros: {len(shelf.books)}")
            else:
                print("Estantería no encontrada.")
        
        elif choice == '3':
            shelf_id = input("ID de Estantería: ").strip()
            capacity = input("Nueva Capacidad (kg): ").strip() or None
            if capacity:
                try:
                    if manager.update_shelf(shelf_id, float(capacity)):
                        print("¡Estantería actualizada exitosamente!")
                    else:
                        print("Error: Estantería no encontrada.")
                except ValueError:
                    print("Error: Entrada inválida.")
        
        elif choice == '4':
            shelf_id = input("ID de Estantería: ").strip()
            if manager.delete_shelf(shelf_id):
                print("¡Estantería eliminada exitosamente!")
            else:
                print("Error: Estantería no encontrada.")
        
        elif choice == '5':
            shelves = manager.list_all_shelves()
            print(f"\nTotal de estanterías: {len(shelves)}")
            for i, shelf in enumerate(shelves, 1):
                print(f"{i}. {shelf}")
        
        elif choice == '0':
            break


def shelf_module_menu(manager: LibraryManager):
    """Shelf algorithms menu."""
    print("\n--- MÓDULO DE ESTANTERÍA ---")
    print("1. Encontrar Combinaciones Riesgosas (Fuerza Bruta)")
    print("2. Encontrar Asignación Óptima de Estantería (Backtracking)")
    
    choice = input("\nSeleccione una opción: ").strip()
    
    if choice == '1':
        try:
            threshold = float(input("Umbral de peso (kg, por defecto 8.0): ").strip() or "8.0")
            combinations = manager.find_risky_combinations(threshold)
            
            print(f"\nSe encontraron {len(combinations)} combinaciones riesgosas:")
            for i, combo in enumerate(combinations, 1):
                total_weight = sum(book.weight for book in combo)
                print(f"\n{i}. Combinación (Peso Total: {total_weight:.2f} kg):")
                for book in combo:
                    print(f"   - {book.title} ({book.weight:.2f} kg)")
        except ValueError:
            print("Error: Entrada inválida.")
    
    elif choice == '2':
        try:
            max_capacity = float(input("Capacidad máxima (kg, por defecto 8.0): ").strip() or "8.0")
            optimal, value, weight = manager.find_optimal_shelf_assignment(max_capacity)
            
            print(f"\nAsignación Óptima de Estantería:")
            print(f"  Valor Total: ${value:,.0f} COP")
            print(f"  Peso Total: {weight:.2f} kg")
            print(f"  Libros ({len(optimal)}):")
            for book in optimal:
                print(f"    - {book.title} (Peso: {book.weight:.2f} kg, Valor: ${book.value:,.0f} COP)")
        except ValueError:
            print("Error: Entrada inválida.")


def recursion_module_menu(manager: LibraryManager):
    """Recursion algorithms menu."""
    print("\n--- MÓDULO DE RECURSIÓN ---")
    author = input("Ingrese el nombre del autor: ").strip()
    
    if not author:
        print("Error: Se requiere el nombre del autor.")
        return
    
    print("\n1. Calcular Valor Total (Recursión de Pila)")
    print("2. Calcular Peso Promedio (Recursión de Cola)")
    choice = input("\nSeleccione una opción: ").strip()
    
    if choice == '1':
        total_value = manager.get_author_total_value(author)
        print(f"\nValor total de los libros de {author}: ${total_value:,.0f} COP")
    
    elif choice == '2':
        print("\nEjecución de Recursión de Cola:")
        avg_weight = manager.get_author_average_weight(author)
        print(f"\nPeso promedio de los libros de {author}: {avg_weight:.2f} kg")


def main():
    """Main function to run the library management system."""
    manager = LibraryManager()
    
    # Try to load existing data
    if os.path.exists("data"):
        try:
            manager.load_data()
        except:
            pass
    
    print("¡Bienvenido al Sistema de Gestión de Bibliotecas!")
    print("Cargando datos iniciales...")
    
    # Try to load initial inventory if it exists
    if os.path.exists("data/initial_books.csv"):
        try:
            count = manager.load_initial_inventory("data/initial_books.csv", "csv")
            print(f"Se cargaron {count} libros desde CSV.")
        except:
            pass
    elif os.path.exists("data/initial_books.json"):
        try:
            count = manager.load_initial_inventory("data/initial_books.json", "json")
            print(f"Se cargaron {count} libros desde JSON.")
        except:
            pass
    
    while True:
        print_menu()
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            filepath = input("Ingrese la ruta del archivo (CSV o JSON): ").strip()
            file_format = 'json' if filepath.endswith('.json') else 'csv'
            count = manager.load_initial_inventory(filepath, file_format)
            print(f"Se cargaron {count} libros.")
        
        elif choice == '2':
            book_management_menu(manager)
        
        elif choice == '3':
            user_management_menu(manager)
        
        elif choice == '4':
            shelf_management_menu(manager)
        
        elif choice == '5':
            user_id = input("ID de Usuario: ").strip()
            isbn = input("ISBN: ").strip()
            if manager.loan_book(user_id, isbn):
                print("¡Libro prestado exitosamente!")
            else:
                print("Error: No se pudo prestar el libro.")
        
        elif choice == '6':
            user_id = input("ID de Usuario: ").strip()
            isbn = input("ISBN: ").strip()
            if manager.return_book(user_id, isbn):
                print("¡Libro devuelto exitosamente!")
            else:
                print("Error: No se pudo devolver el libro.")
        
        elif choice == '7':
            user_id = input("ID de Usuario: ").strip()
            isbn = input("ISBN: ").strip()
            if manager.reserve_book(user_id, isbn):
                print("¡Libro reservado exitosamente!")
            else:
                print("Error: No se pudo reservar el libro (el libro debe tener stock = 0).")
        
        elif choice == '8':
            query = input("Consulta de búsqueda: ").strip()
            search_by = input("Buscar por (título/autor, por defecto: título): ").strip() or "title"
            results = manager.search_books(query, search_by)
            print(f"\nSe encontraron {len(results)} resultados:")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        
        elif choice == '9':
            user_id = input("ID de Usuario: ").strip()
            history = manager.get_user_loan_history(user_id)
            if history:
                print(f"\nHistorial de Préstamos para Usuario {user_id} (Más reciente primero):")
                for i, loan in enumerate(reversed(history), 1):
                    print(f"{i}. ISBN: {loan['isbn']}, Título: {loan.get('title', 'N/A')}, Fecha: {loan['date']}")
            else:
                print("No se encontró historial de préstamos.")
        
        elif choice == '10':
            isbn = input("ISBN: ").strip()
            reservations = manager.get_reservations(isbn)
            if reservations:
                print(f"\nReservas para ISBN {isbn} (Primero en la fila primero):")
                for i, res in enumerate(reservations, 1):
                    print(f"{i}. Usuario: {res['user_id']}, Fecha: {res['date']}")
            else:
                print("No se encontraron reservas.")
        
        elif choice == '11':
            shelf_module_menu(manager)
        
        elif choice == '12':
            recursion_module_menu(manager)
        
        elif choice == '13':
            report = manager.generate_global_inventory_report()
            print(report)
            save = input("\n¿Guardar reporte en archivo? (s/n): ").strip().lower()
            if save == 's' or save == 'y':
                manager.save_global_report()
        
        elif choice == '14':
            manager.save_data()
        
        elif choice == '15':
            manager.load_data()
        
        elif choice == '0':
            save = input("\n¿Guardar datos antes de salir? (s/n): ").strip().lower()
            if save == 's' or save == 'y':
                manager.save_data()
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor intente de nuevo.")


if __name__ == "__main__":
    main()

