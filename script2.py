import csv
from operator import itemgetter


data = []
MoyDict = {}

#Fais appel au fichier csv

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

#Calcul de la moyenne et "enregistre" la note la plus haute et la plus basse

for row in data:
    haute = 0
    basse = 0
    total = 0
    moyenne = 0
    for column in row:
        if column.isdigit():
            column = int(column)
            if column > haute:
                haute = column
            if column < basse or basse == 0:
                basse = column
            total += column
    moyenne = total / 3
    MoyDict[row[0]] = [haute, basse, round(moyenne)]

#Ajout des notes dans la liste

Liste = []

for key, value in MoyDict.items():
    Liste.append([key, value[0],value[1],value[2]])


Liste.sort(key=itemgetter(1), reverse=True)

#Affiche les notes haute, basse et la moyenne

print('La moyenne des notes des étudiants classé du plus grand au plus petit \n')
print(Liste)

