class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        write = 0   # position to write compressed chars
        i = 0       # scanning pointer
        while i<n:
            ch=chars[i] #
            count=0     #
            while i<n and ch==chars[i]:
                i+=1
                count+=1   #
            chars[write]=ch  #
            write+=1        #
            if count>1:    #
                for c in str(count):  #
                    chars[write]=c
                    write+=1

        return write