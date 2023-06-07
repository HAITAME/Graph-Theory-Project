import tkinter as tk
from tkinter import messagebox
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from BFS import iterative_bfs
from breadth_first_search import bfs_edges
from tkinter import simpledialog
 
def display():
    src = simpledialog.askstring("Sommet Depart", "Entrer un Sommet : ")
    if src:
        print(src)
        return src

# dijkstra
def dijkstra(G, window):
    source_node = display()

    # Dijkstra algorithm
    shortest_paths = nx.single_source_dijkstra_path(G, source=source_node)

    # Clear any previous graph
    plt.clf()

    # Draw G
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    # nx.draw_networkx_edges(G, pos, width=2, edge_color='red')

    # Update the canvas to display new G
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)


    # text widget 
    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    # details
    for node in shortest_paths:
        path = shortest_paths[node]
        path_length = nx.single_source_dijkstra_path_length(G, source=source_node)[node]
        details_text.insert(tk.END, f"Noeud {node}: chemin: {path}, Coût: {path_length}\n")

    details_text.config(state=tk.DISABLED)


# kruskal 
def kruskal(G, window):
    mst_edges = nx.minimum_spanning_edges(G, algorithm='kruskal', data=False)
    mst_edges_list = list(mst_edges)

    # Create a new graph 
    mst_graph = nx.Graph()

    mst_graph.add_nodes_from(G.nodes())
    tot=0

    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        tot = tot + weight

        mst_graph.add_edge(node1, node2, weight=weight)

    # Clear
    plt.clf()

    # Draw the minimum spanning tree graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='gray')
    nx.draw_networkx_edges(mst_graph, pos, width=2, edge_color='red')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)

    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        details_text.insert(tk.END, f"Arcs : ({node1}, {node2}), Coût: {weight}\n")
    details_text.insert(tk.END, f"Coût Totale: {tot}\n")

    details_text.config(state=tk.DISABLED)

# prim
def prim(G, window):
    mst_edges = nx.minimum_spanning_edges(G, algorithm='prim', data=False)
    mst_edges_list = list(mst_edges)

    # Create a new graph 
    mst_graph = nx.Graph()

    mst_graph.add_nodes_from(G.nodes())
    tot=0

    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        tot = tot + weight
        mst_graph.add_edge(node1, node2, weight=weight)

    # Clear 
    plt.clf()

    # Draw the minimum spanning tree graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='gray')
    nx.draw_networkx_edges(mst_graph, pos, width=2, edge_color='red')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

    # Update the canvas 
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)


    # Text widget
    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    #Details
    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        details_text.insert(tk.END, f"Arc: ({node1}, {node2}), Coût: {weight}\n")
    details_text.insert(tk.END, f"Coût Totale: {tot}\n")

    details_text.config(state=tk.DISABLED)

# DFS :: PILE :: LIFO 
# DFS :: LIFO
def dfsT(G, window):
    
    start_node = (display()) 

    visited = set()
    dfs_traversal = []

    def dfs(node):
        visited.add(node)
        dfs_traversal.append(node)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor)

    ######### start #########
    dfs(start_node)

    # Clear any previous graph
    plt.clf()

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='black')

    # Update the canvas to display the new graph
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)
    
    # Create a text widget to display the details
    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    # txt
    for node in dfs_traversal:
        details_text.insert(tk.END, f"{node}\n")

    details_text.config(state=tk.DISABLED)

# BFS :: FIFO :: FILE
def bfsT(G, window):
    #Breadth-First Search (BFS)
    visited = set()
    bfs_traversal = []

    # Get the starting node 
    start_node = (display()) 

    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop()
        bfs_traversal.append(node)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Clear
    plt.clf()

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='black')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)

    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    for node in bfs_traversal:
        details_text.insert(tk.END, f"{node}\n")

    details_text.config(state=tk.DISABLED)

# Warshall
def warshall(G, window):
    dist_matrix = nx.floyd_warshall_numpy(G)

    # Clear any previous graph
    plt.clf()

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)

    #text widget
    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    # Add the distances between each pair of nodes to the text widget
    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix[i])):
            details_text.insert(tk.END, f" Du noeud {i+1} à {j+1} :  {dist_matrix[i][j]}\n")

    details_text.config(state=tk.DISABLED)

# Breadth-First Search
#BFS :: FIFO
def bfsM(G, window):
    visited = set()
    bfs_traversal = []

    start_node = int(display()) 

    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop()
        bfs_traversal.append(node)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    plt.clf()

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='black')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)

    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    for node in bfs_traversal:
        details_text.insert(tk.END, f"{node}\n")

    details_text.config(state=tk.DISABLED)



# DFS :: PILE :: LIFO 
def dfsM(G, window):
    visited = set()
    dfs_traversal = []

    def dfs(node):
        visited.add(node)
        dfs_traversal.append(node)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor)

    start_node = int(display())  

    dfs(start_node)

    plt.clf()

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, width=2, edge_color='black')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, pady=10)

    details_text = tk.Text(window, height=30, width=40)
    details_text.grid(row=10, column=1, padx=10, pady=10)

    for node in dfs_traversal:
        details_text.insert(tk.END, f"{node}\n")

    details_text.config(state=tk.DISABLED)


def afficher_caracteristiques_graphe(G ):
                    # Création de la fenêtre
                    #  fenetre_caracteristiques = tk.Toplevel(window)
                    fenetre = tk.Toplevel()
                    fenetre.title("Caractéristiques du graphe")
                    # Nombre de sommets
                    nb_sommets = G.number_of_nodes()
                    label_sommets = tk.Label(fenetre, text="Nombre de sommets : {}".format(nb_sommets))
                    label_sommets.pack()
                    # # Nombre d'arêtes
                    nb_aretes = G.number_of_edges()
                    label_aretes = tk.Label(fenetre, text="Nombre d'arêtes : {}".format(nb_aretes))
                    label_aretes.pack()

                    
                    if check_state_o.get()==0:
                                                # # Liste des sommets
                        sommets = G.nodes()
                        label_sommets_liste = tk.Label(fenetre, text="Liste des sommets : {}".format(sommets))
                        label_sommets_liste.pack()
                        # # Liste des arêtes
                        aretes = G.edges()
                        label_aretes_liste = tk.Label(fenetre, text="Liste des arêtes : {}".format(aretes))
                        label_aretes_liste.pack()

                        #diametre du graphe
                        diametre = nx.diameter(G)
                        label_diametre = tk.Label(fenetre, text="Diametre : {}".format(diametre))
                        label_diametre.pack()
                        #densite
                        densite = nx.density(G)
                        label_densite = tk.Label(fenetre, text="Densite : {}".format(densite))
                        label_densite.pack()
                        #degre
                        degre = nx.degree(G)
                        label_degre = tk.Label(fenetre, text="Degre : {}".format(degre))
                        label_degre.pack()

                    # generate_dict(G)
                        matrix_dict = nx.to_dict_of_lists(G)
                        label_dict = tk.Label(fenetre, text="Dictionnaire : {}".format(matrix_dict))
                        label_dict.pack()                    


                        # Connexité
                        connexite = "Le graphe est connexe." if nx.is_connected(G) else "Le graphe n'est pas connexe."
                        label_connexite = tk.Label(fenetre, text=connexite)
                        label_connexite.pack()
                    #     # Orientation
                    #     orientation = "Le graphe est orienté." if nx.is_directed(G) else "Le graphe n'est pas orienté."
                    #     label_orientation = tk.Label(fenetre, text=orientation)
                    #     label_orientation.pack()
                    #     # Pondération
                    #     ponderation = "Le graphe est pondéré." if nx.is_weighted(G) else "Le graphe n'est pas pondéré."
                    #     label_ponderation = tk.Label(fenetre, text=ponderation)
                    #     label_ponderation.pack()
                    #     #pondere negetivement
                    #     # ponderation_N = "Le graphe est pondéré négativement.." if nx.is_negatively_weighted(G) else "Le graphe n'est pas pondéré négativement.."
                    #     # label_ponderation = tk.Label(fenetre, text=ponderation_N)
                    #     # label_ponderation.pack()
                    #     # Bipartition
                    #     bipartition = "Le graphe est biparti." if nx.is_bipartite(G) else "Le graphe n'est pas biparti."
                    #     label_bipartition = tk.Label(fenetre, text=bipartition)
                    #     label_bipartition.pack() 
                    
                    # def get_algorithmsM(): 
                        # window_algoM = tk.Tk()
                        # window_algoM.geometry
                        
                        # frame = tk.Frame(window_algoM)
                        # frame.pack(pady=10)
                        
                        # if check_state_p.get()==0:
                        #      BFS = tk.Button(frame, text="BFS", width=10, command=lambda: bfsM(G, window_algoM))
                        #      BFS.grid(row=1, column=0)
                             
                        #      DFS = tk.Button(frame, text="DFS", width=10, command=lambda: dfsM(G, window_algoM))
                        #      DFS.grid(row=1, column=1)

                       
                        # if check_state_p.get()!=0:
                        #      BFS = tk.Button(frame, text="BFS", width=10, command=lambda: bfsT(G, window_algoM))
                        #      BFS.grid(row=1, column=0)
                             
                        #      DFS = tk.Button(frame, text="DFS", width=10, command=lambda: dfsT(G, window_algoM))
                        #      DFS.grid(row=1, column=1)

                        #      Dijikstra = tk.Button(frame, text="Dijikstra", width=10, command=lambda: dijkstra(G, window_algoM))
                        #      Dijikstra.grid(row=1, column=3)

                        #      Warshall = tk.Button(frame, text="Warshall", width=10, command=lambda: warshall(G, window_algoM))
                        #      Warshall.grid(row=1, column=4)
                             
                        #      if check_state_o.get()==0 :
                        #         Prims = tk.Button(frame, text="Prims", width=10, command=lambda: prim(G, window_algoM))
                        #         Prims.grid(row=1, column=5)

                        #         Kruskal = tk.Button(frame, text="Kruskal", width=10, command=lambda: kruskal(G, window_algoM))
                        #         Kruskal.grid(row=1, column=2)

                        # window_algoM.mainloop()


                    def get_algorithmsM(): 
                        window_algoM = tk.Tk()
                        window_algoM.geometry()  

                        # Create a frame to contain the buttons
                        frame = tk.Frame(window_algoM)
                        frame.grid(row=0, column=0, padx=10, pady=10)

                        if check_state_p.get() == 0:
                            BFS = tk.Button(frame, text="BFS", width=10, command=lambda: bfsM(G, window_algoM))
                            BFS.grid(row=0, column=0, padx=10)

                            DFS = tk.Button(frame, text="DFS", width=10, command=lambda: dfsM(G, window_algoM))
                            DFS.grid(row=0, column=1, padx=10)
                        else:
                            BFS = tk.Button(frame, text="BFS", width=10, command=lambda: bfsT(G, window_algoM))
                            BFS.grid(row=0, column=0, padx=10)

                            DFS = tk.Button(frame, text="DFS", width=10, command=lambda: dfsT(G, window_algoM))
                            DFS.grid(row=0, column=1, padx=10)

                            Dijkstra = tk.Button(frame, text="Dijkstra", width=10, command=lambda: dijkstra(G, window_algoM))
                            Dijkstra.grid(row=0, column=2, padx=10)

                            Warshall = tk.Button(frame, text="Warshall", width=10, command=lambda: warshall(G, window_algoM))
                            Warshall.grid(row=0, column=3, padx=10)

                            if check_state_o.get() == 0:
                                Prims = tk.Button(frame, text="Prims", width=10, command=lambda: prim(G, window_algoM))
                                Prims.grid(row=0, column=4, padx=10)

                                Kruskal = tk.Button(frame, text="Kruskal", width=10, command=lambda: kruskal(G, window_algoM))
                                Kruskal.grid(row=0, column=5, padx=10)

                        window_algoM.mainloop()

         # Display the algorithms of the graph
                    button_algo1 = tk.Button(fenetre, text="les algorithmes", command=get_algorithmsM)
                    button_algo1.pack()
                    
                    #Planaire 
                    #planaire ="Le graphe est planaire." if nx.is_planar(G) else  "Le graphe n'est pas biparti."
                    

                    fenetre.mainloop()

def choix ():
    ############## Creation de G ################
    if check_state_o.get()==0:
        G = nx.Graph()
    else:
        G = nx.DiGraph()
        
    #######################  Verification des choix ##################
    if check_state_p.get()==0:
        # Label_choix=tk.Label(root, text="Voulez vous cree le phrahe avec une matrice ou avec un dictionnaire" ,font=(10), bg='#CCE5FF')
        # Label_choix.grid(row=6, column=0) 
        
        def matrice():

            def gener_matrice(): 
                try: 
                    L = int(Nbr_Sommet.get())
                    C= L
                except ValueError:
                    #ErrorL.config(text="Merci d'entrez un nombre entier non null")
                    messagebox.showinfo(title="Message" , message="Merci d'entrez un nombre entier non null")
                    return
                cadre_matrice = tk.Frame(cadre_M, width=200, height=200, bd=1, relief=tk.SOLID, bg='#CCE5FF' )
                cadre_matrice.grid(row=2, column=0, padx=10, pady=10)

                matrice =[]
                for i in range(L):
                     L_Label=tk.Label(cadre_matrice, text=i , font=('Arial',10), bg='#CCE5FF')
                     L_Label.grid(row=i+3, column=0)
                     for j in range(C):
                         C_Label=tk.Label(cadre_matrice, text=j , font=('Arial',10), bg='#CCE5FF')
                         C_Label.grid(row=2, column=j+1)

                for i in range(L):
                    l=[]
                    for j in range(C):
                        entryM = tk.Entry(cadre_matrice, width=5)
                        entryM.grid(row=i+3, column=j+1, padx=5, pady=5)

                        l.append(entryM) 

                    matrice.append(l)

                M_Button = tk.Button(cadre_M,text ="Géner le graphe")
                M_Button.grid(row=3+L, column=1, pady=10)


                def Cree_graph ():
                    #Creation des sommets
                    for i in range(L):
                        G.add_node(i)
                    #Creation des acres    
                    for i in range(L):
                        for j in range(C):
                            if matrice[i][j].get() == "1":
                                G.add_edge(i, j)
                    plt.clf()
                    def affichage_graphe():
                        if G.number_of_nodes() > 0:
                            # Créez une fenêtre pour afficher le graphe
                            fenetre_GM = tk.Toplevel(root)
                            fenetre_GM.title("Affichage du graphe")      
                            fenetre_GM.geometry("500x500")

                            # Créez un cadre pour contenir la visualisation du graphe
                            cadre_figure = tk.Frame(fenetre_GM)
                            cadre_figure.pack()

                            # Créez une figure et un canevas pour afficher le graphe
                            fig = plt.figure(figsize=(6, 6))
                            canvas = FigureCanvasTkAgg(fig, master=cadre_figure)
                            canvas.draw()
                            canvas.get_tk_widget().pack()

                            # Dessinez le graphe sur la figure
                            pos = nx.spring_layout(G)  # Déterminez une disposition des nœuds appropriée
                            nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold')

                            afficher_caracteristiques_graphe(G)
                            list = iterative_bfs(G,0)
                            print(list)

                            fenetre_GM.mainloop()
                        else:
                            messagebox.showinfo(title="Message" , message="Merci d'entrez un nombre entier non null")

                    # Affichez la fenêtre
                    affichage_graphe()
                M_Button.clicked = False
                M_Button.config(command=gener_matrice)
                if M_Button.clicked == False:
                    M_Button.config(command=Cree_graph)
                    M_Button.clicked = True
                    
                    
                visited = [] # List for visited nodes.
                queue = []     #Initialize a queue
                
                def bfs(visited, graph):
                     node = int(display())
                     visited.append(node)
                     queue.append(node)
                     Liste =  str(node) + ":" 
                   
                     while queue:          # Creating loop to visit each node
                       m = queue.pop(0) 
                       print (m, end = " ")
                       Liste += str(m) + "->"
                       
                   
                       for neighbour in graph[m]:
                         if neighbour not in visited:
                           visited.append(neighbour)
                           queue.append(neighbour)
                    
                     print(Liste)
                     label_bfs =tk.Label(cadre_M,text="BFS :{}".format(Liste))
                    #  label_bfs.config(text=Liste)
                     label_bfs.grid(row=5+L, column=0)
                
                
                visited_dfs = set()
                Liste_dfs=""
                Liste2 = []
                def dfsM2(visited_dfs, graph, node):  #function for dfs
                    
                    def dfs2(visited_dfs, graph, node):
                        Liste =  str(node) + ":"
                        if node not in visited_dfs:
                        #    print (node)
                           Liste =  str(node) + ":"
                        #    Liste_dfs.insert(tk.END, node + " ")  # Ajouter le nœud visité à la fin du widget de texte avec un espace

                           visited_dfs.add(node)
                           for neighbour in graph[node]:
                               dfs(visited_dfs, graph, neighbour)
                               
                               
                               
                               
                        print(Liste2)
                        return Liste
                    t= dfs2(visited_dfs, graph, node)
                    
                # print(Liste_dfs)
                
                           
                matrix_dict = nx.to_dict_of_lists(G)
                # button_bfs = tk.Button(cadre_M, text="Parcours BFS", command= lambda:bfs(visited, G))
                # button_bfs.grid(row=3+L, column=2, pady=10)
                
                # button_bfs = tk.Button(cadre_M, text="Parcours DFS", command= lambda:dfsM2(visited_dfs, G, 0 , Liste2))
                # button_bfs.grid(row=3+L, column=3, pady=10)
                # Liste2_str = "->".join(Liste2)
                # print(Liste2_str)
                

                   
                

            window_M=tk.Toplevel()
            window_M.title("Matrice")
             #root.geometry("1000x600")
            window_M.configure(bg='#CCE5FF')

            cadre_M = tk.Frame(window_M, width=200, height=200, bd=1, relief=tk.SOLID, bg='#CCE5FF' )
            cadre_M.grid(row=0, column=0, padx=10, pady=10)
            #Nombre de Sommet // nodes 
            Label=tk.Label(cadre_M, text="Nombre du sommets: " , bg='#CCE5FF')
            Label.grid(row=0, column=0)
            Nbr_Sommet = tk.StringVar()
            entry =  tk.Entry(cadre_M , textvariable=Nbr_Sommet)
            entry.grid(row=0, column=1)


            #boutton de validation // ganeration du matrice adj
            Button = tk.Button(cadre_M , text = "Valider" , command=gener_matrice)
            Button.grid(row=0, column=3)
            """frame = tk.Frame(master=window_M , bg="red")
            frame.grid(row=0, column= 30)"""
            
            
            # def generate_dict(self):
            #     if self.matrix is None:
            #         print("La matrice n'a pas encore été créée.")
            #         return
            #     matrix_dict = {}
            #     for i in range(self.num_sommets):
            #         nom_sommet = self.noms_sommets[i].get()
            #         voisins = []
            #         for j in range(self.num_sommets):
            #             if int(self.matrix[i][j].get()) == 1:
            #                 voisins.append(self.noms_sommets[j].get())
            #         matrix_dict[nom_sommet] = voisins
            #         self.matrix_dict = matrix_dict
                
            #     visited = [] # List for visited nodes.
            #     queue = []     #Initialize a queu
            #     def bfs(visited, graph, node): #function for BFS
            #       visited.append(node)
            #       queue.append(node)
            #       while queue:          # Creating loop to visit each node
            #         m = queue.pop(0) 
            #         print (m, end = " ")
            #         for neighbour in graph[m]:
            #           if neighbour not in visited:
            #             visited.append(neighbour)
            #             queue.append(neighbour)
            #     tk.Button(cadre_M,text="bfs",command=self.bfs(self.matrix_dict,'0')).grid(row=1,column=3)
            #     dict_text = tk.Text(cadre_M, height=10, width=40)
            #     dict_text.pack()
            #     dict_text.insert(tk.END, str(matrix_dict))

            
         
            
            window_M.mainloop()
            #afficher_caracteristiques_graphe(G)     

        
        ######################Appele des fcts ############
        # 
        matrice()
         
        
         #afficher_caracteristiques_graphe(G)
        #afficher_graphe(G)
        
    else:
            def creer_graphe():
                # Récupérer les arêtes et les coûts entrés par l'utilisateur
                arretes_str = entree_arretes.get()
                couts_str = entree_couts.get()

                # Séparer les arêtes individuelles et les coûts correspondants
                arretes_liste = arretes_str.split(',')
                couts_liste = couts_str.split(',')

                # Ajouter les arêtes avec les coûts au graphe
                for i, arrete in enumerate(arretes_liste):
                    # Séparer les nœuds de l'arête
                    noeuds = arrete.split('-')
                    # Vérifier le format correct des nœuds
                    if len(noeuds) == 2:
                        # Vérifier si le coût est disponible pour cette arête
                        if i < len(couts_liste):
                            cout = couts_liste[i]
                        else:
                            cout = ''  # Coût par défaut si non spécifié
                        G.add_edge(noeuds[0], noeuds[1], weight=float(cout))

                # Afficher le graphe dans une nouvelle fenêtre
                fenetre_G = tk.Toplevel()
                fenetre_G.title("Affichage du graphe")
                fenetre_G.geometry("500x500")

                cadre_figure = tk.Frame(fenetre_G)
                cadre_figure.pack()

                fig = plt.figure(figsize=(6, 6))
                canvas = FigureCanvasTkAgg(fig, master=cadre_figure)
                canvas.draw()
                canvas.get_tk_widget().pack()

                pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold')

                # Afficher les coûts sur les arêtes du graphe
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
               
                afficher_caracteristiques_graphe(G)

                fenetre_G.mainloop()
                #afficher_caracteristiques_graphe(G)     

            # Créer la fenêtre principale
            window = tk.Tk()
            window.title("Création du graphe")
            window.geometry("400x250")

            # Créer une zone de texte pour saisir les arêtes
            label_arretes = tk.Label(window, text="Entrer les arêtes du graphe (séparées par des virgules ; ex: a-b,c-d):")
            label_arretes.pack()

            entree_arretes = tk.Entry(window)
            entree_arretes.pack()

            # Créer une zone de texte pour saisir les coûts des arêtes
            label_couts = tk.Label(window, text="Entrer les coûts des arêtes (séparés par des virgule ; ex: 2,3.5,1):")
            label_couts.pack()

            entree_couts = tk.Entry(window)
            entree_couts.pack()

            # Créer un bouton pour générer le graphe
            bouton_creer = tk.Button(window, text="Créer le graphe", command=creer_graphe)
            bouton_creer.pack()

            window.mainloop()
            def bfs(graphe, start):
                if graphe is None:
                    print("Le graphe n'a pas été créé.")
                    return
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
                            visited.append(neighbor)
            # bfs(G, '1')
    # def choix_algo():
    #     return
 

    
###################################################  MENU ############################################################
root=tk.Tk()
root.title("Théorie des graphes")
root.geometry()
root.configure(bg='#CCE5FF')
#message
Label=tk.Label(root, text="Merci d'entrer des informations sur le graphe" ,font=(10), bg='#CCE5FF').grid(row=0, column=0)
Label=tk.Label(root, text="Le graphe est non orienté et non pondére par defaut" ,font=(None, 12), bg='#CCE5FF').grid(row=1, column=0)


#Orienter le graphe 
check_state_o = tk.IntVar()
check_oriente = tk.Checkbutton(root, text="graphe orienté", var=check_state_o, bg='#CCE5FF')
check_oriente.grid(row=3, column=0)
 # Pondération
check_state_p= tk.IntVar()
check_poneration = tk.Checkbutton(root, text="graphe pondéré", var=check_state_p, bg='#CCE5FF')
check_poneration.grid(row=4, column=0)
Button = tk.Button(root , text = "Valider" ,command =choix)
Button.grid(row=5, column=0)

root.mainloop()