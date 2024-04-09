def calcular_horas_extra(salario_mensual_bruto, horas_extra_trabajadas):
    # Calcular el salario por hora normal
    salario_por_hora_normal = salario_mensual_bruto / (35 * 4)  # 35 horas por semana, 4 semanas por mes

    # Inicializar el importe de las horas extra
    importe_horas_extra = 0

    # Calcular importe de las horas extra según las normas administrativas
    if horas_extra_trabajadas <= 7:  # No hay horas extra entre la 36ª y la 43ª
        importe_horas_extra += salario_por_hora_normal * 1.25 * horas_extra_trabajadas
    elif horas_extra_trabajadas <= 8:  # Horas extra entre la 36ª y la 43ª
        importe_horas_extra += salario_por_hora_normal * 1.25 * 7
        importe_horas_extra += salario_por_hora_normal * 1.5 * (horas_extra_trabajadas - 7)
    else:  # Horas extra a partir de la 44ª
        importe_horas_extra += salario_por_hora_normal * 1.25 * 7
        importe_horas_extra += salario_por_hora_normal * 1.5 * 1
        importe_horas_extra += salario_por_hora_normal * 1.5 * (horas_extra_trabajadas - 8)

    return importe_horas_extra

# Solicitar al usuario que ingrese el salario mensual bruto y la cantidad de horas extra trabajadas
salario_mensual_bruto = float(input("Ingrese el salario mensual bruto: "))
horas_extra_trabajadas = int(input("Ingrese la cantidad de horas extra trabajadas: "))

# Calcular el importe de las horas extra
importe_horas_extra = calcular_horas_extra(salario_mensual_bruto, horas_extra_trabajadas)

# Mostrar el resultado al usuario
print("El importe de las horas extra a pagar es:", importe_horas_extra)
