class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def rotatemat(mat):
            transpose=[[0]*len(mat) for i in range(len(mat[0]))]
            for i in range(len(mat[0])):
                for j in range(len(mat)):
                    transpose[i][j]=mat[j][i]

            for i in range(len(transpose)):
                transpose[i].reverse()

            return transpose
        for i in range(4):
            if(mat==target):
                return True
            mat=rotatemat(mat)

        return False