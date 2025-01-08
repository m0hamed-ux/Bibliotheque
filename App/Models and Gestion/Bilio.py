from livre import *
from Adherent import *
from Auteur import *
from Emprunt import *
from datetime import date
class Biblio:
    def __init__(self):
        self.__livres=[]
        self.__adherents=[]
        self.__emprunts=[]
    def ajouterLivre(self):
        print("---Saisir les information de livre :---")
        code = input("Code (Ex : L1234) : ")
        for Livre in self.__livres:
            if Livre.get_code() == code:
                raise Exception("Il existe déjà un livre avec ce code !")
        titre = input("Titre : ")
        print("Les Informations d'auteur : ")
        auteur = Auteur(input("├── Nom : "), input("├── Prenom : "), input("├── Code (Ex : A1234) : "))
        nbr_ttl_exemplaire = int(input("Le nombre total des exemplaires : "))
        nbr_exemplaire_disponible = int(input("Le nombre des exemplaires disponibles : "))
        if nbr_ttl_exemplaire < nbr_exemplaire_disponible:
            raise Exception("le Le nombre total des exemplaires doit etre superieur de le nombre des exemplaires disponibles")
        lvr = livre(code, titre, auteur, nbr_ttl_exemplaire, nbr_exemplaire_disponible)
        self.__livres.append(lvr)
    def ajouterAdherent(self):
        print("---Saisir les information de l'adherent :---")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        print("La date d’adhésion : ")
        day = int(input("├── Jour : "))
        month = int(input("├── Mois : "))
        year = int(input("├── Annee : "))
        try:
            dateAdhesion = date(year, month, day)
        except Exception as e:
            print(e)
        else:
            Adh = Adherent(nom, prenom, dateAdhesion)
            self.__adherents.append(Adh)
    def rechercherAdherent(self,code):
        for adherent in  self.__adherents :
            if adherent.getCode() == code : 
                return adherent
        return None
        
    def rechercherLivre(self,code):
        for livre in self.__livres:
            if livre.get_code() == code : 
                return livre 
        return None
    def ajouterEmprunt(self, codeA, codeL):
        adherent = self.rechercherAdherent(codeA)
        livre = self.rechercherLivre(codeL)
        if livre and adherent and livre.livreDisponible():
            dateEmprunt = date.today()
            dateRetourPrevue = dateEmprunt + timedelta(days=3)
            emprunt = Emprunt(livre, adherent, dateEmprunt, dateRetourPrevue, dateREffective=None)
            self.__emprunts.append(emprunt)
            livre.set_nbr_exemplaire_disponible(livre.get_nbr_exemplaire_disponible()-1)
            livre.addNbrEmprunt()

    def retourEmprunt(self,codeEmprunt):
        for elt in self.__emprunts:
            if elt.getCode()==codeEmprunt:
                elt.setDateRetourEffective(date.today)
                elt.set_nbr_exemplaire_disponible(elt.set_nbr_exemplaire_disponible()+1)                         
    def topEmprunts(self):
        max=self.__emprunts[0].getLivreEmprunte().nbEmprunt
        for elt in self.__emprunts[1:len(self.__emprunts)]:
            if elt.getLivreEmprunte().nbEmprunt>max:
                max=elt.getLivreEmprunte().nbEmprunt
                livreM=elt.getLivreEmprunte()
        return livreM
    def emprunteurs(self):
        emprunteurs=[]
        for elt in self.__emprunts:
            if elt.etatEmprunt() in ["en cours","non rendu"]:
                if elt.getEmprunteurLivre() not in emprunteurs:
                    emprunteurs.append(elt.getEmprunteurLivre())
        if len(emprunteurs) == 0:
            raise Exception("la liste est vide")
        return emprunteurs
    def datePossibilitéEmprunt(self, codeL):
        pass 

    
    def AfficherLivres(self):
        if len(self.__livres) == 0:
            raise Exception("la liste est vide")
        print("La list des livres : ")
        for livre in self.__livres:
            print(f"{livre}")
    def AfficherAdherents(self):
        if len(self.__adherents) == 0:
            raise Exception("la liste est vide")
        print("La list des adherents : ")
        for Adherent in self.__adherents:
            print(f"├── {Adherent}")
    def Rapport(self):
        print(f"Nombres des livres : {len(self.__livres)}\nNombres des adherents : {len(self.__adherents)}")