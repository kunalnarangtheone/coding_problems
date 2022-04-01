
class NumIslands:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [[False for j in range(len(self.graph[0]))] for i in range(len(self.graph))]


    def dfs(self, i, j):
        if i < 0 or i > len(self.graph) - 1 or j < 0 or j >= len(self.graph[0]) - 1 or self.visited[i][j]:
            return

        else:
            self.visited[i][j] = True

            self.dfs(i - 1, j + 1)
            self.dfs(i, j + 1)
            self.dfs(i + 1, j + 1)
            self.dfs(i - 1, j)
            self.dfs(i + 1, j)
            self.dfs(i - 1, j - 1)
            self.dfs(i, j - 1)
            self.dfs(i + 1, j - 1)

    def num_islands(self):
        count = 0
        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                if self.graph[i][j] == 1:
                    self.dfs(i, j)
                    count += 1

        return count

graph = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

n_islands = NumIslands(graph)
print(n_islands.num_islands())
