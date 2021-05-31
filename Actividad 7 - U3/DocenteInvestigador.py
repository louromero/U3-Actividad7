from io import DEFAULT_BUFFER_SIZE
from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from PersonalApoyo import PersonalApoyo

class DocenteInvestigador(Docente,Investigador):
    __categoria=""
    __importeExtra=0.00

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,area,tipo,categoria,importe):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,area,tipo)
        self.__categoria=categoria
        self.__importeExtra=importe

    def getCategoria(self):
        return self.__categoria

    def getImporteExtra(self):
        return self.__importeExtra

    def restoCAlculo(self):
        return super().restoCalculo()+self.getImporteExtra

    def getInfo(self):
        importe = "{:,.2f}".format(self.getImporteExtra())
        return "| {:<15} {:<15} ${:<14} |".format(self.getApellido().title()[0:14],self.getNombre().title()[0:14],importe)

    def __str__(self):
        cadena1=super().__str__()
        categoria=self.getCategoria()
        importe="${:.2f}".format(self.getImporteExtra())
        total="${:.2f}".format(self.getSueldo())
        cadena1+="{} {} {}".format(categoria,importe,total)
        return cadena1

    def toJson(self):
        d = dict(__class__ = self.__class__.__name__,
                 __atributos__= dict(
                     cuil= self.getCuil(),
                     nombre= self.getNombre(),
                     apellido= self.getApellido(),
                     sueldoB= self.getSueldoBasico(),
                     antiguedad= self.getAntiguedad(),
                     area= self.getArea(),
                     tipoInv= self.getTipo(),
                     carrera= self.getCarrera(),
                     cargo= self.getCargo(),
                     catedra= self.getCatedra(),
                     categoria= self.getCategoria(),
                     importeExtra= self.getImporteExtra()
                 ))
        return d