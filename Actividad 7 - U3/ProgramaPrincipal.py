from Menu import Menu
from ObjectEncoder import ObjectEncoder

if __name__=='__main__':
    jsonF=ObjectEncoder()
    diccionario=jsonF.leerJSONarchivo('personal.json')
    lista=jsonF.decodificarDiccionario(diccionario)
    menu=Menu()
    salir=False
    while not salir:
        print("\n----------------------------------MENU-----------------------------------")
        print("1. Insertar agente.")
        print("2. Agregar agente.")
        print("3. Mostrar tipo de agente por posicion dada.")
        print("4. Listrar docentes de investigadores dada una carrera.")
        print("5. Contar cantidad de investigadores en un area.")
        print("6. Listar agentes.")
        print("7. Listar por categoria dada.")
        print("8. Almacenar los objetos en memoria.")
        print("0. Salir.")
        print("---------------------------------------------------------------------------------\n")
        opcion=int(input("Ingrese opcion: "))
        menu.opcion(opcion,lista)
        salir=opcion==0