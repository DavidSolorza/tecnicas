# Documentación del Sistema de Gestión de Bibliotecas (SGB)

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Componentes Principales](#componentes-principales)
5. [Estructuras de Datos](#estructuras-de-datos)
6. [Algoritmos Implementados](#algoritmos-implementados)
7. [Funcionalidades](#funcionalidades)
8. [Guía de Uso](#guía-de-uso)
9. [Requerimientos Técnicos](#requerimientos-técnicos)
10. [Ejemplos de Uso](#ejemplos-de-uso)

---

## Introducción

El **Sistema de Gestión de Bibliotecas (SGB)** es una aplicación completa desarrollada en Python que permite gestionar todos los aspectos de una biblioteca, incluyendo libros, usuarios, préstamos, reservas y estanterías. El sistema implementa diversas estructuras de datos, algoritmos de ordenamiento y búsqueda, y técnicas de programación avanzadas como recursión, fuerza bruta y backtracking.

### Objetivos del Proyecto

- Demostrar la comprensión de estructuras de datos (Listas, Pilas, Colas)
- Implementar algoritmos de ordenamiento (Insertion Sort, Merge Sort)
- Implementar algoritmos de búsqueda (Linear Search, Binary Search)
- Aplicar técnicas de resolución de problemas (Fuerza Bruta, Backtracking)
- Utilizar recursión (Stack Recursion, Tail Recursion)
- Aplicar principios de Programación Orientada a Objetos (POO)
- Crear un sistema modular y bien documentado

---

## Arquitectura del Sistema

El sistema está diseñado siguiendo una arquitectura modular que separa las responsabilidades en diferentes componentes:

```
┌─────────────────────────────────────────────────────────┐
│                    Interfaz de Usuario                   │
│  (main.py - CLI / gui_main.py - GUI)                     │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│              LibraryManager (Gestor Principal)           │
│  - Coordina todas las operaciones                        │
│  - Gestiona inventarios y estructuras de datos          │
└──────┬──────────┬──────────┬──────────┬─────────────────┘
       │          │          │          │
┌──────▼──┐ ┌─────▼──┐ ┌─────▼──┐ ┌─────▼──────┐
│ Models  │ │Algorithms│ │Data    │ │Utils      │
│         │ │          │ │Structs │ │           │
│ - Book  │ │- Sorting │ │- Stack │ │- File     │
│ - User  │ │- Search  │ │- Queue │ │  Handler  │
│ - Shelf │ │- Shelf   │ │        │ │           │
│         │ │- Recursion│ │        │ │           │
└─────────┘ └──────────┘ └────────┘ └───────────┘
```

---

## Estructura del Proyecto

```
tecnicas-de-programacion/
│
├── models/                      # Modelos de datos (POO)
│   ├── __init__.py
│   ├── book.py                 # Clase Book (Libro)
│   ├── user.py                 # Clase User (Usuario)
│   └── shelf.py                # Clase Shelf (Estantería)
│
├── data_structures/            # Estructuras de datos
│   ├── __init__.py
│   ├── stack.py                 # Stack (Pila) - LIFO
│   └── queue.py                 # Queue (Cola) - FIFO
│
├── algorithms/                  # Algoritmos implementados
│   ├── __init__.py
│   ├── sorting.py               # Insertion Sort, Merge Sort
│   ├── searching.py             # Linear Search, Binary Search
│   ├── shelf_algorithms.py      # Fuerza Bruta, Backtracking
│   └── recursion.py             # Recursión de Pila y Cola
│
├── utils/                       # Utilidades
│   ├── __init__.py
│   └── file_handler.py          # Manejo de archivos (CSV/JSON)
│
├── data/                        # Archivos de datos
│   ├── initial_books.csv        # Inventario inicial (CSV)
│   ├── initial_books.json       # Inventario inicial (JSON)
│   ├── books.json               # Inventario actual (auto-generado)
│   ├── loan_history.json        # Historial de préstamos
│   └── reservations.json        # Reservas pendientes
│
├── reports/                     # Reportes generados
│   └── global_inventory_report.txt
│
├── main.py                      # Interfaz de línea de comandos (CLI)
├── gui_main.py                  # Interfaz gráfica (GUI)
├── library_manager.py           # Clase principal del sistema
├── test_system.py               # Script de pruebas
├── README.md                    # Documentación general
├── DOCUMENTACION.md             # Esta documentación
└── .gitignore                   # Archivos ignorados por Git
```

---

## Componentes Principales

### 1. Models (Modelos)

#### Book (Libro)
**Ubicación:** `models/book.py`

Representa un libro en el sistema con los siguientes atributos:
- `isbn` (str): Número ISBN único
- `title` (str): Título del libro
- `author` (str): Autor del libro
- `weight` (float): Peso en kilogramos
- `value` (float): Valor en pesos colombianos (COP)
- `stock` (int): Cantidad disponible
- `shelf_id` (str, opcional): ID de la estantería donde está ubicado

**Métodos principales:**
- `to_dict()`: Convierte el libro a diccionario
- `from_dict()`: Crea un libro desde un diccionario

#### User (Usuario)
**Ubicación:** `models/user.py`

Representa un usuario del sistema:
- `user_id` (str): Identificador único
- `name` (str): Nombre del usuario
- `email` (str): Correo electrónico
- `phone` (str): Teléfono

#### Shelf (Estantería)
**Ubicación:** `models/shelf.py`

Representa una estantería física:
- `shelf_id` (str): Identificador único
- `capacity` (float): Capacidad máxima en kg (default: 8.0)
- `books` (list): Lista de libros en la estantería

**Métodos principales:**
- `get_total_weight()`: Calcula el peso total
- `get_total_value()`: Calcula el valor total
- `can_add_book()`: Verifica si se puede agregar un libro
- `add_book()`: Agrega un libro a la estantería

### 2. LibraryManager (Gestor Principal)

**Ubicación:** `library_manager.py`

Clase central que coordina todas las operaciones del sistema.

#### Estructuras de Datos Principales

```python
# Dos listas maestras (REQUERIMIENTO)
self.general_inventory = []      # Lista desordenada (orden de carga)
self.ordered_inventory = []      # Lista ordenada por ISBN (ascendente)

# Estructuras de datos
self.loan_history = {}           # Dict[user_id, Stack] - Historial LIFO
self.reservations = {}            # Dict[isbn, Queue] - Reservas FIFO

# Gestión adicional
self.users = {}                   # Dict[user_id, User]
self.shelves = {}                 # Dict[shelf_id, Shelf]
```

#### Funcionalidades Principales

1. **Gestión de Libros (CRUD)**
   - `add_book()`: Agrega libro y mantiene ordenado con Insertion Sort
   - `get_book_by_isbn()`: Busca usando Binary Search
   - `search_books()`: Busca usando Linear Search
   - `update_book()`: Actualiza información
   - `delete_book()`: Elimina libro

2. **Gestión de Préstamos**
   - `loan_book()`: Presta libro (agrega a Stack - LIFO)
   - `return_book()`: Devuelve libro (verifica reservas con Binary Search)

3. **Gestión de Reservas**
   - `reserve_book()`: Reserva libro (agrega a Queue - FIFO, solo si stock=0)

4. **Módulos Avanzados**
   - `find_risky_combinations()`: Fuerza Bruta
   - `find_optimal_shelf_assignment()`: Backtracking
   - `get_author_total_value()`: Recursión de Pila
   - `get_author_average_weight()`: Recursión de Cola

5. **Reportes**
   - `generate_global_inventory_report()`: Reporte ordenado con Merge Sort

---

## Estructuras de Datos

### 1. Stack (Pila) - LIFO

**Ubicación:** `data_structures/stack.py`

**Uso:** Historial de préstamos por usuario

**Características:**
- Last In, First Out (LIFO)
- El préstamo más reciente está en la cima
- Implementación con lista de Python

**Operaciones:**
- `push(item)`: Agrega elemento al tope
- `pop()`: Remueve y retorna el elemento del tope
- `peek()`: Retorna el elemento del tope sin removerlo
- `is_empty()`: Verifica si está vacía
- `size()`: Retorna el tamaño

**Ejemplo de uso:**
```python
stack = Stack()
stack.push({'isbn': '123', 'date': '2025-01-01'})
loan = stack.pop()  # Obtiene el préstamo más reciente
```

### 2. Queue (Cola) - FIFO

**Ubicación:** `data_structures/queue.py`

**Uso:** Lista de espera para reservas

**Características:**
- First In, First Out (FIFO)
- El primero en reservar es el primero en recibir
- Implementación con lista de Python

**Operaciones:**
- `enqueue(item)`: Agrega elemento al final
- `dequeue()`: Remueve y retorna el primer elemento
- `front()`: Retorna el primer elemento sin removerlo
- `is_empty()`: Verifica si está vacía
- `size()`: Retorna el tamaño

**Ejemplo de uso:**
```python
queue = Queue()
queue.enqueue({'user_id': 'U001', 'date': '2025-01-01'})
reservation = queue.dequeue()  # Obtiene la primera reserva
```

---

## Algoritmos Implementados

### 1. Algoritmos de Ordenamiento

#### Insertion Sort (Ordenamiento por Inserción)

**Ubicación:** `algorithms/sorting.py`

**Uso:** Mantener el Inventario Ordenado siempre ordenado por ISBN

**Complejidad:**
- Tiempo: O(n²) peor caso, O(n) mejor caso
- Espacio: O(1)

**Características:**
- Se ejecuta automáticamente cada vez que se agrega un libro
- Mantiene la lista ordenada de forma incremental
- Eficiente para listas pequeñas o parcialmente ordenadas

**Implementación:**
```python
def insertion_sort(books: list, key=lambda x: x.isbn) -> list:
    sorted_books = books.copy()
    for i in range(1, len(sorted_books)):
        current = sorted_books[i]
        j = i - 1
        while j >= 0 and key(sorted_books[j]) > key(current):
            sorted_books[j + 1] = sorted_books[j]
            j -= 1
        sorted_books[j + 1] = current
    return sorted_books
```

#### Merge Sort (Ordenamiento por Mezcla)

**Ubicación:** `algorithms/sorting.py`

**Uso:** Generar Reporte Global ordenado por valor

**Complejidad:**
- Tiempo: O(n log n)
- Espacio: O(n)

**Características:**
- Divide y vencerás
- Estable (mantiene el orden relativo)
- Eficiente para listas grandes

**Implementación:**
```python
def merge_sort(books: list, key=lambda x: x.value) -> list:
    if len(books) <= 1:
        return books.copy()
    
    mid = len(books) // 2
    left = merge_sort(books[:mid], key)
    right = merge_sort(books[mid:], key)
    
    return _merge(left, right, key)
```

### 2. Algoritmos de Búsqueda

#### Linear Search (Búsqueda Lineal)

**Ubicación:** `algorithms/searching.py`

**Uso:** Buscar libros por título o autor en el Inventario General

**Complejidad:**
- Tiempo: O(n)
- Espacio: O(1)

**Características:**
- Busca secuencialmente en la lista
- Funciona con listas desordenadas
- Retorna todos los resultados que coinciden

**Implementación:**
```python
def linear_search(books: list, query: str, search_by: str = 'title') -> list:
    results = []
    query_lower = query.lower()
    for book in books:
        if search_by == 'title':
            if query_lower in book.title.lower():
                results.append(book)
        elif search_by == 'author':
            if query_lower in book.author.lower():
                results.append(book)
    return results
```

#### Binary Search (Búsqueda Binaria)

**Ubicación:** `algorithms/searching.py`

**Uso:** Buscar libros por ISBN en el Inventario Ordenado (CRÍTICO)

**Complejidad:**
- Tiempo: O(log n)
- Espacio: O(1)

**Características:**
- Requiere lista ordenada
- Muy eficiente para búsquedas
- **CRÍTICO:** Se usa para verificar reservas al devolver libros

**Implementación:**
```python
def binary_search(books: list, isbn: str) -> int:
    left = 0
    right = len(books) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if books[mid].isbn == isbn:
            return mid
        elif books[mid].isbn < isbn:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # No encontrado
```

### 3. Algoritmos de Resolución de Problemas

#### Fuerza Bruta (Brute Force)

**Ubicación:** `algorithms/shelf_algorithms.py`

**Uso:** Encontrar combinaciones riesgosas de 4 libros que exceden 8 kg

**Complejidad:**
- Tiempo: O(n⁴)
- Espacio: O(n⁴)

**Características:**
- Explora exhaustivamente todas las combinaciones
- Garantiza encontrar todas las soluciones
- Puede ser lento para listas grandes

**Implementación:**
```python
def find_risky_combinations(books: list, threshold: float = 8.0) -> list:
    risky_combinations = []
    for combo in combinations(books, 4):
        total_weight = sum(book.weight for book in combo)
        if total_weight > threshold:
            risky_combinations.append(combo)
    return risky_combinations
```

#### Backtracking

**Ubicación:** `algorithms/shelf_algorithms.py`

**Uso:** Encontrar combinación óptima que maximiza valor sin exceder peso

**Complejidad:**
- Tiempo: O(2ⁿ) peor caso
- Espacio: O(n) para recursión

**Características:**
- Explora el espacio de soluciones de forma inteligente
- Prunea ramas que no llevan a soluciones válidas
- Encuentra la solución óptima

**Implementación:**
```python
def find_optimal_shelf(books: list, max_capacity: float = 8.0) -> tuple:
    best_combination = []
    best_value = 0
    
    def backtrack(current_index, current_books, current_weight, current_value):
        nonlocal best_combination, best_value
        
        if current_index >= len(books):
            if current_value > best_value:
                best_combination = current_books.copy()
                best_value = current_value
            return
        
        # No incluir libro actual
        backtrack(current_index + 1, current_books, current_weight, current_value)
        
        # Incluir libro actual si cabe
        book = books[current_index]
        if current_weight + book.weight <= max_capacity:
            current_books.append(book)
            backtrack(current_index + 1, current_books,
                     current_weight + book.weight,
                     current_value + book.value)
            current_books.pop()  # Backtrack
    
    backtrack(0, [], 0.0, 0.0)
    return (best_combination, best_value, sum(b.weight for b in best_combination))
```

### 4. Algoritmos de Recursión

#### Recursión de Pila (Stack Recursion)

**Ubicación:** `algorithms/recursion.py`

**Uso:** Calcular valor total de libros por autor

**Características:**
- Usa la pila de llamadas para acumular valores
- La acumulación ocurre después de la llamada recursiva
- Más fácil de entender pero menos eficiente en memoria

**Implementación:**
```python
def calculate_author_total_value(books: list, author: str, index: int = 0) -> float:
    if index >= len(books):
        return 0.0
    
    current_value = 0.0
    if books[index].author.lower() == author.lower():
        current_value = books[index].value
    
    # Recursión: acumula después de la llamada
    return current_value + calculate_author_total_value(books, author, index + 1)
```

#### Recursión de Cola (Tail Recursion)

**Ubicación:** `algorithms/recursion.py`

**Uso:** Calcular peso promedio de libros por autor

**Características:**
- Pasa valores acumulados como parámetros
- La llamada recursiva es la última operación
- Más eficiente (aunque Python no optimiza tail recursion)
- Muestra el proceso de ejecución por consola

**Implementación:**
```python
def calculate_author_average_weight(books: list, author: str,
                                   index: int = 0,
                                   total_weight: float = 0.0,
                                   count: int = 0) -> float:
    if index >= len(books):
        if count == 0:
            return 0.0
        average = total_weight / count
        print(f"Resultado: Peso total = {total_weight:.2f} kg, "
              f"Conteo = {count}, Promedio = {average:.2f} kg")
        return average
    
    current_weight = total_weight
    current_count = count
    
    if books[index].author.lower() == author.lower():
        current_weight += books[index].weight
        current_count += 1
        print(f"Procesando libro {index + 1}: '{books[index].title}' "
              f"(Peso: {books[index].weight:.2f} kg)")
    
    # Recursión de cola: pasa valores acumulados
    return calculate_author_average_weight(
        books, author, index + 1, current_weight, current_count
    )
```

---

## Funcionalidades

### 1. Gestión de Libros

#### Agregar Libro
- Valida que el ISBN no exista
- Agrega a Inventario General (desordenado)
- Agrega a Inventario Ordenado y mantiene orden con Insertion Sort

#### Buscar Libro
- **Por ISBN:** Usa Binary Search en Inventario Ordenado
- **Por Título/Autor:** Usa Linear Search en Inventario General

#### Actualizar Libro
- Permite actualizar cualquier campo
- Re-ordena el Inventario Ordenado si es necesario

#### Eliminar Libro
- Remueve de ambas listas
- Elimina reservas asociadas

### 2. Gestión de Usuarios

- CRUD completo (Create, Read, Update, Delete)
- Inicializa Stack de historial al crear usuario

### 3. Gestión de Préstamos

#### Prestar Libro
1. Verifica que usuario y libro existan
2. Verifica que haya stock disponible
3. Disminuye stock
4. Agrega registro a Stack (LIFO) del usuario

#### Devolver Libro
1. **CRÍTICO:** Usa Binary Search para encontrar el libro
2. Aumenta stock
3. **CRÍTICO:** Verifica si hay reservas pendientes
4. Si hay reservas, asigna automáticamente al primero en la cola (FIFO)

### 4. Gestión de Reservas

#### Reservar Libro
- Solo permite reserva si stock = 0
- Agrega a Queue (FIFO) del ISBN
- Persiste en archivo JSON

### 5. Módulo de Estantería

#### Combinaciones Riesgosas (Fuerza Bruta)
- Encuentra todas las combinaciones de 4 libros
- Que excedan el umbral de peso (default: 8 kg)
- Explora exhaustivamente todas las posibilidades

#### Asignación Óptima (Backtracking)
- Encuentra combinación que maximiza valor
- Sin exceder capacidad de peso (default: 8 kg)
- Muestra el proceso de exploración

### 6. Módulo de Recursión

#### Valor Total (Recursión de Pila)
- Calcula suma de valores de libros por autor
- Usa recursión estándar con acumulación en retorno

#### Peso Promedio (Recursión de Cola)
- Calcula promedio de pesos de libros por autor
- Usa recursión de cola con parámetros acumulados
- Muestra proceso de ejecución

### 7. Reportes

#### Reporte Global de Inventario
- Ordena por valor usando Merge Sort
- Muestra todos los libros con información completa
- Calcula valor total del inventario
- Puede guardarse en archivo

---

## Guía de Uso

### Interfaz de Línea de Comandos (CLI)

**Ejecutar:**
```bash
python main.py
```

**Menú Principal:**
1. Cargar Inventario Inicial
2. Gestión de Libros (CRUD)
3. Gestión de Usuarios (CRUD)
4. Gestión de Estanterías (CRUD)
5. Prestar un Libro
6. Devolver un Libro
7. Reservar un Libro
8. Buscar Libros
9. Ver Historial de Préstamos
10. Ver Reservas
11. Módulo de Estantería
12. Módulo de Recursión
13. Generar Reporte Global
14. Guardar Datos
15. Cargar Datos
0. Salir

### Interfaz Gráfica (GUI)

**Ejecutar:**
```bash
python gui_main.py
```

**Características:**
- Interfaz moderna con pestañas
- Formularios intuitivos
- Tablas para visualizar datos
- Botones con iconos y colores
- Mensajes informativos

**Pestañas:**
- 📖 Libros: Gestión completa de libros
- 👥 Usuarios: Gestión de usuarios
- 📋 Préstamos: Préstamos y reservas
- 🔍 Búsqueda: Buscar libros
- ⚙️ Avanzado: Módulos de estantería y recursión
- 📊 Reportes: Generar reportes

### Persistencia de Datos

**Archivos generados automáticamente:**
- `data/books.json`: Inventario actual
- `data/loan_history.json`: Historial de préstamos
- `data/reservations.json`: Reservas pendientes

**Cargar datos iniciales:**
- Colocar archivo CSV o JSON en `data/initial_books.csv` o `data/initial_books.json`
- El sistema carga automáticamente al iniciar

---

## Requerimientos Técnicos

### Requisitos del Sistema

- **Python:** 3.7 o superior
- **Sistema Operativo:** Windows, Linux, macOS
- **Dependencias:** Ninguna (solo biblioteca estándar de Python)

### Módulos Utilizados

- `tkinter`: Interfaz gráfica (incluido en Python)
- `json`: Manejo de archivos JSON
- `csv`: Manejo de archivos CSV
- `datetime`: Manejo de fechas
- `itertools`: Combinaciones para fuerza bruta
- `typing`: Tipos de datos

### Instalación

No requiere instalación de dependencias externas. Solo necesita Python 3.7+.

```bash
# Verificar versión de Python
python --version

# Ejecutar sistema CLI
python main.py

# Ejecutar sistema GUI
python gui_main.py
```

---

## Ejemplos de Uso

### Ejemplo 1: Agregar y Buscar Libro

```python
from library_manager import LibraryManager

manager = LibraryManager()

# Agregar libro
manager.add_book(
    isbn="978-0-123456-78-9",
    title="El Gran Gatsby",
    author="F. Scott Fitzgerald",
    weight=0.45,
    value=45000,
    stock=3
)

# Buscar por ISBN (Binary Search)
book = manager.get_book_by_isbn("978-0-123456-78-9")
print(book.title)  # "El Gran Gatsby"

# Buscar por título (Linear Search)
results = manager.search_books("Gatsby", "title")
print(len(results))  # 1
```

### Ejemplo 2: Préstamo y Devolución con Reservas

```python
# Agregar usuario
manager.add_user("U001", "Juan Pérez", "juan@email.com")

# Prestar libro
manager.loan_book("U001", "978-0-123456-78-9")
# Stock disminuye a 2

# Agotar stock
manager.update_book("978-0-123456-78-9", stock=0)

# Reservar (solo funciona si stock = 0)
manager.reserve_book("U002", "978-0-123456-78-9")

# Devolver libro
manager.return_book("U001", "978-0-123456-78-9")
# Automáticamente se presta a U002 (primero en la cola)
```

### Ejemplo 3: Módulo de Estantería

```python
# Encontrar combinaciones riesgosas (Fuerza Bruta)
risky = manager.find_risky_combinations(threshold=8.0)
print(f"Combinaciones riesgosas: {len(risky)}")

# Encontrar asignación óptima (Backtracking)
optimal, value, weight = manager.find_optimal_shelf_assignment(max_capacity=8.0)
print(f"Valor óptimo: ${value:,.0f} COP")
print(f"Peso: {weight:.2f} kg")
print(f"Libros: {len(optimal)}")
```

### Ejemplo 4: Recursión

```python
# Valor total (Recursión de Pila)
total_value = manager.get_author_total_value("George Orwell")
print(f"Valor total: ${total_value:,.0f} COP")

# Peso promedio (Recursión de Cola)
avg_weight = manager.get_author_average_weight("George Orwell")
# Muestra proceso de ejecución por consola
print(f"Peso promedio: {avg_weight:.2f} kg")
```

### Ejemplo 5: Reporte Global

```python
# Generar reporte (Merge Sort por valor)
report = manager.generate_global_inventory_report()
print(report)

# Guardar en archivo
manager.save_global_report("reports/inventario_global.txt")
```

---

## Flujo de Datos

### Flujo de Préstamo

```
Usuario solicita préstamo
    ↓
Verificar usuario existe
    ↓
Verificar libro existe (Binary Search)
    ↓
Verificar stock > 0
    ↓
Disminuir stock
    ↓
Agregar a Stack de historial (LIFO)
    ↓
Préstamo exitoso
```

### Flujo de Devolución con Reservas

```
Usuario devuelve libro
    ↓
Buscar libro (Binary Search - CRÍTICO)
    ↓
Aumentar stock
    ↓
Verificar reservas pendientes (Binary Search - CRÍTICO)
    ↓
¿Hay reservas?
    ├─ Sí → Obtener primera reserva (Queue - FIFO)
    │       ↓
    │   Prestar automáticamente
    │       ↓
    │   Devolución exitosa
    │
    └─ No → Devolución exitosa
```

### Flujo de Reserva

```
Usuario solicita reserva
    ↓
Verificar usuario existe
    ↓
Verificar libro existe (Binary Search)
    ↓
Verificar stock = 0 (REQUERIMIENTO)
    ↓
Agregar a Queue de reservas (FIFO)
    ↓
Reserva exitosa
```

---

## Consideraciones de Diseño

### Decisiones de Implementación

1. **Dos Listas Maestras:**
   - Inventario General: Para búsquedas lineales y reflejar orden de carga
   - Inventario Ordenado: Para búsquedas binarias eficientes

2. **Stack para Préstamos:**
   - LIFO permite ver préstamos más recientes primero
   - Natural para historial cronológico

3. **Queue para Reservas:**
   - FIFO garantiza justicia (primero en reservar, primero en recibir)
   - Evita conflictos de prioridad

4. **Insertion Sort:**
   - Eficiente para mantener orden incremental
   - Se ejecuta solo cuando se agregan libros

5. **Binary Search Crítico:**
   - Usado para verificar reservas al devolver
   - Garantiza asignación correcta

### Optimizaciones

- Los algoritmos están optimizados para sus casos de uso
- La persistencia usa JSON para facilidad de lectura
- La interfaz gráfica carga datos de forma asíncrona

---

## Extensibilidad

El sistema está diseñado para ser extensible:

1. **Nuevos Modelos:** Agregar clases en `models/`
2. **Nuevos Algoritmos:** Agregar funciones en `algorithms/`
3. **Nuevas Estructuras:** Agregar clases en `data_structures/`
4. **Nuevas Funcionalidades:** Extender `LibraryManager`

---

## Conclusión

El Sistema de Gestión de Bibliotecas demuestra la aplicación práctica de:
- Estructuras de datos fundamentales
- Algoritmos de ordenamiento y búsqueda
- Técnicas avanzadas de programación
- Principios de diseño de software
- Programación orientada a objetos
- Arquitectura modular

El código está completamente documentado y listo para uso educativo y profesional.

---

## Autor

Desarrollado como parte del proyecto de "Técnicas de Programación" 2025-2.

## Licencia

Este proyecto es para fines educativos.

---

**Última actualización:** Enero 2025

