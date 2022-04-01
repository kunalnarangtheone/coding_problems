from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjacency = defaultdict(list)

    def add_vertex(self, x, y):
        if y not in self.adjacency[x]:
            self.adjacency[x].append(y)

        if x not in self.adjacency[y]:
            self.adjacency[y].append(x)

class GraphBFS:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, starting):
        if not self.graph:
            return

        queue = deque()
        visited = set()
        queue.append(starting)
        visited.add(starting)

        while queue:
            node = queue.popleft()
            print(node)

            for neighbor in self.graph.adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()
g.add_vertex("A", "B")
g.add_vertex("A", "C")
g.add_vertex("B", "D")
g.add_vertex("B", "G")
g.add_vertex("C", "D")
g.add_vertex("C", "E")
g.add_vertex("D", "F")
g.add_vertex("E", "F")
g.add_vertex("F", "G")

gbfs = GraphBFS(g)
gbfs.bfs("A")
