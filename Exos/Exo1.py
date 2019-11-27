# -*- coding: utf-8 -*-
age = 0
while int(age) < 1 or int(age) > 125:
    age = input("Quel age avez vous: ")
agemod = int(age) + 31
print("En 2050 vous aurez " + str(agemod) + " ans")
