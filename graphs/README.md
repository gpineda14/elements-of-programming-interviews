# Graphs #

A graph is a set of vertices that are connected by edges. A directed graph is set of vertices and edges where given an edge e = (u, v), the vertex u is its source and v is its sink.

A path in a directed graph from u to v is sequence of vertices that connect together with the help of edges that go from u to v. The length of a path is the number of edges it traverses. If a path is reachable from u to v, we say that v is reachable from u.

A directed acyclic graph is a directed graph in which there are no cycles. Cycles are paths that contain one or more edges and begin and end with the same vertex. Vertices that don't have any incoming edges are known as sources and vertices that don't have any outgoing edges are sinks. A topological ordering of vertices in a DAG is an ordering of the vertices in which each edge is from a vertex earlier in the ordering to a vertex later in the ordering.

An undirected graph is set of edges and vertices, except the edges do not have direction. If u and v are in an undirected graph, they are said to be connected if there is a path from u to v. A connected component is a set of vertices where each pair of vertices is connected. Every vertex belongs to one connected component. A directed graph is said to be weakly connected if replacing all of its directed edges to undirected edges produces an undirected graph that is connected. It is connected if it contains a directed path from u to v or from v to u for every pair of vertices u and v. It is strongly connected if it contains a directed path from u to v and a directed path from v to u for every pair of vertices u and v.

Graphs can be implemented using adjacency lists or adjacency matrices. Adjacency lists have for every vertex a list of vertices to which it has an edge. Adjacency martices are V x V boolean-valued matrices where index represents the vertex and a 1 indicating the presence of an edge. So if A[0][1] = 1, then there is an edge between vertex 0 and 1.

## Tips for dealing with Graph problems ##

1. Graphs are ideal for modeling and analyzing relationships between pairs of objects
2. Use graphs for spatially connected objects such as road segments
3. Use graphs when you need to analyze any binary relationship between objects. They can quite often be reduced to well-known graph problems
4. Some graph problems entail analyzing the graph structure such as looking for cycles or connected components. DFS work particularly well for these applications.
5. Some graph problems are related to optimization such as finding the shortest path. You can use BFS, Dijkstra's algorithm, and minimum spanning tree for these sort of optimizations.
6. DFS and BFS for graphs is O(|V| + |E|) with space complexity of O(|V|)
7. BFS can be used to compute distances from the start vertex
8. DFS can be used to check for presence of cycles 
