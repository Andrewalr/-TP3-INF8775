import sys
import os
import time
from operator import attrgetter

    
start = time.perf_counter()
################################################################################


class site:
    type = 0

    def __init__(self, type):
        self._type = type

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  
    sites = []
    arretes = []
    typeatomes = []
    voisinMax = []

    t = 0
    k = 0
    a = 0

    energie = 0

    # ouvrir le fichier a lire
    file = open('N10_K3_0', 'r')
    Lines = file.readlines()
    count = 0

    #lire le fichier
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

    # premiere ligne correspond aux paramaetres t k et A
    currentLine = Lines[0].split()

    t = int(currentLine[0])
    k = int(currentLine[1])
    a = int(currentLine[2])

    # deuxieme ligne correspond au nombre d’atomes de chaque type,
    currentLine = Lines[2].split()
    
    i=0
    for atome in currentLine:
        typeatomes.append(int(currentLine[i]))
        i = i+1
    

    # A partir de la troisieme ligne on commence a lire la matrice
    H = [[0 for i in range(k)] for j in range(k)]
    
    i = 0
    while i < k:
        currentLine = Lines[4+i].split()
        currentLine = [int(i) for i in currentLine]
        H[i] = currentLine
        i = i+1

    # A partir de la quatrieme ligne on lit les arretes 
    i=0
    while i < a:
        currentLine = Lines[5+k+i].split()
        currentLine = [int(i) for i in currentLine]
        arretes.append(currentLine)
        i=i+1

    file.close()

    # Trouver le site avec le  plus de voisin
    i=0
    for arrete in arretes:
        
       

