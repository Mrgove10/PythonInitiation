from math import log
from time import time
from sys import stdout
start = time()
# -----------
limite = 100000
f = open("workfile","w") 
# https://blog.invivoo.com/sieve-of-eratosthenes/

def SieveOfEratosthenes(n):
    string = ""
    N = n + 1   
    t = [True] * N
    # remove multiple of 2
    for i in range(4, N, 2):
        t[i] = False
    # treat the odd numbers
    for i in range(3, N, 2):
        if t[i]:
            # ‘i’ is a prime number
            for j in range(i * i, N, i+i):
                t[j] = False
    # extract the list of prime numbers
    idx = 0
    for i in range(1, N):
        if t[i]:
            string += "Rang : {} Nombre : {} \n".format(idx ,i)
            idx += 1
        if idx > limite:
            break
    #stdout.write(string)
    f.write(string)
    f.close()

l = log(limite)
SieveOfEratosthenes(round(limite * (l + log(l) - 1/2)))
with open("workfile", 'r') as fin:
    print(fin.read(), end="\n")
    
# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))