class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        for i in range(len(sentences)):
            sentences[i] = len(sentences[i].split(" "))
        return max(sentences)
        