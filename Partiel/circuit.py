#!/usr/bin/python3
# -*-coding:Utf-8 -*
from vehicule import VoitureEssence, VoitureDiesel
circuit = [0, 0, 0, 50, 0, 0, 90, 0, 20, 120]


def controleChoix(texte, mini, maxi):
    """ Display "texte" and check than user input is a numeric value between "mini" and "maxi" """
    while True:
        choix = input(texte)
        try:
            choix = int(choix)
            assert choix in range(mini, maxi+1)
        except ValueError:
            print("Vous devez saisir un nombre !")
        except AssertionError:
            print("Vous devez saisir un nombre entre {} et {}".format(mini, maxi))
        else:
            return choix


def afficheCircuit(circuit, tour):
    """ Display the track in "circuit" and dispaly player's position"""
    i = 0
    for virage in circuit:
        i += 1
        if virage == 0:
            # print with 2nd parameter allow to print whithout cariage return
            print("Ligne Droite ", end='')
        else:
            print("Virage {}°   ".format(virage), end='')
        if tour == i:
            print("<===")
        else:
            print(".")


def testSortieDePiste(joueur, angle):
    """ Check if the player is still on the track"""
    if angle != 0:
        calc = (200 - angle)
        if joueur.getVitesse() > calc:
            return True
        else:
            return False


# Initialistation des variables
# Make user choose between 1 : Diesel 2 : Essence
carburation = controleChoix(
    "choose between  | 1 : Diesel | 2 : Essence : ", 1, 2)
# Made user choose between 500 et 3000 kg
poids = controleChoix("choose between 500 et 3000 kg : ", 500, 3000)
# Made user choose between 25 et 1000 Cv
acceleration = controleChoix("choose between 25 et 1000 Cv : ", 25, 1000)
nom = input("choose a name : ")    # Made user enter a name

if carburation == 1:
    joueur = VoitureDiesel(nom, poids, acceleration)
if carburation == 2:
    joueur = VoitureEssence(nom, poids, acceleration)

temps = 0   # Add speed on each turn to calculate total time
tour = 0    # Turn number
crash = False   # True if car crash

# Allocate player's car named Joueur up to choice carburation

for virage in circuit:
    """
    Write main loop here ...
    """
    print("======================= Tour N° {} ===".format(tour))

    print("1 : Accélérer")
    print("2 : Continuer")
    print("3 : Freiner")
    choix = input("Votre choix ? : ")
    if choix == 1:
        joueur.Accelerer()
    elif choix == 2:
        pass
    elif choix == 3:
        joueur.Freiner()

    print(joueur)

    afficheCircuit(circuit, virage)
    temps = temps + joueur.getVitesse()
    
    tour = tour + 1

# End of program
if crash:
    print("Et paf le mur ! (Votre vitesse : {} / vitesse max = {})".format(
        joueur.getVitesse(), 200 - circuit[tour]))
else:
    print("Bravo ! Votre temps : {0:.2f} s".format(3600/temps))
