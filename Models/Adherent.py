from Personne import *
from datetime import *
from re import *
class Adherent(Personne) :
    code=0
    def __init__(self,nom,prenom,DayAdhésion,monthAdhésion,yearAdhésion):
        Adherent.code +=1
        Personne.__init__(self,nom,prenom)
        if not date(yearAdhésion, monthAdhésion, DayAdhésion)== date.today():
            raise Exception ("date inscription invalide")
        else:
            self.__DateAdhésion = date(yearAdhésion, monthAdhésion, DayAdhésion)
            self.__code = Adherent.code
        
    def getCode(self):
        return self.__code
    def getDateDateAdhésion(self):
        return self.__DateAdhésion
    def __str__(self):
        return super().__str__()+f" / Le code est : {self.getCode()} et la date d'Adhésion : {self.DateAdhésion.day} . {self.DateAdhésion.month} . {self._DateAdhésion.year}"