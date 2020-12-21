import random
from globals import *


def generate_veritces():
    return [Vertex(id=i) for i in range(N)]


def generate_edges():
    edges = []
    not_Visted = list(range(0, N))
    src = random.choice(not_Visted)
    first = src

    while len(not_Visted) > 0:
        not_Visted.remove(src)
        dest = random.choice(not_Visted) if not_Visted else first
        e = Edge(src, dest)
        if not (e.src == e.dest or e in edges):
            edges.append(e)
            src = dest

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

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.key > other.key

    def __lt__(self, other):
        return self.key < other.key
    
    def __str__(self):
        return str(self.id + 1)
    
    def __repr__(self):
        return "vertix " + str(self.id + 1)


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __eq__(self, other):
        a = self.src == other.src and self.dest == other.dest
        b = self.src == other.dest and self.dest == other.src
        return a or b

    def __str__(self):
        return "Edge " + str(self.src + 1)+ " ~> " + str(self.dest + 1)
    def __repr__(self):
        return "Edge " + str(self.src + 1)+ " ~> " + str(self.dest + 1)

class Graph:

    def __init__(self, Vertexs=list(), edges=list()):
        self.V = Vertexs if Vertexs else generate_veritces()
        self.E = edges if edges else generate_edges()        

        # create adjacency lists
        self.adj = [[] for v in self.V]

        # add each edge to its proper adj list - each edge goes both ways (undirected graph)
        for e in self.E:
            self.adj[e.src].append(e.dest)
            self.adj[e.dest].append(e.src)

    def print_graph(self, w=None):
        for i in range(len(self.V)):
            print("Vertex " + str(i + 1) + ":", end="")
            temp = self.adj[i]
            for t in sorted(temp):
                print(" -({})-> {}".format(w[i][t], t + 1), end='\n\t\t ')
            print(" \n")