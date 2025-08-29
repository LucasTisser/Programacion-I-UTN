def es_par(num: int) -> bool:
    if num % 2 == 0 :
        print(f"El numero {num} es par")
        return True
    else:
        print(f"El numero {num} es impar")
        return False

numero = int(input("Ingrese un numero: "))
es_par(numero)