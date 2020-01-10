#!/usr/bin/python3
# -*-coding:Utf-8 -*
import math


class Vehicule():
    """ This class allow to create a vehicule
    Attributes :
        nom : String (Default 'No Name')
        poids  : Integer (Default 1000)
        vitesse : Integer (Default 0)
        acceleration : Integer (Default 25)
    Méthods :
        Accelerer : Increase vitesse by round(Acceleration - poids / 100)
        Freiner : set vitesse to 0 if < 35. Else divide vitesse by 2 (rouded down)
    """

    def __init__(self, nom="No Name", poids=1000, acceleration=25):
        """ Init values of a new vehicle """
        self.__nom__ = nom
        self.__poids__ = poids
        self.__acceleration__ = acceleration
        self.__vitesse__ = 0

    def __repr__(self):
        """ Display infos """
        return "{} / {} Km/h ({} / {} Kg / +{})".format(self.__nom__, self.__vitesse__, self.__class__.__name__, self.__poids__, self.__acceleration__)

    def getNom(self):
        return self.__nom__

    def getPoids(self):
        return self.__poids__

    def getAcceleration(self):
        return self.__acceleration__

    def getVitesse(self):
        return self.__vitesse__

    def Accelerer(self):
        calc = math.ceil(self.__acceleration__ - self.__poids__ / 100)
        self.__vitesse__ = self.__vitesse__ + calc

    def Freiner(self):
        if(self.__vitesse__ < 25):
            self.__vitesse__ = 0
        else:
            self.__vitesse__ = round(self.__vitesse__ / 2)


class VoitureEssence(Vehicule):
    def __init__(self, nom, poids, acceleration):
        self.__carburation__ = "Essence"
        Vehicule.__init__(self, nom, poids, acceleration)


class VoitureDiesel(Vehicule):
    def __init__(self, nom, poids, acceleration):
        self.__carburation__ = "Diesel"
        Vehicule.__init__(self, nom, poids, acceleration)

    def Accelerer(self):
        print(self.__vitesse__)
        calc = math.ceil((0.8 * self.__acceleration__) - (self.__poids__ / 100))
        self.__vitesse__ = self.__vitesse__ + calc
