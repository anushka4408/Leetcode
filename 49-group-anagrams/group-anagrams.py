class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        for i in strs:
            sortedw=''.join(sorted(i))
            if(sortedw in dict):
                dict[sortedw].append(i)
            else:
                dict[sortedw]=[i]
        return dict.values()















        # dictionary={}
        # for word in strs:
    
        #     sortedword=''.join(sorted(word))
        #     if(sortedword in dictionary):
        #         dictionary[sortedword].append(word)
        #     else:
        #         dictionary[sortedword]=[word]
        # return dictionary.values()

        