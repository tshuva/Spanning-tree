import random
from globals import *


def generate_veritces():
    return [Vertice(id=i) for i in range(N)]


def generate_edges():
    edges = []
    while len(edges) < M:
        e = Edge(random.randint(0, N - 1), random.randint(0, N - 1))
        if not (e.src == e.dest or e in edges):
            edges.append(e)

    return edges


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __eq__(self, other):
        a = self.src == other.src and self.dest == other.dest
        b = self.src == other.dest and self.dest == other.src
        return a or b


class Vertice:
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


class Graph:

    def __init__(self, vertices=None, edges=None):
        self.V = vertices if vertices else generate_veritces()
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
