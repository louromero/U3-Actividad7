class Nodo:
    __personal=None
    __siguiente=None

    def __init__(self,personal):
        self.__personal=personal

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self,sig):
        self.__siguiente=sig

    def getDato(self):
        return self.__personal