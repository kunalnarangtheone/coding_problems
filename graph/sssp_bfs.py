from graph import create_graph_2
from queue import Queue

class SSSP:
    def __init__(self, starting = "A"):
        self.visited = []
        self.starting = starting
        self.graph = create_graph_2().adjacency
        self.parents = {node: None for node in self.graph}


    def sssp_bfs(self):
        if not self.graph:
            return

        q = Queue()
        q.put(self.starting)

        while not q.empty():
            vertex = q.get()

            if vertex not in self.visited:
                self.visited.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in self.visited:
                    q.put(neighbor)

                # Additionally put the unvisited adjacent
                if self.parents[neighbor] is None and neighbor != self.starting:
                    self.parents[neighbor] = vertex

    def sssp_path(self, end_node):
        node = end_node
        path = []

        while node is not None:
            path.append(node)
            node = self.parents[node]

        path.reverse()
        return path




sssp = SSSP()
sssp.sssp_bfs()
print(sssp.sssp_path("F"))
