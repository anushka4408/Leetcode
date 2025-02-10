class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        # Create seperate rows and columns
        rows=[0]*m
        col=[0]*n
        count=0

        # Increment rows and column seperately
        for ri,ci in indices:
            rows[ri]+=1
            col[ci]+=1

# count odd by adding row and column at each indice
        for i in range(m):
            for j in range(n):
                if((rows[i]+col[j])%2 !=0):
                    count+=1
        return count
                
            
