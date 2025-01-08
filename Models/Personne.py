class Perssonne:
    def _init_(self,nom,prenom):
        if not isinstance(nom,str):
            raise Exception("le nom est invalid!")
        elif not isinstance(prenom,str):
            raise Exception("le prenom est invalid!")
        else:
            self.__nom=nom
            self.__prenom=prenom
        
    def get_nom(self,nom):
        self.nom=nom
        
    def set_nom(self,nom):
        if not isinstance(nom,str):
            raise Exception("le nom est invalid!")
        else:
            self.nom=nom
        
    def get_prenomm(self,nom):
        self.nom=nom
        
    def set_prenom(self,prenom):
        if not isinstance(prenom,str):
            raise Exception("le prenom est invalid!")
        else:
            self.prenom=prenom
    
    def _str_(self):
        return f"Nom : {self.nom} , Prenom : {self.prenom}"