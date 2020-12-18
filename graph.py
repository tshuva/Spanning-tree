import random
from globals import *


def generate_veritces():
    return [Vertex(id=i) for i in range(N)]


def generate_edges():
    edges = []
    src = random.randint(0, N - 1)
    while len(edges) < M:
        dest = random.randint(0, N - 1)
        e = Edge(src, dest)
        if not (e.src == e.dest or e in edges):
            edges.append(e)
            src = dest

    return edges

class Vertex:
    def __init__(self, id, key=float('inf'), pi=float('inf')):
        self.id = id
        self.key = key
        self.pi = pi
        self.level = float('inf')

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.key > other.key

    def __lt__(self, other):
        return self.key < other.key
    
    def __str__(self):
        return str(self.id)
    
    def __repr__(self):
        return "vertix " + str(self.id)

    def __hash__(self):
        return hash(self.id)

class Edge:
    def __init__(self, src: Vertex, dest:Vertex):
        self.src = src
        self.dest = dest

    def __eq__(self, other):
        a = self.src == other.src and self.dest == other.dest
        b = self.src == other.dest and self.dest == other.src
        return a or b

class Graph:

    def __init__(self, Vertexs=list(), edges=list()):
        self.V = Vertexs if Vertexs else generate_veritces()
        self.E = edges if edges else generate_edges()
        
        self.graph = { v : list([]) for v in set(self.V) }
        self.set_edges(M)            

        # create adjacency lists
        self.adj = [[] for v in self.V]

        # add each edge to its proper adj list - each edge goes both ways (undirected graph)
        for e in self.E:
            self.adj[e.src].append(e.dest)
            self.adj[e.dest].append(e.src)

        " Make sure graph is connected"
        empty_lists = [index for index, lst in enumerate(self.adj) if lst == []]
        for v in empty_lists:
            self._connect_vertice(v)

    def _connect_vertice(self, vertice):
        dest = random.randint(0, N - 1)
        while dest == vertice:
            dest = random.randint(0, N - 1)
        self.E.append(Edge(vertice, dest))

        self.adj[vertice].append(dest)
        self.adj[dest].append(vertice)

    def print_graph(self, w=None):
        for i in range(len(self.V)):
            print("Vertex " + str(i + 1) + ":", end="")
            temp = self.adj[i]
            for t in sorted(temp):
                print(" -({})-> {}".format(w[i][t], t + 1), end='\n\t\t ')
            print(" \n")


    def set_edges(self,amount):
        count = 0
        while count < amount:
            if self.add_edge(random.randint(0, N - 1), random.randint(0, N - 1)):
                count = count + 1


    def add_edge(self,src=0,dest=N-1,wight=None):
        src_v = Vertex(src)
        dest_v = Vertex(dest)
        if src!=dest and not any(x for x in self.graph[src_v] if x[0] == dest_v) :
            w =  wight if wight else random.randint(1, 100)        
            self.graph[src_v].append((dest_v,w))
            self.graph[dest_v].append((src_v,w))
            return Edge(src_v,dest_v)
        return None

        
    
            