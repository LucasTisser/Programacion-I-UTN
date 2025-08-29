def area_triangulo(base:int, altura:int) -> int :
    area = (base * altura) / 2
    print(f"El area del triangulo es : {area}")

base = int(input("Ingrese una base para el triangulo: "))
altura = int(input("Ingrese una altura para el triangulo: "))

area_triangulo(base, altura)