# 🎬 GUION PARA VIDEO: ALGORITMOS DE ORDENAMIENTO Y BÚSQUEDA

## Duración estimada: 2-3 minutos

---

## INTRODUCCIÓN (15 segundos)

"En esta sección, presentaré los algoritmos de ordenamiento y búsqueda implementados en nuestro Sistema de Gestión de Bibliotecas. Estos algoritmos son fundamentales para mantener los datos organizados y permitir búsquedas eficientes."

---

## PARTE 1: ALGORITMOS DE ORDENAMIENTO (1 minuto)

### Insertion Sort (30 segundos)

"Nuestro sistema implementa **Insertion Sort** para mantener el Inventario Ordenado siempre ordenado por ISBN. 

Este algoritmo se ejecuta automáticamente cada vez que agregamos un nuevo libro al sistema. Funciona comparando cada elemento con los anteriores e insertándolo en su posición correcta.

La ventaja de Insertion Sort es que es eficiente para listas pequeñas o parcialmente ordenadas, con una complejidad de O(n²) en el peor caso, pero O(n) cuando la lista ya está ordenada.

En nuestro código, lo encontramos en `algorithms/sorting.py`, y se utiliza en `library_manager.py` para mantener la lista ordenada incrementalmente."

### Merge Sort (30 segundos)

"Para generar el Reporte Global de Inventario ordenado por valor, implementamos **Merge Sort**, un algoritmo de divide y vencerás.

Merge Sort divide la lista en mitades recursivamente hasta tener listas de un elemento, y luego las combina en orden. Tiene una complejidad garantizada de O(n log n), lo que lo hace muy eficiente para listas grandes.

Este algoritmo es ideal para nuestro reporte porque necesitamos ordenar todos los libros por su valor en pesos colombianos, y Merge Sort garantiza un ordenamiento estable y eficiente.

La implementación incluye una función auxiliar `_merge` que combina dos listas ordenadas en una sola lista ordenada."

---

## PARTE 2: ALGORITMOS DE BÚSQUEDA (1 minuto)

### Linear Search (30 segundos)

"Para búsquedas por título o autor, implementamos **Linear Search** o búsqueda lineal.

Este algoritmo recorre secuencialmente el Inventario General, que es una lista desordenada que refleja el orden de carga de los datos. Linear Search es perfecto para este caso porque no requiere que la lista esté ordenada.

La función retorna todas las coincidencias encontradas, no solo la primera, lo que permite al usuario ver todos los libros que coinciden con su búsqueda. Tiene una complejidad de O(n), donde n es el número de libros en el inventario.

La búsqueda es case-insensitive, lo que mejora la experiencia del usuario."

### Binary Search (30 segundos)

"Para búsquedas por ISBN, utilizamos **Binary Search** o búsqueda binaria, que es mucho más eficiente.

Este algoritmo requiere que la lista esté ordenada, por lo que lo aplicamos sobre nuestro Inventario Ordenado, que se mantiene ordenado por ISBN usando Insertion Sort.

Binary Search divide la lista a la mitad en cada iteración, comparando el elemento del medio con el valor buscado. Esto reduce significativamente el número de comparaciones, con una complejidad de O(log n).

**Un aspecto crítico** de nuestra implementación es que Binary Search se usa no solo para encontrar libros, sino también para verificar si un libro devuelto tiene reservas pendientes en la cola de espera, permitiendo asignación automática según prioridad FIFO."

---

## CONCLUSIÓN (15 segundos)

"En resumen, nuestro sistema utiliza Insertion Sort para mantener el orden incremental, Merge Sort para reportes eficientes, Linear Search para búsquedas flexibles por título o autor, y Binary Search para búsquedas rápidas por ISBN y gestión de reservas.

La combinación de estos algoritmos garantiza un sistema eficiente y funcional que cumple con todos los requisitos del proyecto."

---

## NOTAS PARA LA GRABACIÓN

### Puntos clave a destacar:
- ✅ Insertion Sort se ejecuta automáticamente al agregar libros
- ✅ Merge Sort garantiza O(n log n) para reportes grandes
- ✅ Linear Search funciona con listas desordenadas
- ✅ Binary Search es crítico para verificar reservas
- ✅ Mencionar las ubicaciones de los archivos (`algorithms/sorting.py` y `algorithms/searching.py`)

### Demostración sugerida:
1. Mostrar el código de Insertion Sort mientras explicas
2. Mostrar cómo Merge Sort divide y combina listas
3. Ejecutar una búsqueda lineal por título
4. Ejecutar una búsqueda binaria por ISBN y mostrar cómo verifica reservas

### Tono:
- Profesional pero accesible
- Técnico pero claro
- Enfocado en la aplicación práctica en el proyecto

---

## VERSIÓN EN INGLÉS (English Version)

# 🎬 SCRIPT FOR VIDEO: SORTING AND SEARCHING ALGORITHMS

## Estimated duration: 2-3 minutes

---

## INTRODUCTION (15 seconds)

"In this section, I will present the sorting and searching algorithms implemented in our Library Management System. These algorithms are fundamental for keeping data organized and enabling efficient searches."

---

## PART 1: SORTING ALGORITHMS (1 minute)

### Insertion Sort (30 seconds)

"Our system implements **Insertion Sort** to keep the Ordered Inventory always sorted by ISBN.

This algorithm runs automatically every time we add a new book to the system. It works by comparing each element with previous ones and inserting it in its correct position.

The advantage of Insertion Sort is that it's efficient for small or partially sorted lists, with O(n²) complexity in the worst case, but O(n) when the list is already sorted.

In our code, you can find it in `algorithms/sorting.py`, and it's used in `library_manager.py` to maintain the list incrementally sorted."

### Merge Sort (30 seconds)

"To generate the Global Inventory Report sorted by value, we implemented **Merge Sort**, a divide-and-conquer algorithm.

Merge Sort divides the list into halves recursively until we have single-element lists, then combines them in order. It has a guaranteed O(n log n) complexity, making it very efficient for large lists.

This algorithm is ideal for our report because we need to sort all books by their value in Colombian pesos, and Merge Sort guarantees stable and efficient sorting.

The implementation includes an auxiliary `_merge` function that combines two sorted lists into one sorted list."

---

## PART 2: SEARCHING ALGORITHMS (1 minute)

### Linear Search (30 seconds)

"For searches by title or author, we implemented **Linear Search**.

This algorithm sequentially traverses the General Inventory, which is an unordered list that reflects the order of data loading. Linear Search is perfect for this case because it doesn't require the list to be sorted.

The function returns all matches found, not just the first one, allowing users to see all books that match their search. It has O(n) complexity, where n is the number of books in the inventory.

The search is case-insensitive, which improves user experience."

### Binary Search (30 seconds)

"For ISBN searches, we use **Binary Search**, which is much more efficient.

This algorithm requires the list to be sorted, so we apply it to our Ordered Inventory, which is kept sorted by ISBN using Insertion Sort.

Binary Search divides the list in half at each iteration, comparing the middle element with the searched value. This significantly reduces the number of comparisons, with O(log n) complexity.

**A critical aspect** of our implementation is that Binary Search is used not only to find books, but also to verify if a returned book has pending reservations in the waiting queue, enabling automatic assignment according to FIFO priority."

---

## CONCLUSION (15 seconds)

"In summary, our system uses Insertion Sort to maintain incremental order, Merge Sort for efficient reports, Linear Search for flexible searches by title or author, and Binary Search for fast ISBN searches and reservation management.

The combination of these algorithms ensures an efficient and functional system that meets all project requirements."

---

## RECORDING NOTES

### Key points to highlight:
- ✅ Insertion Sort runs automatically when adding books
- ✅ Merge Sort guarantees O(n log n) for large reports
- ✅ Linear Search works with unordered lists
- ✅ Binary Search is critical for verifying reservations
- ✅ Mention file locations (`algorithms/sorting.py` and `algorithms/searching.py`)

### Suggested demonstration:
1. Show Insertion Sort code while explaining
2. Show how Merge Sort divides and combines lists
3. Execute a linear search by title
4. Execute a binary search by ISBN and show how it verifies reservations

### Tone:
- Professional but accessible
- Technical but clear
- Focused on practical application in the project

