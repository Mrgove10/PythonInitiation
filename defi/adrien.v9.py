from math import log
from time import time
from sys import stdout
start = time()
# -----------
limite = 100000

# https://blog.invivoo.com/sieve-of-eratosthenes/
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
# yield
# modifier le fichier d'affichage direct 
def SieveOfEratosthenes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

string = ""
l = log(limite)
v = SieveOfEratosthenes(round(limite * (l + log(l) - 1/2)))
tpsalgo = time() - start
for index, val in enumerate(v):
    string += "Rang : " + str(index+1) + " Nombre : " + str(val) + "\n"
    if index+1 >= limite:
        break
stdout.write(string)
#print("algo : {} secondes".format(tpsalgo.__round__(3)))
# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))