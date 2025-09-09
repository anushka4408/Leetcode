class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        # """
        # def ispalindrome(sub):
        #     if(sub==sub[::-1]):
        #         return True
        #     return False
        # def lps(left,right):
        #     if left>right:
        #         return ""
        #     sub=s[left:right+1]
        #     if ispalindrome(sub)==True:
        #         return sub
        #     leftstr=lps(left+1,right)
        #     rightstr=lps(left,right-1)

        #     return leftstr if len(leftstr)>=len(rightstr) else rightstr

        # return lps(0,len(s)-1)


        if not s:
            return ""

        start, end = 0, 0  # track longest palindrome boundaries

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1  # valid palindrome boundaries

        for i in range(len(s)):
            # Odd length palindrome
            l1, r1 = expandAroundCenter(i, i)
            # Even length palindrome
            l2, r2 = expandAroundCenter(i, i + 1)

            # update longest
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]


        
        
