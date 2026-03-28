n = int(input("¿Cuántos números desea ingresar? "))
numeros = []
for i in range(n):
    num = int(input(f"Ingrese número {i+1}: "))
    numeros.append(num)
print("Lista original:", numeros)

for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Intercambio
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp

print("Lista ordenada:", numeros)