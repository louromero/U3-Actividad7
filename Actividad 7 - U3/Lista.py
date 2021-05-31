from Nodo import Nodo
from Docente import Docente
from Investigador import Investigador
from PersonalApoyo import PersonalApoyo
from DocenteInvestigador import DocenteInvestigador

class Lista:
    __comienzo=None
    __actual=None
    __index=0
    __tope=0


    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__index=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index==self.__tope:
            self.__actual=self.__comienzo
            self.__index=0
            raise StopIteration
        else:
            self.__index+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def getNodo(self,pos):
        band = False
        retorno = None

        if pos <= self.__tope:
            while not band and self.__index <= self.__tope:
                if pos == self.__index:
                    retorno = self.__actual.getDato()
                    band = True
                else:
                    self.__actual = self.__actual.getSiguiente()
                    self.__index += 1

        if band == False:
            print("No encontrado")
        else:
            print("Encontrado")

        self.__actual = self.__comienzo
        self.__index  = 0
        return retorno

    def crearPersonal(self):
        band=False
        nuevoPersonal=None
        op=0
        while not band:
            print("\n----------------------------------------")
            print("1. Personal de Apoyo\n2. Docente\n3. Investigador\n4. Docente Investigador")
            print("----------------------------------------------------")
            while op not in [1,2,3,4]:
                try:
                    op=int(input("\nIngrese opcion: "))
                    if op not in [1,2,3,4]:
                        raise ValueError
                except ValueError:
                    print("\nEror, intente de nuevo.")
            cuil=int(input("Cuil: "))
            apellido=input("Apellido: ")
            nombre= input("Nombre: ")
            sueldoB=float(input("Sueldo Base: "))
            antiguedad=int(input("Antiguedad: "))
            if op == 1:
                band = True
                while band:
                    try:
                        categoria= int(input("Categoria: "))
                    except ValueError:
                        print("\nValor erroneo, intentar de nuevo")
                    else: band = False
                nuevoPersonal = PersonalApoyo(cuil,apellido,nombre,sueldoB,antiguedad,categoria)
                band = True

            elif op == 2 or op == 4:
                carrera= input("Carrera: ")
                cargo= input("Cargo: ")
                catedra= input("Catedra: ")
                if op == 2:
                    nuevoPersonal = Docente(cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra)
                band = True

            if op == 3 or op == 4:
                area= input("Area: ")
                tipoI= input("Tipo de investigacion: ")
                if op == 3:
                    nuevoPersonal = Investigador(cuil, apellido, nombre, sueldoB, antiguedad,area,tipoI)
                band = True

            if op == 4:
                band = False
                while not band:
                    try:
                        importeE= float(input("Importe extra: "))
                        if importeE < 0:
                            raise ValueError
                    except ValueError:
                        print("Valor erroneo, intente de nuevo")
                    else: band = True
                categoria = input("Categoria: ")
                nuevoPersonal = DocenteInvestigador(cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra,area,tipoI,importeE, categoria)

        return nuevoPersonal


    def insertar(self,posicion,elemento):
        band=False
        bandera=False
        anterior=None
        if posicion>self.__tope:
            print("\nPosicion fuera de alcance. ")
            band=True
        if band==False:
            if posicion==0:
                band=True
                self.__tope+=1
                nuevoNodo=Nodo(elemento)
                if self.__comienzo is None:
                    self.__comienzo=nuevoNodo
                else:
                    nuevoNodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nuevoNodo
            else:
                anterior=self.__actual
                self.__actual=self.__actual.getSiguiente()
                self.__index+=1

            while not bandera and self.__index<=self.__tope:
                if self.__index==posicion:
                    nuevoNodo=None(elemento)
                    nuevoNodo.setSiguiente(self.__actual)
                    anterior.setSiguiente(nuevoNodo)
                    self.__tope+=1
                    bandera=True
                else:
                    anterior=self.__actual
                    self.__actual=self.__actual.getSiguiente()
                    self.__index+=1
        self.__actual=self.__comienzo
        self.__index=0

    def agregar(self,elemento):
        nodo=Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=self.__comienzo
        self.__tope+=1

    def mostrarTipo(self,posicion):
        dato=self.getNodo(posicion)
        nombre=dato.__class__.__name__
        print("\nEl objeto es de la clase {}".format(nombre))

    def listaPorCarrera(self,carrera):
        aux=[]
        for x in self:
            if isinstance(x,DocenteInvestigador):
                if x.getCarrera()==carrera:
                    aux.append(x)
        sorted(aux,key=lambda x:x.getNombre())
        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} |".format("Nombre", "Apellido", "Sueldo Basico", "Cuil", "Antiguedad","Tipo Inv","Area", "Carrera","Cargo",
                "Catedra"  ,"Categoria", "Importe Extra", "Sueldo" ))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for x in aux:
            print(x)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    def contarPorArea(self,area):
        cantDoce=0
        cantInv=0
        for x in self.__iter__():
            if isinstance (x,DocenteInvestigador):
                if x.getArea()==area:
                    cantDoce+=1
            elif isinstance(x,Investigador):
                if x.getArea()==area:
                    cantInv+=1
        print("\nHay {} docentes investigadores y {} investigadores".format(cantDoce,cantInv))

    def listar(self):
        aux = []
        for x in self.__iter__():
            aux.append(x)
        aux.sort(key=lambda x: x.getApellido())
        print("---------------------------------------------------------------------------")
        print(" {:<15} {:<15} {:<25} {:<15} |".format("Nombre","Apellido","Tipo","Sueldo"))
        print("---------------------------------------------------------------------------")
        for x in aux:
            sueldo = "{:,.2f}".format(x.getSueldo())
            print(" {:<15} {:<15} {:<25} {:<15} ".format(x.getNombre()[0:14].title(), x.getApellido()[0:14].title(), x.__class__.__name__[0:24], sueldo))
        print("---------------------------------------------------------------------------")

    def listarCategoria(self,categoria):
        total = 0
        print("-------------------------------------------------")
        print(" {:<15} {:<15} {:<15} |".format("Apellido", "Nombre", "Importe Extra"))
        print("-------------------------------------------------")
        for x in self:
            if isinstance(x,DocenteInvestigador):
                if x.getCategoria() == categoria:
                    print(x.getInfo())
                    total += x.getImporteExtra()
        print("-------------------------------------------------")
        total = "{:,.2f}".format(total)
        print("{:>49}|".format("Total a abonar: ${}".format(total)))
        print("-------------------------------------------------")

    def toJson(self):
        d = dict(
            __class__= self.__class__.__name__,
            personal= [personal.toJson() for personal in self.__iter__()]
        )
        return d