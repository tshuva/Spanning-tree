from graph import *


def q2(g, source, destination, w):
    src = g.V[source]
    dest = g.V[destination]
    src_visited_vertices = [src]
    dest_visited_vertices = [dest]
    while dest not in src_visited_vertices and src not in dest_visited_vertices:
        if dest.pi is not None:
            dest = dest.pi
            dest_visited_vertices.append(dest)
        if src.pi is not None:
            src = src.pi
            src_visited_vertices.append(src)

    start_of_circle = dest if dest in src_visited_vertices else src
    src = g.V[source]
    dest = g.V[destination]
    max_edge = (Edge(source, destination), w[source][destination])
    curr = Vertex(-1)
    while dest != start_of_circle or src != start_of_circle:
        if ((dest == start_of_circle) or
                (src is not start_of_circle and
                 w[src.id][src.pi.id] >= w[dest.id][dest.pi.id])):
            curr = src
            src = src.pi
        else:
            curr = dest
            dest = dest.pi
        curr_weight = w[curr.id][curr.pi.id]
        if curr_weight > max_edge[1]:
            max_edge = (Edge(curr.pi.id, curr.id), curr_weight)

    g_max_dest = g.V[max_edge[0].dest]
    g_max_src = g.V[max_edge[0].src]
    if [source, destination] != [max_edge[0].src, max_edge[0].dest]:
        if all(vertex in dest_visited_vertices for vertex in [g_max_src, g_max_dest]):
            remove_edge(dest_visited_vertices[:1 + dest_visited_vertices.index(g_max_dest)],
                        g.V[source], g.V[destination], w)
        elif all(vertex in src_visited_vertices for vertex in [g_max_src, g_max_dest]):
            remove_edge(src_visited_vertices[:1 + src_visited_vertices.index(g_max_dest)],
                        g.V[destination], g.V[source], w)


def remove_edge(list, new_edge_src, new_edge_dest, w):
    for i in range(len(list))[1:]:
        list[i].pi = list[i - 1]
        list[i].key = w[list[i].id][list[i - 1].id]
    new_edge_dest.pi = new_edge_src
    new_edge_dest.key = w[new_edge_dest.id][new_edge_src.id]
