from graph import *
import random
from prim import *


def generate_weights(edges):
    weights = [[float('inf') for i in range(N)] for j in range(N)]
    for e in edges:
        if weights[e.src][e.dest] == float('inf'):
            w = random.randint(1, 100)
            weights[e.src][e.dest] = w
            weights[e.dest][e.src] = w
    return weights


def q1(g, w):
    r = g.V[random.randint(0, len(g.V) - 1)]  # pick random start
    mst_prim(g, w, r)
    print_mst(g, r)


if __name__ == '__main__':
    g = Graph()
    w = generate_weights(g.E)
    g.print_graph(w)
    q1(g, w)
    a=0
