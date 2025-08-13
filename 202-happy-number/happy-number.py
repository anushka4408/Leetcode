class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        def sumsquares(n):
            total=0
            while n>0:
                digit=n%10
                total+=digit**2
                n=n//10

            return total
        while n!=1 and n not in seen:
            seen.add(n)
            n=sumsquares(n)
        return n==1