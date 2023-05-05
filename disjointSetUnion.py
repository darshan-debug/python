class UnionFind:
    def __init__(self, n: int):
        #  initially each node will be it's own representative.
        self.parent = list(range(n + 1))
        # stores the number of nodes in the components with the node as the root node, initially the size of component for each node is 1
        self.size = [1] * (n + 1)
        # stores the number of components in the graph, initially it will be equal to N as each node is considered a separate component
        self.components = n
    def find(self, x: int) -> int: #returns the root node in parent hierarchy
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x: int, y: int) -> int: #merges 2 set of nodes, if they are not merged 
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        if self.size[x] > self.size[y]:
            self.size[x] += self.size[y]
            self.parent[y] = x
        else:
            self.size[y] += self.size[x]
            self.parent[x] = y
        self.components -= 1
        return 1