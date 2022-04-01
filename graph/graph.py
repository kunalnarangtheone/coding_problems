class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if not vertex in self.adjacency:
            self.adjacency[vertex] = []

    def add_neighbor(self, vertex, neighbor):
        if neighbor not in self.adjacency[vertex]:
            self.adjacency[vertex].append(neighbor)

    def __str__(self):
        return f"The graph is: {self.adjacency}"

def create_graph():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)

    g.add_neighbor(1, 2)
    g.add_neighbor(1, 4)
    g.add_neighbor(2, 3)
    g.add_neighbor(3, 1)
    return g

def create_graph_2():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_vertex("G")

    g.add_neighbor("A", "B")
    g.add_neighbor("A", "C")
    g.add_neighbor("B", "A")
    g.add_neighbor("B", "D")
    g.add_neighbor("B", "G")
    g.add_neighbor("C", "A")
    g.add_neighbor("C", "D")
    g.add_neighbor("C", "E")
    g.add_neighbor("D", "B")
    g.add_neighbor("D", "C")
    g.add_neighbor("D", "F")
    g.add_neighbor("E", "C")
    g.add_neighbor("E", "F")
    g.add_neighbor("F", "D")
    g.add_neighbor("F", "E")
    g.add_neighbor("F", "G")
    g.add_neighbor("G", "B")
    g.add_neighbor("G", "F")
    return g
