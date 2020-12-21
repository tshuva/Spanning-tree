from graph import *
import random
from prim import *
from update_edge import q2


def generate_weights(edges):
    weights = [[float('inf') for i in range(N)] for j in range(N)]
    for e in edges:
        if weights[e.src][e.dest] == float('inf'):
            w = random.randint(1, 100)
            weights[e.src][e.dest] = w
            weights[e.dest][e.src] = w
    return weights


def max_with_inf(list):
    maximum = float('-inf')
    for item in list:
        if item > maximum and item !=float('inf'):
            maximum = item
    return maximum


def new_edge(g, w, src ,dest, new_w):
    w[src][dest] = new_w 
    w[dest][src] = new_w 
    g.adj[src].append(dest)
    g.adj[dest].append(src) 


def q1(g, w,r):
    mst_prim(g, w, r)
    print_mst(g, r)


if __name__ == '__main__':
    g = Graph()
    w = generate_weights(g.E)
    g.print_graph(w)
    r = g.V[random.randint(0, len(g.V) - 1)]  # pick random start
    q1(g, w, r)

    src = random.randint(0, N - 1)
    dest = random.randint(0, N - 1)
    while (dest in g.adj[src] or src == dest):           
        src = random.randint(0, N - 1)
        dest = random.randint(0, N - 1)     
    
    # make new edge the most 'expensive' for both veritces
    new_w = max(max_with_inf(x) for x in w)  + 1 
    new_edge(g, w, src, dest, new_w)
    print("First try: \n The new edge is " + str(Edge(src,dest)) + " and thie weight is " + str(new_w))
    q2(g, src, dest, w)
    print_mst(g, r)

    # make new edge the most 'cheap' for both veritces
    new_w = min(w[src] + w[dest]) - 1
    new_edge(g, w, src, dest, new_w)
    print("second try: \n  The new edge is " +str(Edge(src,dest)) + " and the weight is " + str(new_w))
    q2(g, src, dest, w)
    print_mst(g, r)
