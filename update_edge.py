from graph import *

def q2(g, source, destination, w):
	src = g.V[source]
	dest = g.V[destination]
	src_visted_veritces=[src]
	dest_visted_veritces=[dest]
	while( dest not in src_visted_veritces and src not in dest_visted_veritces):
		if dest.pi is not None:
			 dest = dest.pi
			 dest_visted_veritces.append(dest)
		if src.pi is not None:
			src = src.pi
			src_visted_veritces.append(src)
	
	start_of_circle = dest  if dest in src_visted_veritces else src
	src = g.V[source]
	dest = g.V[destination]
	max_edge = (Edge(source,destination), w[source][destination])
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
		currWight = w[curr.id][curr.pi.id]
		if currWight > max_edge[1]:
			max_edge = (Edge(curr.pi.id, curr.id), currWight)
			
	g_max_dest = g.V[max_edge[0].dest]
	g_max_src = g.V[max_edge[0].src]
	if ([source,destination] != [max_edge[0].src,max_edge[0].dest]):
		if  all(vertex in dest_visted_veritces for vertex in [g_max_src, g_max_dest]):
			remove_edge(dest_visted_veritces[:1 + dest_visted_veritces.index(g_max_dest)],
						g.V[source], g.V[destination], w) 
		elif all(vertex in src_visted_veritces for vertex in [g_max_src, g_max_dest]):
			remove_edge(src_visted_veritces[:1 + src_visted_veritces.index(g_max_dest)],
						g.V[destination], g.V[source], w)


def remove_edge(list,new_edge_src,new_edge_dest,w):
	for i in range(len(list))[1:]:
		list[i].pi = list[i-1]
		list[i].key = w[list[i].id][list[i-1].id] 
	new_edge_dest.pi = new_edge_src
	new_edge_dest.key = w[new_edge_dest.id][new_edge_src.id]
