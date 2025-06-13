print("Calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

resultado = 0

while True:
    opt = int(input("Ingrese la opcion: "))
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    
    if opt == 1:
        resultado = num1 + num2
        print(f"El reusltado es: ")
    elif opt == 2:
        