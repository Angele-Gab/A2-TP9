class Sapin :

    def __init__(self, MasseMax, MasseTotale, ListeDecorations=[]) :
        self.__MM = MasseMax
        self.__MT = MasseTotale
        self.__LD = ListeDecorations

    def getMasseMax(self):
        return self.__MM

    def getMasseTotale(self):
        return self.__MT

    def setMasseMax(self, a):
        self.__MM = a

    def setMasseTotale(self, a):
        self.__MT=a

    def Ajout(self,d):
        self.__LD.append(d)
        self.__MT += d.getMasse()

    def Suppression(self,d):
        self.__LD.remove(d)
        self.__MT -= d.getMasse()

    def Affichage(self):
        print("Ce sapin de Noël peut supporter ", self.__MM,"g de décorations.")
        if len(self.__LD) == 0 :
            print("Il ne contient actuellemnt aucune décoration.")
        else :
            print("Il contient actuellement ", self.__MT,"g de décorations, listées ci-après : ")
        for i in self.__LD :
            i.Affichage()

        print("-----------------------------------------------------")
