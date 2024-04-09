def calcular_area_triangulo(lado, altura):
    area = 0.5 * lado * altura
    return area

# Solicitar al usuario que ingrese la medida del lado y la altura relativa a ese lado
lado = float(input("Ingrese la medida de un lado del triángulo: "))
altura = float(input("Ingrese la altura relativa al lado ingresado: "))

# Calcular el área del triángulo
area_triangulo = calcular_area_triangulo(lado, altura)

# Mostrar el resultado al usuario
print("El área del triángulo es:", area_triangulo)
