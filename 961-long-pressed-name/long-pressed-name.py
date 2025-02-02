class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # new=[]
        # for i in typed:
        #     if(i not in new):
        #         new.append(i)
        # new=''.join(new)
        # if(new==name):
        #     return True
        # return False
        w=list(typed)
        if(len(name)==len(typed)):
            if(name==typed):
                return True
            else:
                return False

        # for i in name:
        #     if i in w:
        #         w.remove(i)
        #         print(w)
        #     else:
        #         return False
        # return True
        i=0
        j=0
        while j<len(typed):
            if(i<len(name) and name[i]==typed[j]):
                i+=1
                j+=1
            elif(j>0 and typed[j]==typed[j-1]):
                j+=1
            else:
                return False
        return i==len(name)

        

