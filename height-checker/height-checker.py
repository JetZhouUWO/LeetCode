class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        # print(expected)
        # print(heights)
        # diff = [a - b for a, b in zip(expected, heights)]
        # diff = [item for item in diff if item != 0]
        # return len(diff)
        count = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count+=1
        return count