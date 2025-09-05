nombre = ""
edad = 0
gasto_en_atracciones = 0
lista_de_atracciones = "\n"


def menu_principal() -> str :
    menu_parque = int(input("""Indique una opcion:
    1. Elegir para subir a una atraccion.
    2. Consultar precio de una atraccion.
    3. Ver informacion del visitante
    4. Ver resumen de atracciones elegidas y salir.\n"""))
    opcion_elegida(menu_parque)

def opcion_elegida(opcion_elegida) :
    opcion = opcion_elegida
    if opcion == 1 :
        subir_atraccion()
    elif opcion == 2 :
        mostrar_precios()
        menu_principal()
    elif opcion == 3 :
        mostrar_resumen()
        menu_principal()
    elif opcion == 4 :
        resumen = registrar_visita()
        return resumen
    else :
        print("ghoal")

def registrar_visitante() -> str :
    global nombre, edad
    nombre = str(input("Indique su nombre: "))
    edad = int(input("Indique su edad: "))
    return nombre, edad

def mostrar_atracciones() -> str :
    atraccion_elegida = int(input("""Que atraccion desea subir?
        1.Montaña rusa
        2.Casa del Terror
        3.Carrusel
        4.Cancelar
        """))
    if atraccion_elegida == 4:
        menu_principal()
    return atraccion_elegida

def puede_subir(edad_ingresada, atraccion) -> bool :
    global edad
    if atraccion == 1 :
        if edad_ingresada >= 12 :
            print("Tiene la edad necesaria para subir a la atraccion")
            print("Acaba de subirse a la Montaña Rusa, el costo es de $1500")
            return True
        else :
            print("No tiene la edad suficiente para subir a la Montaña Rusa")
            print("Volviendo al Menu Principal. . .")
            return False
    elif atraccion == 2 :  
        if edad_ingresada > 6 :
            print("Acaba de entrar a la Casa del Terror, el costo es de $1200")
            return True
        else :
            print("No tiene la edad suficiente para entrar a la Casa del Terror")
            print("Volviendo al Menu Principal. . .")
            return False
    elif atraccion == 3 :    
        print("Acaba de entrar al Carrusel, el costo es de $800")
    return True

def mostrar_precios() -> str :
    precios = print("""
    Montaña Rusa - $1500
    Casa del Terror - $1200
    Carrusel - $800
    """)
    return precios

def calcular_precio(atraccion) -> float :
    global lista_de_atracciones, gasto_en_atracciones
    if atraccion == 1 :
        lista_de_atracciones += "Montaña Rusa \n"
        gasto_en_atracciones += 1500
    elif atraccion == 2 :  
        lista_de_atracciones += "Casa del Terror \n"
        gasto_en_atracciones += 1200    
    else:
        lista_de_atracciones += "Carrusel \n"
        gasto_en_atracciones += 800

def subir_atraccion() -> str :
    global edad
    atraccion_elegida = mostrar_atracciones()
    sube_o_no = puede_subir(edad, atraccion_elegida)
    if sube_o_no == False :
        menu_principal()
    else : 
        calcular_precio(atraccion_elegida)
        menu_principal()

def registrar_visita() -> str :
    global nombre , lista_de_atracciones, gasto_en_atracciones
    resumen = print(f"""Resumen de su visita por PythonLand:
    -Nombre: {nombre}
    -Lista De Atracciones que eligio : {lista_de_atracciones}
    -Total a Pagar : {gasto_en_atracciones}
    """)
    return resumen

def mostrar_resumen() -> str : 
    global nombre, edad
    print(f"""
    Nombre : {nombre}
    Edad : {edad}
    """)