class SlowDisjointSet:
    def __init__(self, N):
        self.N = N
        self._bubbles = []
        for i in range(N):
            self._bubbles.append({i})
        self._operations = 0
        self._calls = 0
    
    def _find_i(self, i):
        """
        Find the index of the bubble that holds a particular
        value in the list of bubbles
        Parameters
        ----------
        i: int
            Element we're looking for
        
        Returns
        -------
        Index of the bubble containing i
        """
        index = -1
        k = 0
        while k < len(self._bubbles) and index == -1:
            for item in self._bubbles[k]:
                self._operations += 1
                if item == i:
                    index = k
                    break
            k += 1
        return index
                
   
    def find(self, i, j):
        """
        Return true if i and j are in the same component, or
        false otherwise
        Parameters
        ----------
        i: int
            Index of first element
        j: int
            Index of second element
        
        """
        self._calls += 1
        id_i = self._find_i(i)
        id_j = self._find_i(j)
        
        if id_i == id_j:
            return True
        else:
            return False
    
    def union(self, i, j):
        """
        Merge the two sets containing i and j, or do nothing if they're
        in the same set
        Parameters
        ----------
        i: int
            Index of first element
        j: int
            Index of second element
        """
        self._calls += 1
        idx_i = self._find_i(i)
        idx_j = self._find_i(j)
        if idx_i != idx_j:
            # Merge lists
            # Decide that bubble containing j will be absorbed into
            # bubble containing i
            self._operations += len(self._bubbles[idx_i]) + len(self._bubbles[idx_j])
            self._bubbles[idx_i] |= self._bubbles[idx_j]
            # Remove the old bubble containing j
            self._bubbles = self._bubbles[0:idx_j] + self._bubbles[idx_j+1::]