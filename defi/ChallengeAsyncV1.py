# see https://www.arrobe.fr/defi/
import threading
from time import time
start = time()
# -----------

limit = 10
count = 1
num = 2

def is_prime(n, c):
    for i in range(2, n):
        if n % i == 0:
            break
        else :
            print("Rang : " + str(c) + " Nombre : " + str(n))

for count in range(limit):
    threading.Thread(target=is_prime, args=(num,count)).start()
    count += 1

# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))
