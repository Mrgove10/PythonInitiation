# -*- coding: utf-8 -*-
age = 0
while int(age) < 1 or int(age) > 125:
    print("Quel age avez vous: ")
    age = input()
agemod = int(age) + 31
print("En 2050 vous aurez " + str(agemod) + " ans")