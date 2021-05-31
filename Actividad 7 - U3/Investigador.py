from Personal import Personal

class Investigador(Personal):
    __area=""
    __tipo=""

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,area,tipo):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__area=area
        self.__tipo=tipo

    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def restoCalculo(self):
        retorno = self.getSueldoBasico() * (self.getAntiguedad() / 100)
        return retorno

    def __str__(self):
        cad  = super().__str__()
        cad += " {:<15} {:<15}".format(self.getTipo()[0:15],self.getArea()[0:15].title())
        return cad

    def toJson(self):

        d = dict(__class__ = self.__class__.__name__,
                 __atributos__ = dict(
                     cuil       = self.getCuil(),
                     nombre     = self.getNombre(),
                     apellido   = self.getApellido(),
                     sueldoB    = self.getSueldoBasico(),
                     antiguedad = self.getAntiguedad(),
                     area       = self.getArea(),
                     tipoInv    = self.getTipo()
                 ))

        return d