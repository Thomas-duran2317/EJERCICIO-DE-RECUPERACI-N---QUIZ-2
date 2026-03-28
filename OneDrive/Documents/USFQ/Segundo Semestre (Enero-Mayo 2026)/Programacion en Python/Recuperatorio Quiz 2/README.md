
Thomas Duran 
Descripción del algoritmo Bubble Sort

El algoritmo Bubble Sort es un método de ordenamiento que compara elementos adyacentes de una lista y los intercambia si están en el orden incorrecto.
Este proceso se repite varias veces hasta que todos los elementos estén ordenados.
En cada pasada, el número más grande se mueve hacia el final de la lista, como si “burbujea” hacia arriba, por eso se llama ordenamiento burbuja.

Complejidad Computacional: 

La complejidad del algoritmo Bubble Sort es:
Peor caso: O(n²)
Caso promedio: O(n²)
Mejor caso: O(n) (cuando la lista ya está ordenada, si se usa una optimización)

¿Por qué tiene complejidad O(n²)?
Porque el algoritmo usa dos bucles (for):
Un bucle recorre toda la lista. El otro bucle compara los elementos adyacentes.

Entonces:
Si hay n elementos, se hacen aproximadamente n × n = n² comparaciones.

¿Qué pasa con el tiempo si la lista tiene 10 vs 100 elementos?
Si la lista tiene 10 elementos → 10² = 100 operaciones aprox.
Si la lista tiene 100 elementos → 100² = 10,000 operaciones aprox.
Es decir, si aumentamos 10 veces la cantidad de elementos, el tiempo aumenta aproximadamente 100 veces, por eso Bubble Sort es un algoritmo lento para listas grandes.
