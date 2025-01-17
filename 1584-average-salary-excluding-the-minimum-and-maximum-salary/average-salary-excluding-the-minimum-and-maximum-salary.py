class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()  # Sort the salary array
        return float(sum(salary[1:-1])/float(len(salary[1:-1])))
