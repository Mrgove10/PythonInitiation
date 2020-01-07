from math import log
from time import time
from sys import stdout
start = time()
# -----------
limite = 100000

# https://blog.invivoo.com/sieve-of-eratosthenes/
# yield
# modifier le fichier d'affichage direct 
def SieveOfEratosthenes(n):
    string = ""
    N = n + 1
    t = [True] * N
    # remove multiple of 2
    
    #for i in range(4, N, 2):
    #    t[i] = False
    [False for i in range(4, N, 2)]
    # treat the odd numbers
    for i in range(3, N, 2):
        if t[i]:
            # ‘i’ is a prime number
            for j in range(i * i, N, i+i):
                t[j] = False
    # extract the list of prime numbers
    # [i for i in range(2, N) if t[i]]
    return [i for i in range(2, N) if t[i]]


#SieveOfEratosthenes(round(limite * (l + log(l) - 1/2)))

string = ""
l = log(limite)
v = SieveOfEratosthenes(round(limite * (l + log(l) - 1/2)))
tpsalgo = time() - start
# for index, val in enumerate(v):
#     string += "Rang : " + str(index+1) + " Nombre : " + str(val) + "\n"
#     if index+1 >= limite:
#         break
# print(string)
print("algo : {} secondes".format(tpsalgo.__round__(3)))
# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))