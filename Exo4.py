# -*- coding: utf-8 -*-
import random
rand = random.randint(1, 100)
userguess = 999
while int(userguess) != rand:
    userguess = input("Votre nombre : ")
    if int(userguess) > rand:
        print("C'est plus bas !")
    if int(userguess) < rand:
        print("C'est plus haut !")
print("Victoire ! le chiffre etais " + userguess + " !")
