import abc
from abc import ABC

class Personal(ABC):
    __cuil=0
    __apellido=""
    __nombre=""
    __sueldoBasico=0.00
    __antiguedad=0

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,*args):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoBasico=sueldoBasico
        self.__antiguedad=antiguedad
        for x in args:
            del x

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad

    def getSueldo(self):
        return self.__sueldoBasico+self.restoCalculo()

    @abc.abstractclassmethod
    def restoCalculo(self):
        pass

    def __str__(self):
        sueldo="{:.2f}".format(self.getSueldo())
        antiguedad="{} anios".format(self.getAntiguedad())
        cadena="{:<15} {:<15} {:<15} {:<15} {:<15}".format(self.getNombre()[0:14].title,self.getApellido()[0:14].title,self.getCuil(),antiguedad,sueldo)
        return cadena