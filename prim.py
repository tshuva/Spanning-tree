from heap import *
from globals import *


def mst_prim(graph, w, r):
    Q = Heap()
    items = graph.V
    for v in items:
        v.key = float('inf')
    r.key = 0
    r.pi = None
    Q.build_heap(items)

    while Q.currentSize > 0:
        u = Q.extract_min()
        for v in graph.adj[u.id]:
            v = graph.V[v]
            if v in Q.heapList[1:] and w[u.id][v.id] < v.key:
                v.pi = u
                v.key = w[u.id][v.id]


def print_mst(g):
    for v in g.V:
        temp = v
        while temp.pi is not None:
            print(str(temp.id + 1) + ' <-- ', end='')
            temp = temp.pi
        print(str(temp.id + 1))
