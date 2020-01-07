from math import log
from time import time
from sys import stdout
from os import system
from io import StringIO
start = time()
# -----------
#lim = 100000

#https://stackoverflow.com/questions/44672524/how-to-create-in-memory-file-object/44672691
def algo(n):
    s = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if s[i]:
            s[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if s[i]]

st = ""
l = log(100000)

for index, val in enumerate(algo(round(100000 * (l + log(l) - 1/2)))):
    st += "Rang : " + str(index+1) + " Nombre : " + str(val) + "\n"
    if index+1 >= 100000:
        break

f = StringIO(st)
print(f.getvalue())
# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))