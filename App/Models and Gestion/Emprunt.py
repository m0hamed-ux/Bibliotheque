from Adherent import *
from datetime import *
class Emprunt:
    code=0
#---------constructeur---------    
    def __init__(self,livreEmprunte,EmprunteurLivre,dateEmprunt,dateRPrevue,dateREffective):
        Emprunt.code+=1
        if not isinstance(livreEmprunte,str):
            raise Exception("Le nom de livre est invalide!")
        elif not isinstance(EmprunteurLivre,Adherent):
            raise Exception("L'emprunteur du livre est invalide!")
        elif not isinstance(dateEmprunt,date) and dateEmprunt<date.today:
            raise Exception("La date d'emprunt est invalide!")
        elif not isinstance(dateRPrevue,date) and dateRPrevue>date.today:
            raise Exception("La date de retour prévue est invalide!")
        elif not isinstance(dateREffective,date):
            raise Exception("La date de retour effective est invalide!")
        else:
            self.__code=Emprunt.code
            self.__livreEmprunte=livreEmprunte
            self.__EmprunteurLivre=EmprunteurLivre
            self.__dateEmprunt=dateEmprunt
            self.__dateRetourPrevue=dateRPrevue
            self.__dateRetourEffective=dateREffective
#---------getter-----------        
    def getCode(self):
        return self.__code
    def getLivreEmprunte(self):
        return self.__livreEmprunte
    def getEmprunteurLivre(self):
        return self.__EmprunteurLivre
    def getDateEmprunt(self):
        return self.__dateEmprunt
    def getDateRetourPrevue(self):
        return self.__dateRetourPrevue
    def getDateRetourEffective(self):
        return self.__dateRetourEffective
#--------setter--------------    
    def setLivreEmprunte(self,value):
        if not isinstance(value,str):
            raise Exception("Le nom de livre est invalide!")
        else:
            self.__livreEmprunte=value
    def setEmprunteurLivre(self,value):
        if not isinstance(value,Adherent):
            raise Exception("L'emprunteur du livre est invalide!")
        else:
            self.__EmprunteurLivre=value
    def setDateEmprunt(self,value):
        if not isinstance(value,date) and value==date.today:
            raise Exception("La date d'emprunt est invalide!")
        else:
            self.__dateEmprunt=value
    def getDateRetourPrevue(self,value):
        if not isinstance(value,date) and value<date.today:
            raise Exception("La date de retour prévue est invalide!")
        else:
            self.__dateRetourPrevue=value
    def setDateRetourEffective(self,value):
        if not isinstance(value,date):
            raise Exception("La date de retour effective est invalide!")
        else:
            self.__dateRetourEffective=value
#---------methodes-------------
    def etatEmprunt(self):
        etat=""
        if self.__dateRetourEffective<self.__dateRetourPrevue:
           etat+="en cours"
        elif self.__dateRetourEffective==self.__dateRetourPrevue:
            etat+="rendu"
        else:
            etat+="non rendu"
        print(etat)     
#--------test--------------
# emp=Emprunt("ALLALI",Adherent("tri","im",8,1,2025),date(2025,1,8),date(2025,4,3),date(2025,4,5))
# emp.etatEmprunt()