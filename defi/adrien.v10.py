from math import log
from time import time
from sys import stdout
from os import system
start = time()
# -----------
limite = 100000

def algo(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

string = ""
l = log(limite)
v = algo(round(limite * (l + log(l) - 1/2)))
#tpsalgo = time() - start #time

for index, val in enumerate(v):
    string += "Rang : " + str(index+1) + " Nombre : " + str(val) + "\n"
    if index+1 >= limite:
        break

fp = open('a',"w")
fp.write(string)
fp.close()
#tpswrite = time() - start #time

system("cat a")
#tpscat = time() - start #time

#print("algo : {} secondes".format(tpsalgo.__round__(3)))
#print("write : {} secondes".format(tpswrite.__round__(3)))
#print("cat : {} secondes".format(tpswrite.__round__(3)))
# -----------
stop = time() - start
print("Temps d'execution : {} secondes".format(stop.__round__(3)))