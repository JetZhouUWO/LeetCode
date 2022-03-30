class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        #rst = address.split(".")
        return "[.]".join(item for item in address.split("."))
        