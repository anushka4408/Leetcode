class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        com=[]
        for i in command:
            com.append(i)
        print(com)
        res=[]
        for i in range(len(com)):
            if(com[i]=='G'):
                res.append('G')
                print(res)
            elif(com[i]=='('):
                if(com[i+1]==')'):
                    res.append('o')
                    print(res)

                if(com[i+1]=='a'):
                    res.append('al')
                    print(res)

                else:
                    continue
        return ''.join(res)
        