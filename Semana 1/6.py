def convertir_minutos(minutos: int) -> int:
    cant_horas = int(minutos / 60) 
    cant_minutos = minutos % 60
    print(f"{minutos} minutos son {cant_horas} hora/s con {cant_minutos} minutos restantes")

minutos = int(input("Ingrese una cantidad de minutos: "))

convertir_minutos(minutos)