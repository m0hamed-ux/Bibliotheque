from Models import livre
from Models import Adherent
from Models import Emprunt
from datetime import date
class Biblio:
    def __init__(self):
        self.__livres=[]
        self.__adherents=[]
        self.__emprunts=[]
    def ajouterLivre(self):
        print("Saisir les information de livre :")
        code = input("Code (Ex : L000): ")
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        nbr_ttl_exemplaire = int(input("Le nombre total des exemplaires : "))
        nbr_exemplaire_disponible = int(input("Le nombre des exemplaires disponibles : "))
        if nbr_ttl_exemplaire < nbr_exemplaire_disponible:
            raise Exception("le Le nombre total des exemplaires doit etre superieur de le nombre des exemplaires disponibles")
        lvr = livre.livre(code, titre, auteur, nbr_ttl_exemplaire, nbr_exemplaire_disponible)
        self.__livres.append(lvr)
    def ajouterAdherent(self):
        print("Saisir les information de l'adherent :")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        print("La date d’adhésion : ")
        day = int(input("\tJour : "))
        month = int(input("\tMois : "))
        year = int(input("\tAnnee : "))
        try:
            dateAdhesion = date(year, month, day)
        except Exception as e:
            print(e)
        else:
            Adh = Adherent.Adherent(nom, prenom, dateAdhesion)
            self.__adherents.append(Adh)
    def rechercherAdherent(self,code):
        for adherent in  self.__adherents :
            if adherent.get_code() == code : 
                return adherent
        return None
        
    def rechercherLivre(self,code):
        for livre in self.__livres:
            if livre.get_code() == code : 
                return livre 
        return None
    def ajouterEmprunt(self,codeA,codeL):
        pass
    def retourEmprunt(self,codeEmprunt):
        pass   
    def topEmprunts(self):
        pass
    def emprunteurs(self):
        pass
    def datePossibilitéEmprunt(self,codeL):
        pass