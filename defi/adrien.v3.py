import math
import sys
from time import time
start = time()
# -----------
limite = 100000

def sieveOfAtkin(limit):
    stringfinale =''
    i =0
    P = [2, 3]
    for index, val in enumerate(P):
        stringfinale += "Rang : " + str(index+1) + " Nombre : " + str(val) + "\n"
        i += 1
    sieve = [False]*(limit+1)
    for x in range(1, int(math.sqrt(limit))+1):
        for y in range(1, int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit+1, x**2):
                sieve[y] = False
    for p in range(0, limit):
        if sieve[p]:
            P.append(p)
            stringfinale += "Rang : " + str(i+1) + " Nombre : " + str(p) + "\n"
            if i+1 >= limite:
                break
            i += 1
    print(stringfinale)
  #  return P

sieveOfAtkin(round(limite * (math.log(limite) + math.log(math.log(limite)) - 1/2)))

# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))
