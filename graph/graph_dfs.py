from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency = defaultdict(list)

    def add_vertex(self, x, y):
        if y not in self.adjacency[x]:
            self.adjacency[x].append(y)

        if x not in self.adjacency[y]:
            self.adjacency[y].append(x)

class GraphDFS:
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, starting):
        if not self.graph:
            return

        stack = []
        visited = []
        stack.append(starting)

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)

            for neighbor in self.graph.adjacency[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        print(visited)

    def dfs_v2(self, starting):
        visited = []

        def dfs_recursive(node):
            nonlocal visited
            visited.append(node)

            for neighbor in self.graph.adjacency[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(starting)
        print(visited)

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

gdfs = GraphDFS(g)
gdfs.dfs_v2("A")
