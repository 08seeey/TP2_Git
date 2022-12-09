#Affiche un message
print("TP2 GIT avec M.ETTAYEB")

#Calcule la factorielle d'un nombre
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)
