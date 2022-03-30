class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        for i in range(len(operations)):
            operations[i] = -1 if "--" in operations[i] else 1
        return sum(operations)