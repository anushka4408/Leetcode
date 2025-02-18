class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # for i in range(len(letters)):
        #     if(letters[i]>target):
        #         return letters[i]
        # return letters[0]
        low=0
        high=len(letters)-1
        while low<=high:
            mid=(low+high)//2
            if(letters[mid]<=target):
                low=mid+1
            elif(letters[mid]>target):
                high=mid-1
        return letters[low%len(letters)]
                
        