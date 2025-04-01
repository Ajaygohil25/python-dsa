# Word Subsets
# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.



class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        wordFre = {}
        for i in words1:
            pass

solution_obj = Solution()
print(solution_obj.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))
print(solution_obj.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]))
# print("e" in "leetcode")

print("lo" in "google")