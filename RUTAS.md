# 📍 RUTAS Y REFERENCIAS PARA SUSTENTACIÓN

Este documento contiene las rutas exactas y números de línea de todas las funcionalidades implementadas según los requisitos del proyecto.

---

## A. ESTRUCTURAS BASE

### 1. Adquisición de Datos (CSV/JSON)

**Ubicación:** `utils/file_handler.py`

- **Lectura CSV:** Líneas 16-55
  - Función: `load_books_from_csv(filepath: str)`
  - Convierte registros CSV a objetos Book
  
- **Lectura JSON:** Líneas 58-95
  - Función: `load_books_from_json(filepath: str)`
  - Convierte registros JSON a objetos Book

**Uso en LibraryManager:** `library_manager.py`
- Líneas 67-97: Método `load_initial_inventory()` que llama a las funciones de carga
- Líneas 82-85: Selección entre CSV y JSON según formato

---

### 2. Listas Maestras (Inventario General e Inventario Ordenado)

**Ubicación:** `library_manager.py`

- **Inventario General (desordenado):** Línea 48
  ```python
  self.general_inventory = []  # Lista desordenada (refleja el orden de carga)
  ```

- **Inventario Ordenado (por ISBN):** Línea 49
  ```python
  self.ordered_inventory = []  # Lista siempre ordenada por ISBN (ascendente)
  ```

- **Mantenimiento de ambas listas:** 
  - Líneas 88-92: Al cargar inventario inicial
  - Líneas 165-170: Al agregar un nuevo libro

---

### 3. Pilas (Historial de Préstamos)

**Implementación de Stack:** `data_structures/stack.py`
- **Clase Stack completa:** Líneas 7-100
- **Método push():** Líneas 20-27
- **Método pop():** Líneas 29-41
- **Método is_empty():** Líneas 57-64

**Uso en LibraryManager:** `library_manager.py`
- **Inicialización:** Línea 52
  ```python
  self.loan_history = {}  # Dict[user_id, Stack] - Pila LIFO para historial de préstamos
  ```

- **Crear Stack para usuario:** Líneas 295-296 y 480-481

- **Push en préstamo:** Líneas 452-490
  - Línea 488: `self.loan_history[user_id].push(loan_record)`
  - El registro incluye ISBN y fecha (líneas 483-487)

- **Consultar historial:** Líneas 534-548
  - Método `get_user_loan_history()` que convierte Stack a lista

---

### 4. Colas (Reservas)

**Implementación de Queue:** `data_structures/queue.py`
- **Clase Queue completa:** Líneas 7-100
- **Método enqueue():** Líneas 20-27
- **Método dequeue():** Líneas 29-41
- **Método is_empty():** Líneas 57-64

**Uso en LibraryManager:** `library_manager.py`
- **Inicialización:** Línea 53
  ```python
  self.reservations = {}  # Dict[isbn, Queue] - Cola FIFO para reservas
  ```

- **Validación de stock cero:** Líneas 577-579
  ```python
  if book.stock > 0:
      return False
  ```

- **Enqueue en reserva:** Líneas 553-592
  - Línea 583: Crear Queue si no existe
  - Línea 590: `self.reservations[isbn].enqueue(reservation)`

- **Dequeue en devolución:** Líneas 523-530
  - Línea 525: `reservation = self.reservations[isbn].dequeue()`
  - Verificación de reservas pendientes antes de desencolar

---

## B. ALGORITMOS DE ORDENAMIENTO

### 5. Ordenamiento por Inserción (Insertion Sort)

**Implementación:** `algorithms/sorting.py`
- **Función insertion_sort():** Líneas 7-35
- **Algoritmo completo:** Líneas 24-33
- **Documentación:** Líneas 8-21

**Uso en LibraryManager:** `library_manager.py`
- **Al cargar inventario:** Línea 92
  ```python
  self.ordered_inventory = insertion_sort(self.ordered_inventory)
  ```

- **Al agregar libro:** Línea 170
  ```python
  self.ordered_inventory = insertion_sort(self.ordered_inventory)
  ```

- **Al actualizar libro:** Línea 236
  ```python
  self.ordered_inventory = insertion_sort(self.ordered_inventory)
  ```

**Importación:** Línea 14 de `library_manager.py`

---

### 6. Ordenamiento por Mezcla (Merge Sort)

**Implementación:** `algorithms/sorting.py`
- **Función merge_sort():** Líneas 38-62
- **División recursiva:** Líneas 56-59
- **Función auxiliar _merge():** Líneas 65-93
- **Lógica de combinación:** Líneas 81-91

**Uso en LibraryManager:** `library_manager.py`
- **Generación de reporte global:** Líneas 685-717
- **Línea 698:** Ordenamiento por valor usando Merge Sort
  ```python
  sorted_books = merge_sort(self.general_inventory, key=lambda x: x.value)
  ```

**Importación:** Línea 14 de `library_manager.py`

---

## C. ALGORITMOS DE BÚSQUEDA

### 7. Búsqueda Lineal (Linear Search)

**Implementación:** `algorithms/searching.py`
- **Función linear_search():** Líneas 7-34
- **Algoritmo completo:** Líneas 26-32
- **Búsqueda por título o autor:** Líneas 27-32
- **Case-insensitive:** Línea 24

**Uso en LibraryManager:** `library_manager.py`
- **Método search_books():** Líneas 192-206
- **Línea 206:** Llamada a linear_search en Inventario General
  ```python
  return linear_search(self.general_inventory, query, search_by)
  ```

**Importación:** Línea 15 de `library_manager.py`

---

### 8. Búsqueda Binaria y Conexión con Reservas

**Implementación:** `algorithms/searching.py`
- **Función binary_search():** Líneas 37-66
- **Algoritmo completo:** Líneas 56-64
- **Búsqueda por ISBN:** Líneas 59-64

**Uso en LibraryManager:** `library_manager.py`
- **Búsqueda por ISBN:** Líneas 174-190
  - Línea 187: `index = binary_search(self.ordered_inventory, isbn)`

- **Conexión crítica con reservas:** Líneas 492-532
  - Línea 512: Buscar libro usando Binary Search
  - Líneas 521-530: Verificar reservas pendientes después de devolución
  - Línea 523: Verificar si hay reservas en la cola
  - Línea 525: Desencolar reserva (FIFO)
  - Línea 529: Asignar automáticamente al usuario reservado

**Importación:** Línea 15 de `library_manager.py`

---

## D. ALGORITMOS DE RESOLUCIÓN

### 9. Fuerza Bruta (Combinaciones)

**Implementación:** `algorithms/shelf_algorithms.py`
- **Función find_risky_combinations():** Líneas 10-34
- **Exploración exhaustiva:** Línea 28
  ```python
  for combo in combinations(books, 4):
  ```
- **Validación de peso:** Líneas 29-32
- **Documentación:** Líneas 11-23

**Uso en LibraryManager:** `library_manager.py`
- **Método find_risky_shelf_combinations():** Líneas 612-628
- **Línea 628:** Llamada a la función
  ```python
  return find_risky_combinations(self.general_inventory, threshold)
  ```

**Importación:** Línea 16 de `library_manager.py`

---

### 10. Backtracking

**Implementación:** `algorithms/shelf_algorithms.py`
- **Función find_optimal_shelf():** Líneas 37-95
- **Función interna backtrack():** Líneas 56-90
- **Caso base:** Líneas 69-75
- **Exploración (no incluir libro):** Línea 78
- **Exploración (incluir libro):** Líneas 81-89
- **Backtracking (eliminar):** Línea 90
- **Inicio del backtracking:** Línea 93

**Uso en LibraryManager:** `library_manager.py`
- **Método find_optimal_shelf_assignment():** Líneas 630-645
- **Línea 645:** Llamada a la función
  ```python
  return find_optimal_shelf(self.general_inventory, max_capacity)
  ```

**Importación:** Línea 16 de `library_manager.py`

---

## E. RECURSIÓN

### 11. Recursión de Pila (Stack Recursion)

**Implementación:** `algorithms/recursion.py`
- **Función calculate_author_total_value():** Líneas 7-33
- **Caso base:** Líneas 24-25
- **Caso recursivo:** Líneas 28-33
- **Acumulación en el stack:** Línea 33
  ```python
  return current_value + calculate_author_total_value(books, author, index + 1)
  ```

**Uso en LibraryManager:** `library_manager.py`
- **Método get_author_total_value():** Líneas 650-664
- **Línea 664:** Llamada a la función recursiva
  ```python
  return calculate_author_total_value(self.general_inventory, author)
  ```

**Importación:** Línea 17 de `library_manager.py`

---

### 12. Recursión de Cola (Tail Recursion)

**Implementación:** `algorithms/recursion.py`
- **Función calculate_author_average_weight():** Líneas 36-78
- **Parámetros acumuladores:** Líneas 36-37
  ```python
  total_weight: float = 0.0, count: int = 0
  ```
- **Caso base:** Líneas 56-62
- **Actualización de acumuladores:** Líneas 65-73
- **Llamada recursiva de cola:** Líneas 76-78
  ```python
  return calculate_author_average_weight(
      books, author, index + 1, current_weight, current_count
  )
  ```
- **Demostración por consola:** Líneas 60-61 y 71-73

**Uso en LibraryManager:** `library_manager.py`
- **Método get_author_average_weight():** Líneas 666-680
- **Línea 680:** Llamada a la función recursiva
  ```python
  return calculate_author_average_weight(self.general_inventory, author)
  ```

**Importación:** Línea 17 de `library_manager.py`

---

## F. ESTRUCTURA DEL PROYECTO

### 13. POO y Estructura de Clases

**Clase Book:** `models/book.py`
- **Definición de clase:** Líneas 7-101
- **Constructor:** Líneas 21-41
- **Métodos:** `to_dict()` (líneas 65-80), `from_dict()` (líneas 82-101)
- **Métodos especiales:** `__str__()`, `__repr__()`, `__eq__()`, `__lt__()`

**Clase User:** `models/user.py`
- **Definición de clase:** Líneas 7-78
- **Constructor:** Líneas 18-31
- **Métodos:** `to_dict()` (líneas 47-59), `from_dict()` (líneas 61-77)

**Clase Shelf:** `models/shelf.py`
- **Definición de clase:** Líneas 7-111
- **Constructor:** Líneas 17-27
- **Métodos:** `get_total_weight()`, `get_total_value()`, `can_add_book()`, `add_book()`, `remove_book()`

**Clase LibraryManager:** `library_manager.py`
- **Definición de clase:** Líneas 26-731
- **Encapsulación:** Todos los atributos son privados (self.xxx)
- **Métodos organizados por funcionalidad:** CRUD, préstamos, reservas, reportes

**Clase Stack:** `data_structures/stack.py`
- **Definición de clase:** Líneas 7-100
- **Encapsulación:** Atributo `items` privado

**Clase Queue:** `data_structures/queue.py`
- **Definición de clase:** Líneas 7-100
- **Encapsulación:** Atributo `items` privado

---

### 14. Modularidad y Carpetas

**Estructura de carpetas:**
```
├── algorithms/          # Algoritmos de ordenamiento, búsqueda, recursión
│   ├── sorting.py      # Insertion Sort, Merge Sort
│   ├── searching.py    # Linear Search, Binary Search
│   ├── recursion.py    # Recursión de pila y cola
│   └── shelf_algorithms.py  # Fuerza Bruta, Backtracking
├── data_structures/    # Estructuras de datos
│   ├── stack.py        # Implementación de Stack
│   └── queue.py        # Implementación de Queue
├── models/             # Modelos de datos (POO)
│   ├── book.py         # Clase Book
│   ├── user.py         # Clase User
│   └── shelf.py        # Clase Shelf
├── utils/              # Utilidades
│   └── file_handler.py # Manejo de archivos CSV/JSON
├── data/               # Datos iniciales
│   ├── initial_books.csv
│   └── initial_books.json
└── library_manager.py  # Clase principal del sistema
```

**Importaciones modulares:** `library_manager.py`
- Líneas 9-23: Todas las importaciones de módulos separados

---

### 15. Documentación del Código

**Docstrings en clases:**
- `library_manager.py` Líneas 27-36: Docstring de LibraryManager
- `models/book.py` Líneas 7-19: Docstring de Book
- `models/user.py` Líneas 7-16: Docstring de User
- `models/shelf.py` Líneas 7-15: Docstring de Shelf
- `data_structures/stack.py` Líneas 7-14: Docstring de Stack
- `data_structures/queue.py` Líneas 7-14: Docstring de Queue

**Docstrings en algoritmos complejos:**
- `algorithms/sorting.py`:
  - Líneas 8-21: Insertion Sort
  - Líneas 39-52: Merge Sort
  - Líneas 65-76: Función _merge
- `algorithms/searching.py`:
  - Líneas 8-22: Linear Search
  - Líneas 38-52: Binary Search
- `algorithms/shelf_algorithms.py`:
  - Líneas 11-23: Fuerza Bruta
  - Líneas 38-51: Backtracking
  - Líneas 56-65: Función backtrack interna
- `algorithms/recursion.py`:
  - Líneas 8-22: Recursión de Pila
  - Líneas 39-54: Recursión de Cola

**Docstrings en métodos principales:** `library_manager.py`
- Líneas 68-80: `load_initial_inventory()`
- Líneas 140-158: `add_book()`
- Líneas 174-186: `get_book_by_isbn()`
- Líneas 192-205: `search_books()`
- Líneas 452-466: `loan_book()`
- Líneas 492-506: `return_book()`
- Líneas 553-567: `reserve_book()`
- Líneas 612-627: `find_risky_shelf_combinations()`
- Líneas 630-644: `find_optimal_shelf_assignment()`
- Líneas 650-663: `get_author_total_value()`
- Líneas 666-679: `get_author_average_weight()`
- Líneas 685-696: `generate_global_inventory_report()`

---

### 16. Informes y Video

**Generación de reporte global:** `library_manager.py`
- **Método generate_global_inventory_report():** Líneas 685-717
- **Guardado de reporte:** Líneas 719-730
  ```python
  def save_global_report(self, filepath: str = "reports/global_inventory_report.txt")
  ```

**Guion de video:** `GUION_VIDEO_ORDENAMIENTO_BUSQUEDA.md`
- Documento completo con guion en español e inglés

---

## RESUMEN DE ARCHIVOS CLAVE

| Requisito | Archivo Principal | Líneas Clave |
|-----------|------------------|--------------|
| Adquisición de Datos | `utils/file_handler.py` | 16-95 |
| Listas Maestras | `library_manager.py` | 48-49, 88-92, 165-170 |
| Stack (Pilas) | `data_structures/stack.py` | 7-100 |
| Queue (Colas) | `data_structures/queue.py` | 7-100 |
| Insertion Sort | `algorithms/sorting.py` | 7-35 |
| Merge Sort | `algorithms/sorting.py` | 38-93 |
| Linear Search | `algorithms/searching.py` | 7-34 |
| Binary Search | `algorithms/searching.py` | 37-66 |
| Fuerza Bruta | `algorithms/shelf_algorithms.py` | 10-34 |
| Backtracking | `algorithms/shelf_algorithms.py` | 37-95 |
| Recursión Pila | `algorithms/recursion.py` | 7-33 |
| Recursión Cola | `algorithms/recursion.py` | 36-78 |
| POO | `models/book.py`, `models/user.py`, `models/shelf.py` | Todas |
| Modularidad | Estructura de carpetas completa | - |
| Documentación | Todos los archivos | Docstrings completos |

---

## NOTAS PARA LA SUSTENTACIÓN

1. **Navegación rápida:** Usa Ctrl+G (o Cmd+G en Mac) en tu editor para ir directamente a las líneas mencionadas.

2. **Demostraciones sugeridas:**
   - Mostrar la estructura de carpetas completa
   - Ejecutar `load_initial_inventory()` y mostrar ambas listas
   - Hacer push/pop en Stack y enqueue/dequeue en Queue
   - Agregar un libro y mostrar cómo Insertion Sort mantiene el orden
   - Generar reporte global con Merge Sort
   - Buscar por título/autor con Linear Search
   - Buscar por ISBN con Binary Search y mostrar conexión con reservas
   - Ejecutar Fuerza Bruta y mostrar combinaciones
   - Ejecutar Backtracking y mostrar solución óptima
   - Ejecutar recursión de pila y cola con salida por consola

3. **Puntos críticos a destacar:**
   - Binary Search conectado con verificación de reservas (líneas 512-530)
   - Insertion Sort se ejecuta automáticamente al agregar libros
   - Queue solo permite reservas cuando stock = 0
   - Stack almacena historial con ISBN y fecha
   - Backtracking muestra exploración y poda
   - Recursión de cola muestra acumuladores en consola

---

**Última actualización:** Generado automáticamente para facilitar la sustentación del proyecto.

