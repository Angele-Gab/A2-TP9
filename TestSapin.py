from Tests import *
from Décorations import *

Sapin = Sapin(5000,0,[])
Sapin.Affichage()
Boule1 = Boule("Bleue",215,15)
Sapin.Ajout(Boule1)
Sapin.Ajout(GuirlandeLumineuse("Bleue",200,500,50))
Sapin.Affichage()
Sapin.Suppression(Boule1)
Sapin.Affichage()

