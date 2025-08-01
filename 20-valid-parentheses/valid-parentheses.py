class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #  { ( { } ) }
        stack=[]
        dic={")":'(','}':'{',']':'['}
        for i in s:
            if(i in dic.values()):
                stack.append(i)
            elif(i in dic):
                if(len(stack)!=0 and stack[-1]==dic[i]):
                    stack.pop()
                else:
                    return False
        return len(stack)==0