"""def bfs(graphe, start):
    visited = []  # Liste des sommets visités
    queue = []  # File pour stocker les sommets à visiter

    queue.append(start)
    visited.append(start)

    while queue:
        current = queue.pop(0)
        print(current)  # Modifier ici pour faire autre chose que l'impression
        neighbors = list(graphe.neighbors(current))
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)"""
                
                
from collections import deque

def iterative_bfs(graph, start):
 
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            queue.extend(unvisited)

    return visited