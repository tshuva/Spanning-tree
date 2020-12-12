from heap import MinHeap
from graph import *
import random


def mst_prim(graph, w, r):
    Q = MinHeap(max_size=len(graph.V))
    Q.build_heap(graph.V)

    for v in Q.Heap:
        v.key = float('inf')
    r.key = 0
    r.pi = None
    while Q.Heap:
        u = Q.extract_min()
        for v in graph.adj[u]:
            if v in Q.Heap and w(u, v) < v.key:
                v.pi = u
                v.key = w(u, v)


def generate_weights(edges):
    weights = [[float('inf')] * N] * N
    for e in edges:
        if weights[e.src][e.dest] == float('inf'):
            w = random.randint(0, 100)
            weights[e.src][e.dest] = w
            weights[e.dest][e.src] = w
    return weights


def q1(g, w):
    r = g.V[random.randint(0, len(g.V) - 1)]  # pick random start
    mst_prim(g, w, r)

    # TODO trace back to get MST


if __name__ == '__main__':
    g = Graph()  # create graph
    g.print_graph()
    w = generate_weights(g.E)
    q1(g, w)
