class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)  # Target can be negative; we only care about distance
        sum_moves = 0
        num_moves = 0

        while sum_moves < target or (sum_moves - target) % 2 != 0:
            num_moves += 1
            sum_moves += num_moves

        return num_moves

        
            
            