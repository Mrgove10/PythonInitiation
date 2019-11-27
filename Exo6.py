# -*- coding: utf-8 -*-
userInput = input("Un nombre : ")
print("Liste des diviseurs de " + userInput + " : ")
for i in range(1, 100):
    if int(userInput) % i == 0:
        print(i)
        