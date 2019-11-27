# -*- coding: utf-8 -*-
userInput = input("Entrée votre phrase a inversé : ")
userInputSplit = userInput.split(' ')
reversedInput = ' '.join(reversed(userInputSplit))
print(reversedInput)
