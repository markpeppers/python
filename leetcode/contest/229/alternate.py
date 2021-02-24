class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = 0
        if len(word1) > len(word2):
            length = len(word1)
        else:
            length = len(word2)
        ans = ''
        for i in range(length):
            if i < len(word1):
                ans = ans + word1[i]
            if i < len(word2):
                ans = ans + word2[i]
        return ans


soln = Solution()
print(soln.mergeAlternately('abcd', 'dddddd'))
