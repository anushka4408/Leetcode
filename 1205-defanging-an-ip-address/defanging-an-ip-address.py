class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        new=address.split('.')
        res=('[.]').join(new)
        return res