class Decorations :

    def __init__(self, Couleur, Masse) :
        self._C = Couleur
        self._M = Masse

    def getMasse(self):
        return self._M

    def getCouleur(self):
        return self._C

    def setMasse(self, a):
        self._M = a

    def setCouleur(self, a):
        self._C=a

    def print(self):
        pass


class Boule(Decorations) :
    def __init__(self,Couleur,Masse,Diametre):
        Decorations.__init__(self,Couleur, Masse)
        self.__D = Diametre

    def getCouleurBoule(self):
        return self._C

    def getMasseBoule(self):
        return self._M

    def getDiametreBoule(self):
        return self.__D

    def setCouleurBoule(self,a):
        self._C =a

    def setMasseBoule(self,a):
        self._M = a

    def setDiametreBoule(self,a):
        self.__D = a

    def Affichage(self):
        print("* Boule ",self._C," de ",self.__D,"cm de diamètre, pesant ",self._M,"g.")




class Guirlande(Decorations) :

    def __init__(self,Couleur,Masse,Longueur):
        Decorations.__init__(self,Couleur, Masse)
        self._L=Longueur

    def getCouleurGuirlande(self):
        return self._C

    def getMasseGuirlande(self):
        return self._M

    def getLongueurGuirlande(self):
        return self._L

    def setCouleurGuirlande(self,a):
        self._C =a

    def setMasseGuirlande(self,a):
        self._M = a

    def setLongueur(self,a):
        self._L = a

    def Affichage(self):
        pass


class GuirlandeLumineuse(Guirlande) :

    def __init__(self,Couleur,Masse,Longueur,NbLumiere):
        Guirlande.__init__(self,Couleur, Masse,Longueur)
        self.__NbL = NbLumiere

    def getNbLumiere(self):
        return self.__NbL

    def setNbLumire(self,a):
        self.__NbL = a

    def Affichage(self):
        print("* Guirlande lumineuse ",self._C," de ",self._L,"cm de long, possédant",self.__NbL, "lumières et pesant ",self._M,"g.")

