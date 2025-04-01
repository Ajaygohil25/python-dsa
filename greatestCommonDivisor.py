# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_str = ""
        min_len = min(len(str1), len(str2))
        for i in range(0, min_len):
            if str2[i] == str1[i]:
                if max_str +str2[i] in str1[i+1:]:
                    if max_str != max_str + str2[i]:
                        max_str += str2[i]

        return max_str
        


obj = Solution()
print(obj.gcdOfStrings("ABCABC", "ABC")) 
print(obj.gcdOfStrings("ABABAB", "ABAB"))
print(obj.gcdOfStrings("LEET", "CODE"))
print(obj.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", 
                       "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))