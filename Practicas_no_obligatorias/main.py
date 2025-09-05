nombre = str(input("Indique su nombre: "))
edad = int(input("Indique su edad: "))
atracciones_que_usara = int(input("Indique cuantas atracciones desea usar: "))
gasto_en_atracciones = 0
lista_de_atracciones = "\n"

while True:

    if atracciones_que_usara == 0 :
        break
    elif atracciones_que_usara > 0 :
        atraccion_en_uso = int(input("""Que atraccion desea utilizar?
        1.Montaña rusa
        2.Casa del Terror
        3.Carrusel
        Indique con un numero : """))
        if atraccion_en_uso == 1 :
            if edad >= 12 :
                print("Tiene la edad necesaria para subir a la atraccion")
                print("Acaba de subirse a la Montaña Rusa, el costo es de $1500")
                lista_de_atracciones += "Montaña Rusa \n"
                gasto_en_atracciones += 1500
                atracciones_que_usara -= 1
            else :
                print("No tiene la edad suficiente para subir a la Montaña Rusa")
        elif atraccion_en_uso == 2 :  
                if edad > 6 :
                    print("Acaba de entrar a la Casa del Terror, el costo es de $1200")
                    lista_de_atracciones += "Casa del Terror \n"
                    gasto_en_atracciones += 1200    
                    atracciones_que_usara -= 1
                else :
                    print("No tiene la edad suficiente para entrar a la Casa del Terror")
        elif atraccion_en_uso == 3 :    
            print("Acaba de entrar al Carrusel, el costo es de $800")
            lista_de_atracciones += "Carrusel \n"
            gasto_en_atracciones += 800
            atracciones_que_usara -= 1

Resumen = print(f"""Resumen final de su visitar por PythonLand:
-Nombre: {nombre}
-Lista De Atracciones que eligio : {lista_de_atracciones}
-Total a Pagar : {gasto_en_atracciones}
""")