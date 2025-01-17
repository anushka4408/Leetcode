class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x:(bin(x).count('1'),x))
# lambda x: (bin(x).count('1'), x) defines a small function that takes x and returns a tuple (bin(x).count('1'), x).
# This tuple is used by sorted() to determine the sorting order:
# Primary criterion: The number of 1s in the binary representation (bin(x).count('1')).
# Secondary criterion: The integer value itself (x).


# A lambda in Python is a way to define a small, anonymous (unnamed) function in a single line of code. It's particularly useful when you need a short function for a specific task without the overhead of defining it using the def keyword.

# The syntax for a lambda function is:
# add = lambda x, y: x + y
# print(add(3, 5))  # Output: 8
# nums = [1, 2, 3, 4]
# squared = map(lambda x: x ** 2, nums)
# print(list(squared))  # Output: [1, 4, 9, 16]