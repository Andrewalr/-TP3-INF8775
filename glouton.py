import sys
import os
import time
from operator import attrgetter
from operator import itemgetter
from pprint import pprint


    
start = time.perf_counter()
################################################################################


class Site:
   
   atome=0
   nbVoisin=0
   listeVoisin=[0]
   id=0

   def __init__(self, atome, nbVoisin,listeVoisin,id):
        self.atome = atome
        self.nbVoisin = nbVoisin
        self.listeVoisin = listeVoisin
        self.id = id


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  
    sites = []
    arretes = []
    arretesLong = []
    typeatomes = []
    voisinMax = []
    mygraph = {}

    t = 0
    k = 0
    a = 0

    energie = 0

    # ouvrir le fichier a lire
    file = open('test1', 'r')
    Lines = file.readlines()
    count = 0

    #lire le fichier
    for line in Lines:
        count += 1
        # print("Line{}: {}".format(count, line.strip()))

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
    
    #creer liste darretes qui se repete
    for a in arretes:
        a1 = [a[0], a[1]]
        a2 = [a[1], a[0]]
        arretesLong.append(a1)
        arretesLong.append(a2)
        sorted(arretesLong, key=itemgetter(0))

    #creer le graph
    
    for currentLine in arretesLong:
        voisin = []
        if currentLine[0] in mygraph:
            voisin = mygraph.get(currentLine[0])
            voisin.append(currentLine[1])
            mygraph.update({currentLine[0]:voisin})
        else:
            voisin = [currentLine[1]]
            mygraph.update({currentLine[0]:voisin})

    #creer les sites

    i=0
    while i < t:
        currentSite = Site(0,0,0,i)
        i=i+1
        sites.append(currentSite)
    
    #compter le nombre de voisin pour chaque site

    i=0
    for arrete in arretes:
        sites[arretes[i][0]].nbVoisin = sites[arretes[i][0]].nbVoisin +1
        sites[arretes[i][1]].nbVoisin = sites[arretes[i][1]].nbVoisin +1
        i=i+1
    
    # trouver le site avec le plus de voisin 
    max_siteid= max(sites, key=lambda site: site.nbVoisin).id
    i =0
    k =0
    atome1=0
    atome2=0
    min = H[0][0]
    for row in H:
        for col in row:
            if(H[i][k]<min):
                min = H[i][k]
                atome1=k
                atome2=i
                k = k+1
        i=i+1        

    #trouver l atome du couple min qui est en plus grande quantite
    ########a tester : inverSER CA
    if(typeatomes[atome1]<typeatomes[atome2]):
        atomeDepart = atome2
    else:
        atomeDepart = atome1

    print(atomeDepart)
    


    def trouverMeilleurAtomeDisponible(atomePere):
        j=0
        for a in typeatomes:
            if a > 0:
                colMin = j
                min = H[atomePere][colMin]
                break
            j=j+1
        i=0
        for col in H[atomePere]:
            if H[atomePere][i] < min:
                if typeatomes[i] > 0 :
                    min = H[atomePere][i]
                    colMin = i
            i=i+1
        return colMin

    #assigner au site avec le plus de voisin l atome du couple min qui est en plus grande quantite
    sites[max_siteid].atome = atomeDepart
    pprint(vars(sites[max_siteid]))
    typeatomes[atomeDepart] = typeatomes[atomeDepart]-1

    def bfs(Graphe, Sommet):
        couleur = {s: "vert" for s in Graphe}
        print(couleur)
        Pere = {}
        Pere[Sommet] = None
        couleur[Sommet] = "orange"
        File =[Sommet]
        while File :
            u = File[0]
            for v in Graphe[u]:
                if couleur[v] == "vert":
                    Pere[v] = u
                    couleur[v] = "orange"      
                    File.append(v)
            File.pop(0)
            couleur[u] = "rouge"

            if u != Sommet:
                atomeT = trouverMeilleurAtomeDisponible(sites[Pere[u]].atome)
                sites[u].atome = atomeT
                typeatomes[atomeT] = typeatomes[atomeT] -1

        return Pere 

    def calculerEnergie(arretes):

        i=0
        energie=0
        for a in arretes:
            energie = energie + H[sites[arretes[i][0]].atome][sites[arretes[i][1]].atome]

        print(energie)      
        return energie

    bfs(mygraph, sites[max_siteid].id)        

    calculerEnergie(arretes)
    print(typeatomes)

    def afficherSolution(sites):
        i=0
        for site in sites:
            print(sites[i].atome)
            i=i+1
    
    afficherSolution(sites)
