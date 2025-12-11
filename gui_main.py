"""
Sistema de Gestión de Bibliotecas - Interfaz Gráfica
Interfaz gráfica moderna y profesional usando tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from library_manager import LibraryManager
import os


class LibraryGUI:
    """
    Clase principal para la interfaz gráfica del sistema de gestión de bibliotecas.
    """
    
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica.
        
        Args:
            root: Ventana principal de tkinter
        """
        self.root = root
        self.manager = LibraryManager()
        
        # Inicializar status_label como None para evitar errores
        self.status_label = None
        
        # Configurar la ventana principal
        self.root.title("Sistema de Gestión de Bibliotecas (SGB)")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Estilos modernos
        self.setup_styles()
        
        # Cargar datos al iniciar
        self.load_initial_data()
        
        # Crear la interfaz
        self.create_widgets()
        
        # Centrar ventana
        self.center_window()
    
    def setup_styles(self):
        """Configura los estilos modernos para la interfaz."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores modernos
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#3498db',
            'success': '#27ae60',
            'danger': '#e74c3c',
            'warning': '#f39c12',
            'info': '#3498db',
            'light': '#ecf0f1',
            'dark': '#34495e',
            'bg': '#f0f0f0'
        }
        
        # Configurar estilos de botones
        style.configure('Primary.TButton',
                       background=self.colors['secondary'],
                       foreground='white',
                       font=('Segoe UI', 10, 'bold'),
                       padding=10)
        style.map('Primary.TButton',
                 background=[('active', '#2980b9')])
        
        style.configure('Success.TButton',
                       background=self.colors['success'],
                       foreground='white',
                       font=('Segoe UI', 10, 'bold'),
                       padding=10)
        
        style.configure('Danger.TButton',
                       background=self.colors['danger'],
                       foreground='white',
                       font=('Segoe UI', 10, 'bold'),
                       padding=10)
        
        style.configure('Warning.TButton',
                       background=self.colors['warning'],
                       foreground='white',
                       font=('Segoe UI', 10, 'bold'),
                       padding=10)
        style.map('Warning.TButton',
                 background=[('active', '#e67e22')])
        
        # Configurar estilos de frames
        style.configure('Card.TFrame',
                       background='white',
                       relief='flat')
        
        # Configurar Treeview
        style.configure('Treeview',
                       font=('Segoe UI', 9),
                       rowheight=25)
        style.configure('Treeview.Heading',
                       font=('Segoe UI', 10, 'bold'),
                       background=self.colors['primary'],
                       foreground='white')
    
    def center_window(self):
        """Centra la ventana en la pantalla."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def load_initial_data(self):
        """Carga los datos iniciales del sistema."""
        # Intentar cargar datos guardados
        if os.path.exists("data"):
            try:
                self.manager.load_data()
            except:
                pass
        
        # Intentar cargar inventario inicial
        if os.path.exists("data/initial_books.json"):
            try:
                count = self.manager.load_initial_inventory("data/initial_books.json", "json")
                messagebox.showinfo("Éxito", f"Se cargaron {count} libros desde el archivo inicial.")
            except:
                pass
    
    def create_widgets(self):
        """Crea todos los widgets de la interfaz."""
        # Frame principal con padding
        main_frame = tk.Frame(self.root, bg=self.colors['bg'], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título principal
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            title_frame,
            text="📚 Sistema de Gestión de Bibliotecas",
            font=('Segoe UI', 24, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Gestión completa de libros, usuarios, préstamos y reservas",
            font=('Segoe UI', 11),
            bg=self.colors['bg'],
            fg=self.colors['dark']
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Notebook (pestañas) para organizar las secciones
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 0: Dashboard (Panel Principal)
        self.create_dashboard_tab(notebook)
        
        # Pestaña 1: Libros
        self.create_books_tab(notebook)
        
        # Pestaña 2: Usuarios
        self.create_users_tab(notebook)
        
        # Pestaña 3: Préstamos y Reservas
        self.create_loans_tab(notebook)
        
        # Pestaña 4: Búsqueda
        self.create_search_tab(notebook)
        
        # Pestaña 5: Módulos Avanzados
        self.create_advanced_tab(notebook)
        
        # Pestaña 6: Reportes
        self.create_reports_tab(notebook)
        
        # Barra de estado
        self.create_status_bar(main_frame)
    
    def create_dashboard_tab(self, notebook):
        """Crea la pestaña del dashboard con tarjetas de resumen."""
        # Inicializar la lista de tarjetas antes de crearlas
        self.dashboard_cards = []
        
        dashboard_frame = ttk.Frame(notebook)
        notebook.add(dashboard_frame, text="🏠 Dashboard")
        
        main_container = tk.Frame(dashboard_frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título del dashboard
        title_frame = tk.Frame(main_container, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            title_frame,
            text="Panel de Administración",
            font=('Segoe UI', 20, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        ).pack()
        
        # Frame para las tarjetas
        cards_frame = tk.Frame(main_container, bg=self.colors['bg'])
        cards_frame.pack(fill=tk.BOTH, expand=True)
        
        # Primera fila de tarjetas
        row1 = tk.Frame(cards_frame, bg=self.colors['bg'])
        row1.pack(fill=tk.X, pady=10)
        
        # Tarjeta 1: Usuarios
        self.create_stat_card(row1, "USUARIOS", "👥", self.get_user_count, '#27ae60', 0)
        
        # Tarjeta 2: Libros
        self.create_stat_card(row1, "LIBROS", "📚", self.get_book_count, '#3498db', 1)
        
        # Tarjeta 3: Autores
        self.create_stat_card(row1, "AUTORES", "✍️", self.get_author_count, '#f39c12', 2)
        
        # Tarjeta 4: Estanterías
        self.create_stat_card(row1, "ESTANTERÍAS", "📦", self.get_shelf_count, '#e74c3c', 3)
        
        # Segunda fila de tarjetas
        row2 = tk.Frame(cards_frame, bg=self.colors['bg'])
        row2.pack(fill=tk.X, pady=10)
        
        # Tarjeta 5: Préstamos Activos
        self.create_stat_card(row2, "PRÉSTAMOS", "📤", self.get_active_loans_count, '#e74c3c', 0)
        
        # Tarjeta 6: Reservas
        self.create_stat_card(row2, "RESERVAS", "🔖", self.get_reservations_count, '#9b59b6', 1)
        
        # Tarjeta 7: Stock Total
        self.create_stat_card(row2, "STOCK TOTAL", "📊", self.get_total_stock, '#16a085', 2)
        
        # Tarjeta 8: Valor Inventario
        self.create_stat_card(row2, "VALOR INVENTARIO", "💰", self.get_inventory_value, '#27ae60', 3)
        
        # Botón para refrescar
        refresh_btn = ttk.Button(
            main_container,
            text="🔄 Actualizar Estadísticas",
            style='Primary.TButton',
            command=self.refresh_dashboard
        )
        refresh_btn.pack(pady=20)
        
        # Inicializar dashboard después de crear todas las tarjetas
        self.root.after(100, self.refresh_dashboard)
    
    def create_stat_card(self, parent, title, icon, count_func, color, column):
        """Crea una tarjeta de estadística."""
        card = tk.Frame(
            parent,
            bg='white',
            relief=tk.RAISED,
            bd=2,
            width=200,
            height=150
        )
        card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        card.pack_propagate(False)
        
        # Fondo de color en la parte superior
        color_bar = tk.Frame(card, bg=color, height=5)
        color_bar.pack(fill=tk.X)
        
        # Contenido de la tarjeta
        content = tk.Frame(card, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Icono y título
        icon_label = tk.Label(
            content,
            text=icon,
            font=('Segoe UI', 32),
            bg='white',
            fg=color
        )
        icon_label.pack(pady=(10, 5))
        
        title_label = tk.Label(
            content,
            text=title,
            font=('Segoe UI', 11, 'bold'),
            bg='white',
            fg=self.colors['dark']
        )
        title_label.pack()
        
        # Contador
        count_label = tk.Label(
            content,
            text="0",
            font=('Segoe UI', 24, 'bold'),
            bg='white',
            fg=color
        )
        count_label.pack(pady=5)
        
        # Guardar referencia para actualizar
        card.count_label = count_label
        card.count_func = count_func
        self.dashboard_cards.append(card)
    
    def get_user_count(self):
        """Obtiene el número de usuarios."""
        return len(self.manager.list_all_users())
    
    def get_book_count(self):
        """Obtiene el número de libros."""
        return len(self.manager.list_all_books())
    
    def get_author_count(self):
        """Obtiene el número de autores únicos."""
        books = self.manager.list_all_books()
        authors = set(book.author.lower() for book in books)
        return len(authors)
    
    def get_shelf_count(self):
        """Obtiene el número de estanterías."""
        return len(self.manager.list_all_shelves())
    
    def get_active_loans_count(self):
        """Obtiene el número de préstamos activos."""
        total = 0
        # Acceder directamente a loan_history del manager
        if hasattr(self.manager, 'loan_history'):
            for user_id in self.manager.loan_history:
                history = self.manager.get_user_loan_history(user_id)
                # Contar préstamos que no han sido devueltos (simplificado)
                # En un sistema real, necesitarías rastrear qué préstamos están activos
                total += len(history)
        return total
    
    def get_reservations_count(self):
        """Obtiene el número total de reservas."""
        total = 0
        # Acceder directamente a reservations del manager
        if hasattr(self.manager, 'reservations'):
            for isbn in self.manager.reservations:
                reservations = self.manager.get_reservations(isbn)
                total += len(reservations)
        return total
    
    def get_total_stock(self):
        """Obtiene el stock total de libros."""
        books = self.manager.list_all_books()
        return sum(book.stock for book in books)
    
    def get_inventory_value(self):
        """Obtiene el valor total del inventario."""
        books = self.manager.list_all_books()
        total = sum(book.value * book.stock for book in books)
        # Retornar número para que se formatee en la tarjeta
        return total
    
    def refresh_dashboard(self):
        """Actualiza todas las tarjetas del dashboard."""
        if not hasattr(self, 'dashboard_cards'):
            return
            
        for card in self.dashboard_cards:
            try:
                count = card.count_func()
                # Formatear según el tipo
                if isinstance(count, (int, float)):
                    if count >= 1000000:
                        text = f"${count/1000000:.1f}M"
                    elif count >= 1000:
                        text = f"${count/1000:.1f}K"
                    else:
                        text = str(count)
                else:
                    text = str(count)
                card.count_label.config(text=text)
            except Exception as e:
                card.count_label.config(text="Error")
        
        # También actualizar la barra de estado
        self.update_status()
    
    def create_books_tab(self, notebook):
        """Crea la pestaña de gestión de libros."""
        books_frame = ttk.Frame(notebook)
        notebook.add(books_frame, text="📖 Libros")
        
        # Frame principal con scroll
        main_container = tk.Frame(books_frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo - Formulario
        left_panel = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10), expand=False, ipadx=20, ipady=20)
        left_panel.config(width=350)
        
        tk.Label(
            left_panel,
            text="Gestión de Libros",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 20))
        
        # Formulario
        form_frame = tk.Frame(left_panel, bg='white')
        form_frame.pack(fill=tk.X)
        
        # ISBN
        tk.Label(form_frame, text="ISBN:", bg='white', font=('Segoe UI', 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.isbn_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.isbn_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Título
        tk.Label(form_frame, text="Título:", bg='white', font=('Segoe UI', 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.title_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.title_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Autor
        tk.Label(form_frame, text="Autor:", bg='white', font=('Segoe UI', 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.author_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.author_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Peso
        tk.Label(form_frame, text="Peso (kg):", bg='white', font=('Segoe UI', 10)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.weight_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.weight_entry.grid(row=3, column=1, pady=5, padx=10)
        
        # Valor
        tk.Label(form_frame, text="Valor (COP):", bg='white', font=('Segoe UI', 10)).grid(row=4, column=0, sticky=tk.W, pady=5)
        self.value_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.value_entry.grid(row=4, column=1, pady=5, padx=10)
        
        # Stock
        tk.Label(form_frame, text="Stock:", bg='white', font=('Segoe UI', 10)).grid(row=5, column=0, sticky=tk.W, pady=5)
        self.stock_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.stock_entry.insert(0, "1")
        self.stock_entry.grid(row=5, column=1, pady=5, padx=10)
        
        # Botones
        btn_frame = tk.Frame(left_panel, bg='white')
        btn_frame.pack(pady=20)
        
        ttk.Button(
            btn_frame,
            text="➕ Agregar",
            style='Success.TButton',
            command=self.add_book
        ).pack(pady=5, fill=tk.X)
        
        ttk.Button(
            btn_frame,
            text="🔍 Buscar por ISBN",
            style='Primary.TButton',
            command=self.search_book_by_isbn
        ).pack(pady=5, fill=tk.X)
        
        ttk.Button(
            btn_frame,
            text="✏️ Actualizar",
            style='Primary.TButton',
            command=self.update_book
        ).pack(pady=5, fill=tk.X)
        
        ttk.Button(
            btn_frame,
            text="🗑️ Eliminar",
            style='Danger.TButton',
            command=self.delete_book
        ).pack(pady=5, fill=tk.X)
        
        # Panel derecho - Lista de libros
        right_panel = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)
        
        tk.Label(
            right_panel,
            text="Inventario de Libros",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 10))
        
        # Treeview para mostrar libros
        columns = ('ISBN', 'Título', 'Autor', 'Peso', 'Valor', 'Stock')
        self.books_tree = ttk.Treeview(right_panel, columns=columns, show='headings', height=20)
        
        for col in columns:
            self.books_tree.heading(col, text=col)
            self.books_tree.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(right_panel, orient=tk.VERTICAL, command=self.books_tree.yview)
        self.books_tree.configure(yscrollcommand=scrollbar.set)
        
        self.books_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botón para refrescar lista
        ttk.Button(
            right_panel,
            text="🔄 Refrescar Lista",
            style='Primary.TButton',
            command=self.refresh_books_list
        ).pack(pady=10)
        
        # Cargar lista inicial
        self.refresh_books_list()
    
    def create_users_tab(self, notebook):
        """Crea la pestaña de gestión de usuarios."""
        users_frame = ttk.Frame(notebook)
        notebook.add(users_frame, text="👥 Usuarios")
        
        main_container = tk.Frame(users_frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo - Formulario
        left_panel = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10), expand=False, ipadx=20, ipady=20)
        left_panel.config(width=350)
        
        tk.Label(
            left_panel,
            text="Gestión de Usuarios",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 20))
        
        form_frame = tk.Frame(left_panel, bg='white')
        form_frame.pack(fill=tk.X)
        
        # ID Usuario
        tk.Label(form_frame, text="ID Usuario:", bg='white', font=('Segoe UI', 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.user_id_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.user_id_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Nombre
        tk.Label(form_frame, text="Nombre:", bg='white', font=('Segoe UI', 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.user_name_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.user_name_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Email
        tk.Label(form_frame, text="Email:", bg='white', font=('Segoe UI', 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.user_email_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.user_email_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Teléfono
        tk.Label(form_frame, text="Teléfono:", bg='white', font=('Segoe UI', 10)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.user_phone_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.user_phone_entry.grid(row=3, column=1, pady=5, padx=10)
        
        btn_frame = tk.Frame(left_panel, bg='white')
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="➕ Agregar", style='Success.TButton', command=self.add_user).pack(pady=5, fill=tk.X)
        ttk.Button(btn_frame, text="🔍 Buscar", style='Primary.TButton', command=self.search_user).pack(pady=5, fill=tk.X)
        ttk.Button(btn_frame, text="✏️ Actualizar", style='Primary.TButton', command=self.update_user).pack(pady=5, fill=tk.X)
        ttk.Button(btn_frame, text="🗑️ Eliminar", style='Danger.TButton', command=self.delete_user).pack(pady=5, fill=tk.X)
        
        # Panel derecho - Lista
        right_panel = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)
        
        tk.Label(
            right_panel,
            text="Lista de Usuarios",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 10))
        
        columns = ('ID', 'Nombre', 'Email', 'Teléfono')
        self.users_tree = ttk.Treeview(right_panel, columns=columns, show='headings', height=20)
        
        for col in columns:
            self.users_tree.heading(col, text=col)
            self.users_tree.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(right_panel, orient=tk.VERTICAL, command=self.users_tree.yview)
        self.users_tree.configure(yscrollcommand=scrollbar.set)
        
        self.users_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        ttk.Button(
            right_panel,
            text="🔄 Refrescar Lista",
            style='Primary.TButton',
            command=self.refresh_users_list
        ).pack(pady=10)
        
        self.refresh_users_list()
    
    def create_loans_tab(self, notebook):
        """Crea la pestaña de préstamos y reservas."""
        loans_frame = ttk.Frame(notebook)
        notebook.add(loans_frame, text="📋 Préstamos")
        
        main_container = tk.Frame(loans_frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Sección de préstamos
        loans_card = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        loans_card.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=20, ipady=20)
        
        tk.Label(
            loans_card,
            text="Gestión de Préstamos y Reservas",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 20))
        
        # Formulario de préstamo
        form_frame = tk.Frame(loans_card, bg='white')
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="ID Usuario:", bg='white', font=('Segoe UI', 10)).grid(row=0, column=0, sticky=tk.W, pady=5, padx=10)
        self.loan_user_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.loan_user_entry.grid(row=0, column=1, pady=5, padx=10)
        
        tk.Label(form_frame, text="ISBN:", bg='white', font=('Segoe UI', 10)).grid(row=1, column=0, sticky=tk.W, pady=5, padx=10)
        self.loan_isbn_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.loan_isbn_entry.grid(row=1, column=1, pady=5, padx=10)
        
        btn_frame = tk.Frame(loans_card, bg='white')
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="📤 Prestar Libro", style='Success.TButton', command=self.loan_book).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📥 Devolver Libro", style='Primary.TButton', command=self.return_book).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🔖 Reservar Libro", style='Primary.TButton', command=self.reserve_book).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📜 Ver Historial", style='Primary.TButton', command=self.view_loan_history).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📋 Ver Reservas", style='Primary.TButton', command=self.view_reservations).pack(side=tk.LEFT, padx=5)
    
    def create_search_tab(self, notebook):
        """Crea la pestaña de búsqueda."""
        search_frame = ttk.Frame(notebook)
        notebook.add(search_frame, text="🔍 Búsqueda")
        
        main_container = tk.Frame(search_frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        search_card = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        search_card.pack(fill=tk.BOTH, expand=True, ipadx=20, ipady=20)
        
        tk.Label(
            search_card,
            text="Búsqueda de Libros",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 20))
        
        form_frame = tk.Frame(search_card, bg='white')
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Consulta:", bg='white', font=('Segoe UI', 10)).grid(row=0, column=0, sticky=tk.W, pady=5, padx=10)
        self.search_query_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=30)
        self.search_query_entry.grid(row=0, column=1, pady=5, padx=10)
        
        tk.Label(form_frame, text="Buscar por:", bg='white', font=('Segoe UI', 10)).grid(row=1, column=0, sticky=tk.W, pady=5, padx=10)
        self.search_by_var = tk.StringVar(value="title")
        tk.Radiobutton(form_frame, text="Título", variable=self.search_by_var, value="title", bg='white', font=('Segoe UI', 10)).grid(row=1, column=1, sticky=tk.W, padx=10)
        tk.Radiobutton(form_frame, text="Autor", variable=self.search_by_var, value="author", bg='white', font=('Segoe UI', 10)).grid(row=1, column=2, sticky=tk.W, padx=10)
        
        ttk.Button(form_frame, text="🔍 Buscar", style='Primary.TButton', command=self.search_books).grid(row=2, column=1, pady=20)
        
        # Resultados
        results_frame = tk.Frame(search_card, bg='white')
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        columns = ('ISBN', 'Título', 'Autor', 'Peso', 'Valor', 'Stock')
        self.search_tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.search_tree.heading(col, text=col)
            self.search_tree.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.search_tree.yview)
        self.search_tree.configure(yscrollcommand=scrollbar.set)
        
        self.search_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_advanced_tab(self, notebook):
        """Crea la pestaña de módulos avanzados."""
        advanced_frame = ttk.Frame(notebook)
        notebook.add(advanced_frame, text="⚙️ Avanzado")
        
        main_container = tk.Frame(advanced_frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Módulo de Estantería
        shelf_card = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        shelf_card.pack(fill=tk.BOTH, expand=True, padx=10, pady=5, ipadx=20, ipady=20)
        
        tk.Label(
            shelf_card,
            text="Módulo de Estantería",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 10))
        
        ttk.Button(shelf_card, text="🔍 Combinaciones Riesgosas (Fuerza Bruta)", style='Warning.TButton', command=self.find_risky_combinations).pack(pady=5, fill=tk.X, padx=20)
        ttk.Button(shelf_card, text="✨ Asignación Óptima (Backtracking)", style='Success.TButton', command=self.find_optimal_shelf).pack(pady=5, fill=tk.X, padx=20)
        
        # Módulo de Recursión
        recursion_card = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        recursion_card.pack(fill=tk.BOTH, expand=True, padx=10, pady=5, ipadx=20, ipady=20)
        
        tk.Label(
            recursion_card,
            text="Módulo de Recursión",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 10))
        
        form_frame = tk.Frame(recursion_card, bg='white')
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Autor:", bg='white', font=('Segoe UI', 10)).grid(row=0, column=0, sticky=tk.W, pady=5, padx=10)
        self.recursion_author_entry = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.recursion_author_entry.grid(row=0, column=1, pady=5, padx=10)
        
        btn_frame = tk.Frame(recursion_card, bg='white')
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="💰 Valor Total (Recursión Pila)", style='Primary.TButton', command=self.calculate_total_value).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="⚖️ Peso Promedio (Recursión Cola)", style='Primary.TButton', command=self.calculate_avg_weight).pack(side=tk.LEFT, padx=5)
    
    def create_reports_tab(self, notebook):
        """Crea la pestaña de reportes."""
        reports_frame = ttk.Frame(notebook)
        notebook.add(reports_frame, text="📊 Reportes")
        
        main_container = tk.Frame(reports_frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        reports_card = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        reports_card.pack(fill=tk.BOTH, expand=True, ipadx=20, ipady=20)
        
        tk.Label(
            reports_card,
            text="Reportes del Sistema",
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg=self.colors['primary']
        ).pack(pady=(0, 20))
        
        ttk.Button(
            reports_card,
            text="📊 Generar Reporte Global (Merge Sort)",
            style='Primary.TButton',
            command=self.generate_report
        ).pack(pady=10, fill=tk.X, padx=20)
        
        # Área de texto para mostrar reporte
        self.report_text = scrolledtext.ScrolledText(
            reports_card,
            font=('Consolas', 10),
            wrap=tk.WORD,
            height=20
        )
        self.report_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    def create_status_bar(self, parent):
        """Crea la barra de estado."""
        status_frame = tk.Frame(parent, bg=self.colors['dark'], height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = tk.Label(
            status_frame,
            text="Sistema listo | Total de libros: 0",
            bg=self.colors['dark'],
            fg='white',
            font=('Segoe UI', 9),
            anchor=tk.W,
            padx=10
        )
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(
            status_frame,
            text="💾 Guardar",
            command=self.save_data
        ).pack(side=tk.RIGHT, padx=5)
        
        self.update_status()
    
    # Métodos de funcionalidad
    def refresh_books_list(self):
        """Actualiza la lista de libros."""
        for item in self.books_tree.get_children():
            self.books_tree.delete(item)
        
        books = self.manager.list_all_books()
        for book in books:
            self.books_tree.insert('', tk.END, values=(
                book.isbn, book.title, book.author,
                f"{book.weight:.2f} kg", f"${book.value:,.0f}", book.stock
            ))
        
        self.update_status()
    
    def refresh_users_list(self):
        """Actualiza la lista de usuarios."""
        for item in self.users_tree.get_children():
            self.users_tree.delete(item)
        
        users = self.manager.list_all_users()
        for user in users:
            self.users_tree.insert('', tk.END, values=(
                user.user_id, user.name, user.email, user.phone
            ))
    
    def add_book(self):
        """Agrega un libro."""
        try:
            isbn = self.isbn_entry.get().strip()
            title = self.title_entry.get().strip()
            author = self.author_entry.get().strip()
            weight = float(self.weight_entry.get().strip())
            value = float(self.value_entry.get().strip())
            stock = int(self.stock_entry.get().strip() or "1")
            
            if self.manager.add_book(isbn, title, author, weight, value, stock):
                messagebox.showinfo("Éxito", "Libro agregado exitosamente.")
                self.clear_book_form()
                self.refresh_books_list()
                self.refresh_dashboard()
            else:
                messagebox.showerror("Error", "Ya existe un libro con este ISBN.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar libro: {str(e)}")
    
    def search_book_by_isbn(self):
        """Busca un libro por ISBN."""
        isbn = self.isbn_entry.get().strip()
        if not isbn:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ISBN.")
            return
        
        book = self.manager.get_book_by_isbn(isbn)
        if book:
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, book.title)
            self.author_entry.delete(0, tk.END)
            self.author_entry.insert(0, book.author)
            self.weight_entry.delete(0, tk.END)
            self.weight_entry.insert(0, str(book.weight))
            self.value_entry.delete(0, tk.END)
            self.value_entry.insert(0, str(book.value))
            self.stock_entry.delete(0, tk.END)
            self.stock_entry.insert(0, str(book.stock))
            messagebox.showinfo("Éxito", f"Libro encontrado: {book.title}")
        else:
            messagebox.showwarning("No encontrado", "No se encontró un libro con ese ISBN.")
    
    def update_book(self):
        """Actualiza un libro."""
        isbn = self.isbn_entry.get().strip()
        if not isbn:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ISBN.")
            return
        
        try:
            kwargs = {}
            if self.title_entry.get().strip():
                kwargs['title'] = self.title_entry.get().strip()
            if self.author_entry.get().strip():
                kwargs['author'] = self.author_entry.get().strip()
            if self.weight_entry.get().strip():
                kwargs['weight'] = float(self.weight_entry.get().strip())
            if self.value_entry.get().strip():
                kwargs['value'] = float(self.value_entry.get().strip())
            if self.stock_entry.get().strip():
                kwargs['stock'] = int(self.stock_entry.get().strip())
            
            if self.manager.update_book(isbn, **kwargs):
                messagebox.showinfo("Éxito", "Libro actualizado exitosamente.")
                self.clear_book_form()
                self.refresh_books_list()
                self.refresh_dashboard()
            else:
                messagebox.showerror("Error", "Libro no encontrado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar: {str(e)}")
    
    def delete_book(self):
        """Elimina un libro."""
        isbn = self.isbn_entry.get().strip()
        if not isbn:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ISBN.")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el libro con ISBN {isbn}?"):
            if self.manager.delete_book(isbn):
                messagebox.showinfo("Éxito", "Libro eliminado exitosamente.")
                self.clear_book_form()
                self.refresh_books_list()
                self.refresh_dashboard()
            else:
                messagebox.showerror("Error", "Libro no encontrado.")
    
    def clear_book_form(self):
        """Limpia el formulario de libros."""
        self.isbn_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.stock_entry.insert(0, "1")
    
    def add_user(self):
        """Agrega un usuario."""
        try:
            user_id = self.user_id_entry.get().strip()
            name = self.user_name_entry.get().strip()
            email = self.user_email_entry.get().strip()
            phone = self.user_phone_entry.get().strip()
            
            if self.manager.add_user(user_id, name, email, phone):
                messagebox.showinfo("Éxito", "Usuario agregado exitosamente.")
                self.clear_user_form()
                self.refresh_users_list()
                self.refresh_dashboard()
            else:
                messagebox.showerror("Error", "Ya existe un usuario con este ID.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar usuario: {str(e)}")
    
    def search_user(self):
        """Busca un usuario."""
        user_id = self.user_id_entry.get().strip()
        if not user_id:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de usuario.")
            return
        
        user = self.manager.get_user(user_id)
        if user:
            self.user_name_entry.delete(0, tk.END)
            self.user_name_entry.insert(0, user.name)
            self.user_email_entry.delete(0, tk.END)
            self.user_email_entry.insert(0, user.email)
            self.user_phone_entry.delete(0, tk.END)
            self.user_phone_entry.insert(0, user.phone)
            messagebox.showinfo("Éxito", f"Usuario encontrado: {user.name}")
        else:
            messagebox.showwarning("No encontrado", "No se encontró un usuario con ese ID.")
    
    def update_user(self):
        """Actualiza un usuario."""
        user_id = self.user_id_entry.get().strip()
        if not user_id:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de usuario.")
            return
        
        try:
            kwargs = {}
            if self.user_name_entry.get().strip():
                kwargs['name'] = self.user_name_entry.get().strip()
            if self.user_email_entry.get().strip():
                kwargs['email'] = self.user_email_entry.get().strip()
            if self.user_phone_entry.get().strip():
                kwargs['phone'] = self.user_phone_entry.get().strip()
            
            if self.manager.update_user(user_id, **kwargs):
                messagebox.showinfo("Éxito", "Usuario actualizado exitosamente.")
                self.clear_user_form()
                self.refresh_users_list()
                self.refresh_dashboard()
            else:
                messagebox.showerror("Error", "Usuario no encontrado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar: {str(e)}")
    
    def delete_user(self):
        """Elimina un usuario."""
        user_id = self.user_id_entry.get().strip()
        if not user_id:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de usuario.")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al usuario {user_id}?"):
            if self.manager.delete_user(user_id):
                messagebox.showinfo("Éxito", "Usuario eliminado exitosamente.")
                self.clear_user_form()
                self.refresh_users_list()
                self.refresh_dashboard()
            else:
                messagebox.showerror("Error", "Usuario no encontrado.")
    
    def clear_user_form(self):
        """Limpia el formulario de usuarios."""
        self.user_id_entry.delete(0, tk.END)
        self.user_name_entry.delete(0, tk.END)
        self.user_email_entry.delete(0, tk.END)
        self.user_phone_entry.delete(0, tk.END)
    
    def loan_book(self):
        """Presta un libro."""
        user_id = self.loan_user_entry.get().strip()
        isbn = self.loan_isbn_entry.get().strip()
        
        if not user_id or not isbn:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return
        
        if self.manager.loan_book(user_id, isbn):
            messagebox.showinfo("Éxito", "Libro prestado exitosamente.")
            self.loan_user_entry.delete(0, tk.END)
            self.loan_isbn_entry.delete(0, tk.END)
            self.refresh_books_list()
            self.refresh_dashboard()
        else:
            messagebox.showerror("Error", "No se pudo prestar el libro. Verifique que el usuario y el libro existan, y que haya stock disponible.")
    
    def return_book(self):
        """Devuelve un libro."""
        user_id = self.loan_user_entry.get().strip()
        isbn = self.loan_isbn_entry.get().strip()
        
        if not user_id or not isbn:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return
        
        if self.manager.return_book(user_id, isbn):
            messagebox.showinfo("Éxito", "Libro devuelto exitosamente.")
            self.loan_user_entry.delete(0, tk.END)
            self.loan_isbn_entry.delete(0, tk.END)
            self.refresh_books_list()
            self.refresh_dashboard()
        else:
            messagebox.showerror("Error", "No se pudo devolver el libro.")
    
    def reserve_book(self):
        """Reserva un libro."""
        user_id = self.loan_user_entry.get().strip()
        isbn = self.loan_isbn_entry.get().strip()
        
        if not user_id or not isbn:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return
        
        if self.manager.reserve_book(user_id, isbn):
            messagebox.showinfo("Éxito", "Libro reservado exitosamente.")
            self.loan_user_entry.delete(0, tk.END)
            self.loan_isbn_entry.delete(0, tk.END)
            self.refresh_dashboard()
        else:
            messagebox.showerror("Error", "No se pudo reservar el libro. El libro debe tener stock = 0.")
    
    def view_loan_history(self):
        """Muestra el historial de préstamos."""
        user_id = self.loan_user_entry.get().strip()
        if not user_id:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de usuario.")
            return
        
        history = self.manager.get_user_loan_history(user_id)
        if history:
            history_text = f"Historial de Préstamos para Usuario {user_id}:\n\n"
            for i, loan in enumerate(reversed(history), 1):
                history_text += f"{i}. ISBN: {loan['isbn']}\n"
                history_text += f"   Título: {loan.get('title', 'N/A')}\n"
                history_text += f"   Fecha: {loan['date']}\n\n"
            messagebox.showinfo("Historial", history_text)
        else:
            messagebox.showinfo("Historial", "No se encontró historial de préstamos.")
    
    def view_reservations(self):
        """Muestra las reservas."""
        isbn = self.loan_isbn_entry.get().strip()
        if not isbn:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ISBN.")
            return
        
        reservations = self.manager.get_reservations(isbn)
        if reservations:
            res_text = f"Reservas para ISBN {isbn}:\n\n"
            for i, res in enumerate(reservations, 1):
                res_text += f"{i}. Usuario: {res['user_id']}\n"
                res_text += f"   Fecha: {res['date']}\n\n"
            messagebox.showinfo("Reservas", res_text)
        else:
            messagebox.showinfo("Reservas", "No se encontraron reservas.")
    
    def search_books(self):
        """Busca libros."""
        query = self.search_query_entry.get().strip()
        if not query:
            messagebox.showwarning("Advertencia", "Por favor ingrese una consulta de búsqueda.")
            return
        
        search_by = self.search_by_var.get()
        results = self.manager.search_books(query, search_by)
        
        # Limpiar resultados anteriores
        for item in self.search_tree.get_children():
            self.search_tree.delete(item)
        
        # Mostrar resultados
        for book in results:
            self.search_tree.insert('', tk.END, values=(
                book.isbn, book.title, book.author,
                f"{book.weight:.2f} kg", f"${book.value:,.0f}", book.stock
            ))
        
        messagebox.showinfo("Búsqueda", f"Se encontraron {len(results)} resultados.")
    
    def find_risky_combinations(self):
        """Encuentra combinaciones riesgosas."""
        try:
            threshold = float(messagebox.askstring("Umbral", "Ingrese el umbral de peso (kg):", initialvalue="8.0") or "8.0")
            combinations = self.manager.find_risky_combinations(threshold)
            
            if combinations:
                result_text = f"Se encontraron {len(combinations)} combinaciones riesgosas:\n\n"
                for i, combo in enumerate(combinations[:10], 1):  # Mostrar máximo 10
                    total_weight = sum(book.weight for book in combo)
                    result_text += f"{i}. Combinación (Peso Total: {total_weight:.2f} kg):\n"
                    for book in combo:
                        result_text += f"   - {book.title} ({book.weight:.2f} kg)\n"
                    result_text += "\n"
                messagebox.showinfo("Combinaciones Riesgosas", result_text)
            else:
                messagebox.showinfo("Combinaciones Riesgosas", "No se encontraron combinaciones riesgosas.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico válido.")
    
    def find_optimal_shelf(self):
        """Encuentra asignación óptima."""
        try:
            max_capacity = float(messagebox.askstring("Capacidad", "Ingrese la capacidad máxima (kg):", initialvalue="8.0") or "8.0")
            optimal, value, weight = self.manager.find_optimal_shelf_assignment(max_capacity)
            
            result_text = f"Asignación Óptima de Estantería:\n\n"
            result_text += f"Valor Total: ${value:,.0f} COP\n"
            result_text += f"Peso Total: {weight:.2f} kg\n"
            result_text += f"Libros ({len(optimal)}):\n\n"
            for book in optimal:
                result_text += f"- {book.title}\n"
                result_text += f"  Peso: {book.weight:.2f} kg, Valor: ${book.value:,.0f} COP\n\n"
            
            messagebox.showinfo("Asignación Óptima", result_text)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico válido.")
    
    def calculate_total_value(self):
        """Calcula el valor total por autor."""
        author = self.recursion_author_entry.get().strip()
        if not author:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre de autor.")
            return
        
        total_value = self.manager.get_author_total_value(author)
        messagebox.showinfo("Valor Total", f"Valor total de los libros de {author}: ${total_value:,.0f} COP")
    
    def calculate_avg_weight(self):
        """Calcula el peso promedio por autor."""
        author = self.recursion_author_entry.get().strip()
        if not author:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre de autor.")
            return
        
        # Crear ventana para mostrar el proceso de recursión
        process_window = tk.Toplevel(self.root)
        process_window.title("Recursión de Cola - Proceso")
        process_window.geometry("600x400")
        
        text_area = scrolledtext.ScrolledText(process_window, font=('Consolas', 10), wrap=tk.WORD)
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Redirigir print a la ventana (simplificado)
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        avg_weight = self.manager.get_author_average_weight(author)
        
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        text_area.insert(tk.END, output)
        text_area.insert(tk.END, f"\n\nPeso promedio: {avg_weight:.2f} kg")
        text_area.config(state=tk.DISABLED)
    
    def generate_report(self):
        """Genera el reporte global."""
        report = self.manager.generate_global_inventory_report()
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(1.0, report)
        messagebox.showinfo("Éxito", "Reporte generado exitosamente.")
    
    def save_data(self):
        """Guarda los datos."""
        try:
            self.manager.save_data()
            messagebox.showinfo("Éxito", "Datos guardados exitosamente.")
            self.update_status()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    def update_status(self):
        """Actualiza la barra de estado."""
        # Verificar que status_label existe antes de actualizarlo
        if self.status_label is not None:
            total_books = len(self.manager.list_all_books())
            total_users = len(self.manager.list_all_users())
            self.status_label.config(text=f"Sistema listo | Libros: {total_books} | Usuarios: {total_users}")


def main():
    """Función principal para ejecutar la interfaz gráfica."""
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

