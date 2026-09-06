# Matriz de 3 filas x 4 columnas, con valor de 0 el cual representa un asiento vacío.
asientos = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]   
]
# Pedir al usuario el asiento que desea reservar
print("--- Reservar Asiento de Cine ---")
print("Escoger el asiento que desea reservar para filas del 0 al 2 y columnas del 0 al 3")
fila = int(input("Ingrese la fila (0-2): "))
columna = int(input("Ingrese la columna (0-3): "))

#Validar que el asiento reservado esté dentro del rango de la matriz y que el asiento esté disponible
if 0 <= fila < 3 and 0 <= columna < 4:
    # Marcar el asiento si está disponible
    asientos [fila][columna] = 1
    print(f"\nAsiento reservado en la fila {fila} y columna {columna}.")
else:
    print("\nPosición inválida. Por favor, ingrese una fila entre 0 y 2 y una columna entre 0 y 3.")

# Mostrar la matriz completa en formato de tabla usando bucles anidados
print("Estado de la sala de cine (0 = asiento vacío, 1 = asiento reservado):") 
for f in range(len(asientos)):
    for c in range(len(asientos[f])):
        print(asientos[f][c], end=" ")
    print()  # Salto de línea después de cada fila