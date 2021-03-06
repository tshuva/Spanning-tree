# מיקי מאירסון 207349010
# נעם תשובה 207576109

from prim import *
from update_edge import q2
from graph import *


def generate_weights(edges):
    weights = [[float('inf') for i in range(N)] for j in range(N)]
    for e in edges:
        if weights[e.src][e.dest] == float('inf'):
            w = random.randint(1, MAX_WEIGHT)
            weights[e.src][e.dest] = w
            weights[e.dest][e.src] = w
    return weights


if __name__ == '__main__':

    " Create graph and weights and print them "
    g = Graph()
    w = generate_weights(g.E)
    g.print_graph(w)
    r = g.V[random.randint(0, len(g.V) - 1)]  # pick random start

    " Build MST with Prim algorithm and print it "
    q1(g, w, r)

    src = random.randint(0, N - 1)
    dest = random.randint(0, N - 1)
    while dest in g.adj[src] or src == dest:
        src = random.randint(0, N - 1)
        dest = random.randint(0, N - 1)

    " Create new edge that is the most 'expensive' in graph "
    new_w = MAX_WEIGHT + 1
    new_edge(g, w, src, dest, new_w)
    print("First try: \n The new edge is " + str(Edge(src, dest)) + " and thie weight is " + str(new_w))

    " Recalculate MST with an edge that does not affect it "
    q2(g, src, dest, w)
    print_mst(g, r)

    " Create new edge that is the 'cheapest' in graph "
    new_w = 0
    new_edge(g, w, src, dest, new_w)
    print("second try: \n  The new edge is " + str(Edge(src, dest)) + " and the weight is " + str(new_w))

    " Recalculate MST with an edge that affects it "
    q2(g, src, dest, w)
    print_mst(g, r)
