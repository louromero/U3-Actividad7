import json
from pathlib import Path
from Lista import Lista
from PersonalApoyo import PersonalApoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador

class ObjectEncoder:
    def guardarJSONarchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
        destino.close

    def leerJSONarchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
        fuente.close()
        return diccionario

    def decodificarDiccionario(self,diccionario):
        if '__class__' not in diccionario:
            return diccionario
        else:
            class_name = diccionario['__class__']
        class_= eval(class_name)
        if class_name=='lista':
            lista=diccionario['personal']
        manejador=class_()
        for i in range(len(lista)):
            dPersonal  = lista[i]
            class_name = dPersonal.pop('__class__')
            class_ = eval(class_name)
            atributos  = dPersonal['__atributos__']
            unPersonal = class_(**atributos)
            manejador.agregar(unPersonal)
        return manejador