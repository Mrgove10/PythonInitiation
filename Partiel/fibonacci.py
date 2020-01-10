###
# Version perso, fait avant la suivante
###
print("Version perso :")
def f(n):
    a, b = 0, 1  #a = 0 nous obligera a ramjouter un apres (see next comment)
    for i in range(0, n):
        a, b = b, a + b
        length = len(str(a))
        if(length == 1000):
            print(i+1) #+1 parceque on cherche le rang , c'est donc le 4782**eme** nombre de fibonacci
            break
    return a
f(5000)

###
# Version 2 trouver avec 3 recherches google, bien plus jolie mais moins gratifiant 
# https://www.lucaswillems.com/fr/articles/51/project-euler-25-solution-python
###
print("Version internet :")
a = 1
b = 1
resultat = 2
while len(str(b)) < 1000:
    a, b = b, a+b
    resultat += 1
print(resultat)