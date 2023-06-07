G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
     
def trouver_arcs(graph):
    arcs = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0 :
                arcs.append((i , j , graph[i][j]))
    return arcs

class EnsembleDisjoint :
    
    parent = {} 
    def __init__(self, N):
        for i in range(N):
            self.parent[i] = i

    def get_parent(self, k):
        if self.parent[k] == k:
            return k

        return self.get_parent(self.parent[k])
    def Union(self, a, b):
        x = self.get_parent(a)
        y = self.get_parent(b)
        self.parent[x] = y
def Kruskal(arcs, nombre_sommets):


    arcs.sort(key=lambda x: x[2])
    Arbre_minimum = []
    ed = EnsembleDisjoint(nombre_sommets)
    index = 0

    while len(Arbre_minimum) != nombre_sommets - 1:


        (src, dest, weight) = arcs[index]
        index = index + 1

        x = ed.get_parent(src)
        y = ed.get_parent(dest)

        if x != y:

            Arbre_minimum.append((src, dest, weight))
            ed.Union(x, y)

    return Arbre_minimum


Arbre_minimum =  Kruskal(trouver_arcs(G), 5) 

print(Arbre_minimum)