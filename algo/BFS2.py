graph = {
    '5' : ['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2' : [],
    '4' : ['8'],
    '8' :[]
}

visisted = []
queue = [] 

def bfs(node , graph):
    visisted.append(node)
    queue.append(node)
    
    while queue :
        m=queue.pop(0)
        print(m,"le sommet a bien defiler")
        for neighbour in graph[m]:
            if neighbour not in visisted :
                visisted.append(neighbour)
                queue.append(neighbour)



print("le bfs du graphe est : \n")
bfs('5',graph)
print(visisted)

