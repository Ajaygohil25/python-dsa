class Solution:
    # Time complexity (O N log N)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s = ''.join(sorted(s))
    #     t = ''.join(sorted(t))

    #     if s == t:
    #         return True
    #     else:
    #         return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in t:
                return False
            else:
                t = t.replace(s[i],'',1)
                print(t)
        return True

obj = Solution()

# result = obj.isAnagram("rat", "car")
# result2 = obj.isAnagram("aacc", "ccac")
result3 = obj.isAnagram("anagram","nagaram")
# print(result)
print(result3)