class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count=0
        window=arr[0:k]
        if(sum(window)//k>=threshold):
            count+=1
        for i in range(k,len(arr)):
            window.append(arr[i])
            window.pop(0)
            if(sum(window)//k>=threshold):
                count+=1
        return count
            
            
        
