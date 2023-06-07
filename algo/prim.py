INF = 1000 
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

def prim(num_node , G):
    selected_node = [] 
    selected_node = [0]*num_node
    selected_node[0] = True 
    no_edge = 0 
    while(no_edge < num_node -1):
        minimum = INF 
        a=0
        b=0
        for m in range(num_node):
            if  selected_node[m]:
                for n in range(num_node):
                    if ( (not selected_node[n]) and G[m][n]):
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a=m
                            b=n
        print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
        selected_node[b] = True
        no_edge += 1
prim(5,G)
        
