import math
from time import time
start = time()
# -----------
limite = 100000

def SieveOfEratosthenes(n):
    N = n + 1
    t = [True] * N
    for i in range(2, N):
        if t[i]:  # ‘i’ is a prime number
            for j in range(i+i, N, i):  # now we remove all ‘i’ multiples
                t[j] = False
    # extract the list of prime numbers
    return [i for i in range(2, N) if t[i]]

v = SieveOfEratosthenes(
    round(limite * (math.log(limite) + math.log(math.log(limite)) - 1/2)))
# timeAlgoPure = time() - start  # time

string = ""
for index, val in enumerate(v):
    string += "Rang : " + str(index+1) + " Nombre : " + str(val) + "\n"
    if index+1 >= limite:
        break
print(string)

# timeAffichage = time() - start  # time
#print("Algo Uniquement : {} secondes".format(timeAlgoPure.__round__(3)))
#print("Affichage : {} secondes".format(timeAffichage.__round__(3)))

# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))
