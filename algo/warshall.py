#1) initailiser un tableau par les arc existants 
#2) defini une fonction qui determine les entrants a un sommet donne 
#3) defini une fonction qui determine les sortants a un sommet donne 
#4) la fonction warshall verifier que l'arc (entrant , sortant) existe dans le tableau des arcs 
#5) si l'arc n'existe pas il va l'ajouter 

graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]
#fonction pour un graph non oriente 
def warshall(G):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = G[i][j] or (G[i][k] and G[k][i])

# tester la connectivite :

# connection = True 

# def connectivite(G):
#     n = len(G)
#     for i in range(n):
#         for j in range(n):
#             if(G[i][j] == 0):
#                 connection = False 
#             else :
#                 connection = True 
#     return connection

# fonction de graph oriente 
def warshallO(G):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(G[i][j] != 1):
                    G[i][j] = 1                          
    return G 
graph = warshallO(graph)
print(graph)
