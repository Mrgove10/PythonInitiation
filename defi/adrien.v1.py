# see https://www.arrobe.fr/defi/
from time import time
start = time()
# -----------

limit = 100000  # 22.327 secondes
count = 1
num = 2

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while count != limit+1:
    if is_prime(num):
        print("Rang : " + str(count) + " Nombre : " + str(num))
        count += 1
    num += 1

# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))
