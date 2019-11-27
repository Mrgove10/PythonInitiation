# -*- coding: utf-8 -*-
for i in range(2000, 4001):
    if i % 7 == 0:
        if i % 5 != 0:
            print(str(i) + " => Oui (divisible par 7 et pas par 5)")
    else:
        print(str(i) + " => Non (pas divisible par 7)")
