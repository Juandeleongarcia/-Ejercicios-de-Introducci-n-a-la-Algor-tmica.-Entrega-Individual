def calcular_media_ponderada(nums, pesos):
    total_pesos = sum(pesos)
    producto_suma = sum([num * peso for num, peso in zip(nums, pesos)])
    media_ponderada = producto_suma / total_pesos
    return media_ponderada

# Solicitar al usuario que ingrese los números y sus respectivos pesos
nums = []
pesos = []
for i in range(3):
    num = float(input(f"Ingrese el número {i+1}: "))
    peso = float(input(f"Ingrese el peso del número {i+1}: "))
    nums.append(num)
    pesos.append(peso)

# Calcular la media ponderada
media_ponderada = calcular_media_ponderada(nums, pesos)

# Mostrar el resultado al usuario
print("La media ponderada de los números dados es:", media_ponderada)
