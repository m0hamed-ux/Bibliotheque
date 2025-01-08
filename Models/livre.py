import re
from Auteur import*
class livre:
    def __init__(self,code,titre,auteur,nbr_ttl_exemplaire,nbr_exemplaire_disponible):
        template=r"^L\d{4}$"
        if not re.match(template,code):
            raise Exception("Le code inserer doit commencer par la lettre 'L' majiscule suivie par quatre chiffre ")
        elif not isinstance(auteur,Auteur):
            raise Exception("INVALIDE !!")
        elif not isinstance(nbr_ttl_exemplaire,int) or not isinstance(nbr_exemplaire_disponible,int):
            raise Exception("le nombre saisie doit etre un entier")
        elif nbr_ttl_exemplaire < 0 and nbr_exemplaire_disponible> nbr_ttl_exemplaire:
            raise Exception(" ERROR réviser les iformations donner !!")
        else:
            self.__code=code
            self.__auteur=auteur
            self.__titre=titre
            self.__nbr_ttl_exemplaire=nbr_ttl_exemplaire
            self.__nbr_exemplaire_disponible=nbr_exemplaire_disponible

            

    #getters 

    def get_code(self):
        return self.__code
    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nbr_ttl_exemplaire(self):
        return  self.__nbr_ttl_exemplaire
    def get_nbr_exemplaire_disponible(self):
        return self.__nbr_exemplaire_disponible
    
    #setters

    def set_code(self,new_code):
        self.__code=new_code
    def set_titre(self,new_titre):
        self.__titre=new_titre
    def set_auteur(self,new_auteur):
        self.__auteur=new_auteur
    def set_nbr_ttl_exemplaire(self,new_value):
        self.__nbr_ttl_exemplaire=new_value
    def set_nbr_exemplaire_disponible(self,new_value2):
        self.__nbr_exemplaire_disponible=new_value2

    #methoode
    def LivreDisponible(self):
        return self.get_nbr_exemplaire_disponible > 0