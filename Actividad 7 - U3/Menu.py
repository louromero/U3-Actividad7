from ObjectEncoder import ObjectEncoder

class Menu:
    __switcher=None

    def __init__(self):
        self.__switcher={ 1:self.opcion1,
                        2: self.opcion2,
                        3:self.opcion3,
                        4:self.opcion4,
                        5:self.opcion5,
                        6:self.opcion6,
                        7:self.opcion7,
                        8:self.opcion8,
                        9:self.salir
                        }
    def getSwitcher(self):
        return self.__switcher

    def opcion(self,op,lista):
        funcion=self.__switcher.get(op,lambda:print("\nOpcion no valida."))
        funcion(lista)

    #----------------------------------------------------------------------------------OPCION 1
    def opcion1(self,lista):
        try:
            posicion=int(input("\nPosicion: "))
            if posicion<0:
                raise ValueError
        except ValueError:
            print("\nPosicion Incorrecta.")
        else:
            personal=lista.crearPersonal()
            lista.insertar(posicion,personal)

    #----------------------------------------------------------------------------------OPCION 2
    def opcion2(self,lista):
        persona=lista.crearPersonal()
        lista.agregar(persona)

    #----------------------------------------------------------------------------------OPCION 3
    def opcion3(self,lista):
        posicion=int(input("\nPosicion: "))
        lista.MostrarTipo(posicion)

    #----------------------------------------------------------------------------------OPCION 4
    def opcion4(self,lista):
        carrera=input("\nCarrera: ")
        lista.listaPorCarrera(carrera)

    #----------------------------------------------------------------------------------OPCION 5
    def opcion5(self,lista):
        area=input("\nArea: ")
        lista.contarPorArea(area)

    #----------------------------------------------------------------------------------OPCION 6
    def opcion6(self,lista):
        lista.listar()

    #----------------------------------------------------------------------------------OPCION 7
    def opcion7(self,lista):
        categoria=input("\nCategoria: ")
        lista.listarCategoria(categoria)

    #----------------------------------------------------------------------------------OPCION 8
    def opcion8(self,lista):
        dic = lista.toJson()
        encoder = ObjectEncoder()
        try:
            encoder.guardarJSONArchivo(dic,"personal.json")
        except:
            print("\nError al guardar")
        else:
            print("\nGuardado exitoso")

    #----------------------------------------------------------------------------------SALIR
    def salir(self,lista):
        print("\nChau :)")