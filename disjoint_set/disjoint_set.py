class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v: v for v in self.vertices}
        self.rank = {v: 0 for v in self.vertices}

    def find(self, item):
        if item not in self.parent:
            return

        elif self.parent[item] == item:
            return item

        else:
            return self.find(self.parent[item])

    # Do union by rank
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            print("These elements have the same root! Cannot perform union operation!")
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root

        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root

        else:
            self.parent[y_root] = x_root
            self.rank[x_root]+=1

ds = DisjointSet([1, 2, 3, 4, 5])
print(ds.parent)
ds.union(1, 2)
ds.union(3, 4)
ds.union(3, 5)
ds.union(1, 3)
print(ds.parent)
print(ds.find(5))
