import subprocess 
import time 
import threading

def ping(i):
    reponse = subprocess.run('ping -c 1 ' + base + str(i), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
    if reponse.returncode == 0: 
        print(base + str(i) + ' est présent')

debut = time.time()
base = '192.168.0.' 
for i in range(255):   
    threading.Thread(target=ping, args=(i,)).start()
temps = time.time() - debut
print('Temps d\'exécution: ' + str(round(temps, 3)) + ' s')