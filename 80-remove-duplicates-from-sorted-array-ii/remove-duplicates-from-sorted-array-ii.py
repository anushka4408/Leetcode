class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if(n<=2):
            return n
        write=2
        for i in range(2,len(nums)):
            if(nums[i]!=nums[write-2]):
                nums[write]=nums[i]
                write+=1
        return write

#         | Step | `read` | `write` | `nums[read]` | `nums[write-2]` | Action            | Updated `nums`               |
# | ---- | ------ | ------- | ------------ | --------------- | ----------------- | ---------------------------- |
# | 0    | —      | 2       | —            | —               | Initialization    | \[0, 0, 1, 1, 1, 1, 2, 3, 3] |
# | 1    | 2      | 2       | 1            | 0               | ✅ 1 ≠ 0 → Keep it | \[0, 0, 1, 1, 1, 1, 2, 3, 3] |
# | 2    | 3      | 3       | 1            | 0               | ✅ 1 ≠ 0 → Keep it | \[0, 0, 1, 1, 1, 1, 2, 3, 3] |
# | 3    | 4      | 4       | 1            | 1               | ❌ 1 == 1 → Skip   | No change                    |
# | 4    | 5      | 4       | 1            | 1               | ❌ 1 == 1 → Skip   | No change                    |
# | 5    | 6      | 4       | 2            | 1               | ✅ 2 ≠ 1 → Keep it | \[0, 0, 1, 1, 2, 1, 2, 3, 3] |
# | 6    | 7      | 5       | 3            | 1               | ✅ 3 ≠ 1 → Keep it | \[0, 0, 1, 1, 2, 3, 2, 3, 3] |
# | 7    | 8      | 6       | 3            | 2               | ✅ 3 ≠ 2 → Keep it | \[0, 0, 1, 1, 2, 3, 3, 3, 3] |

        
        