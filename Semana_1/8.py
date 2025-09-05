def calcular_edad(anio_nacimiento: int) -> int :
    anio_actual = 2025
    edad_calculada = 2025 - anio_nacimiento
    print(f"Su edad calculada es : {edad_calculada}")


nacimiento = int(input("Ingrese su año de nacimiento: "))
calcular_edad(nacimiento)