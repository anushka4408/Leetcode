class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count=0
        # for item in items:
        #     if(ruleKey=='type' and ruleValue==item[0]):
        #         count+=1
        #     if(ruleKey=='color' and ruleValue==item[1]):
        #         count+=1
        #     if(ruleKey=='name' and ruleValue==item[2]):
        #         count+=1
        # return count

        keyindex={"type":0,"color":1,"name":2}
        if ruleKey not in keyindex:
            return 0
        for item in items:
            if(ruleValue==item[keyindex[ruleKey]]):
                count+=1
        return count