from Emprunt import *
from Adherent import *
from datetime import *
class Biblio:
    def __init__(self):
        self.__livres=[]
        self.__adherents=[]
        self.__emprunts=[]
    def ajouterEmprunt(self, codeA, codeL):
        adherent = self.rechercherAdherent(codeA)
        livre = self.rechercherLivre(codeL)
        if livre and adherent and livre.livreDisponible():
            dateEmprunt = date.today()
            dateRetourPrevue = dateEmprunt + timedelta(days=3)
            emprunt = Emprunt(livre, adherent, dateEmprunt, dateRetourPrevue)
            self.__emprunts.append(emprunt)
            livre.set_nbr_exemplaire_disponible(livre.get_nbr_exemplaire_disponible()-1)
    def retourEmprunt(self,codeEmprunt):
        for elt in self.__emprunts:
            if elt.getCode()==codeEmprunt:
                elt.setDateRetourEffective(date.today())
                elt.set_nbr_exemplaire_disponible(elt.get_nbr_exemplaire_disponible()+1)                         
    def topEmprunts(self):
        max=self.__emprunts[0].getLivreEmprunte().nbEmprunt
        for elt in self.__emprunts[1:]:
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
        return emprunteurs
    def datePossibilitéEmprunt(self,codeL):
        livre = self.rechercherLivre(codeL)
        if not livre:
            raise Exception("Livre introuvable.")
        if livre.livreDisponible():
            print("Le livre est disponible.")
        for elt in self.__emprunts:
            if elt.getLivreEmprunte() == livre and elt.etatEmprunt() == "En cours":
                return elt.getDateRetourPrevue().strftime('%d/%m/%Y')
        print("Il n'est pas prevu qu'il soit disponible.")