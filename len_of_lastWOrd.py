class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_split = s.split(" ")
        return len(s_split[-1])

sobj = Solution()
print(sobj.lengthOfLastWord("   fly me   to   the moon  "))