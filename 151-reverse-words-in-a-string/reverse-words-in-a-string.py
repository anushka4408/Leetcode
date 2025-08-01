class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        liststring=s.split()
        return ' '.join(liststring[::-1])