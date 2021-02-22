class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        found = []
        for word in d:
            p = 0
            for c in s:
                if c == word[p]:
                    p += 1
                    if p == len(word):
                        found.append(word)
                        break
        found.sort()
        longest = ''
        for word in found:
            if len(word) > len(longest):
                longest = word
        return longest


s = "abpcplea"
d = ["ale", "monkey", "plea", "apple"]
# s = "abpclplea"
# d = ["a", "b", "c"]
ts = [("abpcplea", ["ale", "monkey", "plea", "apple"]),
      ("abpclplea", ["a", "b", "c"]),
      ("fdopughclnkkalucdaqrtd", ["fuck", "doughnut", "placard"]),
      ("fdopughclnkkalucdaqrtd", ["fuck", "doug", "placard"]),
      ("", ["superman", "food", "whatyousay"]),
      ("fsldfshs", [])]
soln = Solution()
for t in ts:
    print(soln.findLongestWord(t[0], t[1]))
