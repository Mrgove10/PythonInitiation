#!/usr/bin/python3
# -*-coding:Utf-8 -*

from math import sqrt


class Pion():
    """ Cette classe simule le déplcement d'un pion sur une grille de 10 * 10
    """

    def __init__(self, x=5, y=5):
        """Les paramétres x et y sont facultatifs
        par défault, il vallent 5 et 5"""
        self.__x = x
        self.__y = y

    def haut(self):
        """ déplace le pion en haut 
        sans dépasser x = 10 """
        self.__x += 1
        if self.__x > 10:
            self.__x = 10

    def bas(self):
        """ déplace le pion en bas
        sans dépasser x = 1 """
        self.__x -= 1
        if self.__x < 1:
            self.__x = 1

    def droite(self):
        """ déplace le pion à droite
        sans dépasser y = 10 """
        self.__y += 1
        if self.__y > 10:
            self.__y = 10

    def gauche(self):
        """ déplace le pion à gauche
        sans dépasser y = 1 """
        self.__y -= 1
        if self.__y < 1:
            self.__y = 1

    def getDistance(self, autre_pion):
        """ Calcule la distance entre le pion et un autre passé en paramétre"""
        return sqrt((self.__x-autre_pion.getx())**2+(self.__y-autre_pion.gety)**2)

    def __repr__(self):
        """Affiche les coordonées d'un pion"""
        return "{}: x = {}, y = {}".format(self.__class__.__name__,self.__x, self.__y)

    def getx(self):
        return self.__x

    def setx(self, value):
        print("Nope !")

    def gety(self):
        return self.__y

    def sety(self, value):
        print("Nope !")

    def estProche(self, autre_pion):
        return (2>=self.getDistance(autre_pion))

class Dame(Pion):
    def __init__(self, xdame=5, ydame=5):
        Pion.__init__(self, xdame, ydame)

    def diago(self, direction):
        if(direction == "haut-droit"):
            Pion.haut(self)
            Pion.droite(self)
        elif(direction == "haut-gauche"):
            Pion.haut(self)
            Pion.droite(self)
        elif(direction == "bas-droit"):
            Pion.bas(self)
            Pion.droite(self)
        elif(direction == "bas-gauche"):
            Pion.bas(self)
            Pion.gauche(self)


# test de la classe
if __name__ == "__main__":
    unPion = Pion(3, 8)  # un pion en coordonées x=3, y=8
    unPion.haut()
    unPion.gauche()
    autrePion = Pion()
    autrePion.bas()
    autrePion.droite()

    print(unPion.__repr__())
    print(autrePion.__repr__())
    print("distance : {}".format(unPion.getDistance(autrePion)))
