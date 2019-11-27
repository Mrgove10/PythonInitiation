# -*- coding: utf-8 -*-
import random
rand = random.randint(1, 100)
print(str(rand))
userguess = 999
tries = 0
while int(userguess) != rand:
    userguess = input("Votre nombre : ")
    tries += 1
    if int(userguess) > rand:
        print("C'est plus bas !")
    if int(userguess) < rand:
        print("C'est plus haut !")
print("Victoire en " + str(tries) + " coups! Le chiffre etais " + userguess + " !")
