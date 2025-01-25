class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=0
        b=0
        vowels=['a','e','i','o','u']
        
        for i in range(0,len(s)//2):
            if(s[i].lower() in vowels):
                a+=1
            else:
                continue
        for i in range(len(s)//2,len(s)):
            if(s[i].lower() in vowels):
                b+=1
            else:
                continue
        if(a==b):
            return True
        else:
            return False
