from Models import Emprunt
from Models import Adherent
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
            date_emprunt = date.today()
            date_retour_prevue = date_emprunt + timedelta(days=3)
            emprunt = Emprunt(livre, adherent, date_emprunt, date_retour_prevue)
            self.emprunts.append(emprunt)
            livre.set_nbr_exemplaire_disponible(livre.set_nbr_exemplaire_disponible-1)
            return emprunt
        return None
    def retourEmprunt(self,codeEmprunt):
        for elt in self.__emprunts:
            if elt.getCode()==codeEmprunt:
                elt.setDateRetourEffective(date.today)
                elt.set_nbr_exemplaire_disponible(elt.set_nbr_exemplaire_disponible+1)         

        
