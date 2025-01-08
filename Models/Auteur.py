from Personne import *
from re import *
class Auteur(Perssonne):
    def _init_(self, nom, prenom, code):
        if match(code, "^A[0-9]{4}$"):
            super()._init_(nom, prenom)
            self.__code = code
        else:
            raise Exception("Code invalide")
    def getCode(self):
        return self.__code
    def setCode(self, code):
        if match(code, "^A[0-9]{4}$"):
            self.__code = code
        else:
            raise Exception("Code invalide")
    def __str__(self):
        return f"L'auteur {self.getCode()} : " + super().__str__()
    