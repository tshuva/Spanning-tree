from heap import *
from globals import *
from graph import *
from copy import deepcopy


def mst_prim(graph, w, r):
    Q = Heap()
    r.key = 0
    r.pi = None
    Q.build_heap(graph.V)
    while Q.currentSize > 0:
        u = Q.extract_min()
        for v in graph.adj[u.id]:
            v = graph.V[v]
            if v in Q.heapList[1:] and w[u.id][v.id] < v.key:
                v.pi = u
                v.key = w[u.id][v.id]
                Q.build_heap(Q.heapList[1:])


def print_mst(g, start):
    print('Printing MST starting from vertex {} with weight 0:'.format(start.id + 1))
    for v in [v for v in g.V if v != start]:
        print('Route to vertex {} (weight {}):'.format(v.id + 1, v.key), end='\t')
        temp = v
        str_to_print = ''
        while temp.pi is not None:
            str_to_print += str(temp.id + 1) + ' <-- '
            temp = temp.pi
        print(str_to_print + str(temp.id + 1))
