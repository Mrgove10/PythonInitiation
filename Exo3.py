# -*- coding: utf-8 -*-
userInput = input("Entrée votre palindrome : ")
reversedUserInput = ''.join(reversed(userInput))
if userInput == reversedUserInput:
    print(userInput + " => Oui")
else:
    print(userInput + " => Non")
