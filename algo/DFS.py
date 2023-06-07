graph = {
    'A':['B'],
    'B':['D'],
    'C':['A','B'],
    'D':['C']
}

visited = []

def DFS(node , G) :
    visited.append(node)
    for neighbor in G[node]:
        if neighbor not in visited :
            DFS(neighbor,G)
      
DFS('A',graph)
print(visited)
