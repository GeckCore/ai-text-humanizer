import sys
import msvcrt
import time

# Biblioteca de snippets pre-programados
SNIPPETS = {
    "1": ("Suma Básica", """def suma_operacion(a, b):
    \"\"\"Calcula la suma de dos números.\"\"\"
    resultado = a + b
    print(f"El resultado de {a} + {b} es: {resultado}")
    return resultado

# Ejemplo de uso
suma_operacion(10, 5)"""),
    
    "2": ("Matrices (NumPy style)", """import numpy as np

def crear_matriz_identidad(n):
    # Genera una matriz identidad de nxn
    matriz = np.eye(n)
    print("Matriz Identidad:")
    print(matriz)
    return matriz

def multiplicacion_matrices(A, B):
    # Multiplicación matricial estándar
    return np.dot(A, B)

# Ejecución
A = crear_matriz_identidad(3)
B = np.random.rand(3, 3)
print(multiplicacion_matrices(A, B))"""),
    
    "3": ("Algoritmo de Ordenamiento", """def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    der = [x for x in lista if x > pivote]
    return quicksort(izq) + centro + quicksort(der)

datos = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista ordenada: {quicksort(datos)}")""")
}

def simulador_escritura():
    print("--- VS CODE SIMULATOR (MODO HACKER) ---")
    print("Selecciona un snippet para 'escribir':")
    for key, value in SNIPPETS.items():
        print(f"{key}. {value[0]}")
    
    opcion = input("\nElige el número: ")
    
    if opcion not in SNIPPETS:
        print("Opción no válida.")
        return

    titulo, codigo = SNIPPETS[opcion]
    print(f"\n--- Preparado para escribir: {titulo} ---")
    print("Pulsa cualquier tecla repetidamente para generar el código...\n")

    for char in codigo:
        # Espera a que se pulse cualquier tecla
        if msvcrt.kbhit:
            msvcrt.getch() 
            sys.stdout.write(char)
            sys.stdout.flush()
            
    print("\n\n[Escritura completada]")

if __name__ == "__main__":
    try:
        simulador_escritura()
    except KeyboardInterrupt:
        print("\nSimulación interrumpida.")


