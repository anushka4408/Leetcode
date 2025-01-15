class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        newarr=[]
        i=0
        arr1.sort()
        for i in arr2:
            while i in arr1:
                arr1.remove(i)
                newarr.append(i)
        newarr.extend(arr1)
        return newarr
