# Cálculo del IMC - (Índice de Masa Corporal)
# El cálculo se realizará según el peso en kg y la altura en metros.
# Los valores se ingresan en kg y centímetros de altura.

# Valores de prueba
peso = 81
altura_cm = 178

# Convierte la altura de cm a metros
altura = altura_cm / 100

# Calcula el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Clasifica el IMC según los rangos de la OMS.
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"

# Determina el estado nutricional de la persona
def estado_nutricional(peso, altura):
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)
    return imc, clasificacion

# Cálculo y clasificación de IMC para los valores de prueba
imc, clasificacion = estado_nutricional(peso, altura)

# Output para los valores de prueba
print(f"Su IMC es: {imc:.2f}")
print(f"La clasificación OMS es: {clasificacion}")

# ------------------------------------------------------------- #

# Solicitar datos al usuario
peso = float(input("Ingrese el peso en kg: "))
altura_cm = float(input("Ingrese la altura en centímetros: "))

# Convierte la altura de cm a metros
altura = altura_cm / 100

# Cálculo y clasificación de IMC para los valores ingresados por el usuario
imc, clasificacion = estado_nutricional(peso, altura)

# Output para los valores ingresados por el usuario
print(f"Su IMC es: {imc:.2f}")
print(f"Su clasificación según la OMS es: {clasificacion}")






