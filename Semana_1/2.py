def operaciones(num1:int , num2:int) -> int :
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    print(f"""
    La suma de los de los numeros es : {suma}
    La resta de los numeros es : {resta}
    La multiplicacion de los numeros es : {multiplicacion}
    """)

numero1 = int(input("Ingrege el primer numero : "))
numero2 = int(input("Ingrege el Segundo numero : "))

operaciones(numero1, numero2)