from prim import *
from update_edge import q2


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

    " Create new edge that is the most 'expensive' in the graph "
    new_edge(g, w, src, dest, MAX_WEIGHT + 1)
    print("First try: \n The new edge is " + str(Edge(src, dest)) + " and thie weight is " + str(MAX_WEIGHT + 1))

    " Recalculate MST with an edge that does not affect it "
    q2(g, src, dest, w)
    print_mst(g, r)

    " Create new edge that is the 'cheapest' in the graph "
    new_edge(g, w, src, dest, 0)
    print("second try: \n  The new edge is " + str(Edge(src, dest)) + " and the weight is " + str(0))

    " Recalculate MST with an edge that affects it "
    q2(g, src, dest, w)
    print_mst(g, r)
