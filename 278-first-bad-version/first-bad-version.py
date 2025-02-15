# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for i in range(n+1):
        #     if(isBadVersion(i)==True):
        #         return i
        low=1
        high=n
        bad=[]
        while low<=high:
            mid=(low+high)//2
            if(isBadVersion(mid)==True):
                bad.append(mid)
                high=mid-1
            else:
                low=mid+1

        return min(bad)

        # while low < high:  # Use '<' to avoid unnecessary comparisons
        #     mid = (low + high) // 2  # Calculate the midpoint
        #     if isBadVersion(mid):  # If mid is bad
        #         high = mid  # Narrow down to the left part (including mid)
        #     else:
        #         low = mid + 1  # Narrow down to the right part (excluding mid)
        
        # # At the end of the loop, low == high and points to the first bad version
        # return low