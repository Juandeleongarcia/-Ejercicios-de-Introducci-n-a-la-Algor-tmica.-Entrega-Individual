def calcular_area_triangulo_rectangulo(lado1, lado2):
    area = 0.5 * lado1 * lado2
    return area

# Solicitar al usuario que ingrese las medidas de los dos lados perpendiculares
lado1 = float(input("Ingrese la medida de uno de los lados perpendiculares del triángulo rectángulo: "))
lado2 = float(input("Ingrese la medida del otro lado perpendicular del triángulo rectángulo: "))

# Calcular el área del triángulo rectángulo
area_triangulo_rectangulo = calcular_area_triangulo_rectangulo(lado1, lado2)

# Mostrar el resultado al usuario
print("El área del triángulo rectángulo es:", area_triangulo_rectangulo)
