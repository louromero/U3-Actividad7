from Personal import Personal

class Docente(Personal):
    __carrera=""
    __cargo=""
    __catedra=""

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def restoCalculo(self):
        cargo= self.getCargo().lower()
        porcentaje =  (self.getAntiguedad() / 100)
        if cargo == "simple":
            porcentaje += 0.10
        elif cargo == "semiexclusivo":
            porcentaje += 0.20
        elif cargo == "exclusivo":
            porcentaje += 0.50
        retorno =  (self.getSueldoBasico() * porcentaje)
        return retorno

    def __str__(self):
        cad  = super().__str__()
        cad += " {:<15} {:<15} {:<15}".format(self.getCarrera()[0:14].title(),self.getCargo()[0:14].title(),self.getCatedra()[0:14].title())
        return cad

    def toJson(self):
        d = dict(__class__ = self.__class__.__name__,
                 __atributos__ = dict(
                     cuil       = self.getCuil(),
                     nombre     = self.getNombre(),
                     apellido   = self.getApellido(),
                     sueldoB    = self.getSueldoBasico(),
                     antiguedad = self.getAntiguedad(),
                     carrera    = self.getCarrera(),
                     cargo      = self.getCargo(),
                     catedra    = self.getCatedra(),
                 ))
        return d