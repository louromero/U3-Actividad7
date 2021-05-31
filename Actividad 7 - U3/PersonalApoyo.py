from Personal import Personal

class PersonalApoyo(Personal):
    __categoria=""

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__categoria=categoria

    def getCategoria(self):
        return self.__categoria

    def restoCalculo(self):
        porcentaje = 1 + (super().getAntiguedad() / 100)
        categoria  = self.getCategoria()
        if categoria >= 1 and categoria <= 10:
            porcentaje += 0.10
        elif categoria >= 11 and categoria <= 20:
            porcentaje += 0.20
        else:
            porcentaje += 0.30
        retorno = self.getSueldoBasico() * porcentaje
        return retorno

    def __str__(self):
        cad  = super().__str__()
        cad += " {:<15}".format( self.__categoria )
        return cad

    def restoCalculo(self):
        return 10

    #JSON
    def toJson(self):
        d = dict(__class__ = self.__class__.__name__,
                 __atributos__ = dict(
                     cuil       = self.getCuil(),
                     nombre     = self.getNombre(),
                     apellido   = self.getApellido(),
                     sueldoB    = self.getSueldoBasico(),
                     antiguedad = self.getAntiguedad(),
                     categoria  = self.getCategoria()
                 ))
        return d