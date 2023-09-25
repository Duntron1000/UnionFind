class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = []
        self._operations = 0
        self._calls = 0
        for i in range(self.N):
            self.parent.append(i)
    
    def root(self, i):
        while self.parent[i] != i:
            self._operations += 1
            i = self.parent[i]
        return i
        
    def union(self, i, j):
        self._calls += 1
        root_i = self.root(i)
        root_j = self.root(j)
        if root_i != root_j:
            self._operations += 1
            self.parent[root_j] = root_i
       
    def find(self, i, j):
        self._calls += 1
        return self.root(i) == self.root(j)
        
        