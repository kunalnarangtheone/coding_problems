from collections import defaultdict

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v: v for v in self.vertices}
        self.rank = {v: 0 for v in self.vertices}

    def find(self, node):
        if self.parent[node] == node:
            return node

        else:
            return self.find(self.parent[node])

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root

        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root

        else:
            self.parent[y_root] = x_root
            self.rank[x_root]+=1

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacency = defaultdict(list)
        self.graph = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    def add_edge_to_graph(self, source, target, weight):
        if (source, target, weight) not in self.graph:
            self.graph.append((source, target, weight))

    def add_edge(self, source, target):
        if target not in self.adjacency[source]:
            self.adjacency[source].append(target)

        if source not in self.adjacency[target]:
            self.adjacency[target].append(source)

    def kruskal(self):
        self.graph.sort(key = lambda x: x[2])
        cost = 0
        ds = DisjointSet(self.vertices)
        vertices = ds.vertices

        for source, target, weight in self.graph:
            s, t = ds.find(source), ds.find(target)

            if s != t:
                ds.union(s, t)
                self.add_edge(source, target)
                cost+=weight

        print(self.adjacency)
        print(f"Cost: {cost}")


g = Graph()
edges = [["A", "B", 5], ["B", "C", 10], ["B", "D", 8], ["C", "D", 6], ["A", "C", 13], ["A", "E", 15], ["C", "E", 20]]
for s, t, w in edges:
    g.add_vertex(s)
    g.add_vertex(t)
    g.add_edge_to_graph(s, t, w)

g.kruskal()
