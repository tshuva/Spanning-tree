from heap import *
from globals import *


def mst_prim(graph, w, r):
    Q = MinHeap(max_size=len(graph.V))
    Q.build_heap(graph.V)

    for v in Q.Heap:
        v.key = float('inf')
    r.key = 0
    r.pi = None

    Q.min_heapify(Q.FRONT)

    while Q.size > 0:
        u = Q.extract_min()
        for v in graph.adj[u.id]:
            v = graph.V[v]
            if v in Q.Heap and w[u.id][v.id] < v.key:
                v.pi = u
                v.key = w[u.id][v.id]


def print_mst(g):
    parents = [v.pi for v in g.V]
    print("Edge \tWeight")
    for i in range(N):
        print(str(parents[i]) + "-" + str(i) + '\t' + str(g.adj[i][parents[i]]))
