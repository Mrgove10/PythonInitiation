# -*- coding: utf-8 -*-
import random

rand = random.randint(1, 10)
print(str(rand))
userguess = 999
tries = 0
usermin = 999
usermax = 0
while int(userguess) != rand and tries < 3:
    userguess = input("Votre nombre : ")
    if int(userguess) < usermin:
        usermin = int(userguess)
        print("new min " + str(usermin))
    if int(userguess) > usermax:
        usermax = int(userguess)
        print("new max " + str(usermax))
    tries += 1
    if tries <= 3:
        if rand == int(userguess):
            rand = random.randint(usermin, usermax)
            print("new rand " + str(rand))
# does not work
    if int(userguess) > rand:
        print("C'est plus bas !")
    if int(userguess) < rand:
        print("C'est plus haut !")
    if userguess == rand:
        print("Victoire en " + str(tries) +
              " coups! Le chiffre etais " + userguess + " !")
