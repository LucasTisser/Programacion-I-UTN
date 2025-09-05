def verificar_acceso(edad:int) -> bool:
    if edad >= 18:
        print("Es mayor de edad")
    else: 
        print("Es menor de edad")

edad = int(input("Ingrese su edad : "))

verificar_acceso(edad)