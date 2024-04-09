def calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva):
    impuestos = precio_sin_impuestos * (porcentaje_iva / 100)
    precio_con_impuestos = precio_sin_impuestos + impuestos
    return precio_con_impuestos

# Solicitar al usuario el precio sin impuestos y el porcentaje de IVA
precio_sin_impuestos = float(input("Ingrese el precio sin impuestos: "))
porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))

# Calcular el precio con todos los impuestos incluidos
precio_con_impuestos = calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva)

# Mostrar el resultado al usuario
print("El precio con todos los impuestos incluidos es:", precio_con_impuestos)
