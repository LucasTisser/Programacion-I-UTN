def buscar_mayor(num1:int, num2:int, num3:int) -> int :
    if (num1 > num2) and (num1 > num3):
        if num2 > num3:
            print(f"""
            {num1}
            {num2}
            {num3}""")
        elif num3 > num2:
            print(f"""
            {num1}
            {num3}
            {num2}""")
    elif (num2 > num1) and (num2 > num3):
        if num1 > num3:
            print(f"""
            {num2}
            {num1}
            {num3}""")
        elif num3 > num1:
            print(f"""
            {num2}
            {num3}
            {num1}""")
    elif (num3 > num1) and (num3 > num2):
        if num1 > num2:
            print(f"""
            {num3}
            {num1}
            {num2}""")
        elif num2 > num1:
            print(f"""
            {num3}
            {num2}
            {num1}""")

numero1 = int(input("Ingrese el primer numero : "))
numero2 = int(input("Ingrese el segundo numero : "))
numero3 = int(input("Ingrese el tercer numero : "))

buscar_mayor(numero1, numero2, numero3)