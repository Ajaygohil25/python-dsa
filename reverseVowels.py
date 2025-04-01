#  Reverse Vowels of a String
# Easy
# Topics
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        print("Length of the string:", length)
        if length == 1:
            return s
        vowels = set("aeiouAEIOU")
        i = 0
        j = length - 1
        s = list(s)
        while i < j:
            if s[i] not in vowels:
                i += 1
            
            if s[j] not in vowels:
                j -= 1
            
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
                
        s = ''.join(s)
        return s    

# Test cases
obj = Solution()

# Test case 1
s1 = "IceCreAm"
expected_output1 = "AceCreIm"
output = obj.reverseVowels(s1)
print(f"Test case 1: {output == expected_output1}, Output: {output}, Expected: {expected_output1}")


# Test case 2
s2 = "leetcode"
expected_output2 = "leotcede"
output = obj.reverseVowels(s2)
print(f"Test case 2: {output == expected_output2}, Output: {output}, Expected: {expected_output2}")

# Test case 3
s3 = "hello"
expected_output3 = "holle"
output = obj.reverseVowels(s3)
print(f"Test case 3: {output == expected_output3}, Output: {output}, Expected: {expected_output3}")

# Test case 4
s4 = "aA"
expected_output4 = "Aa"
output = obj.reverseVowels(s4)
print(f"Test case 4: {output == expected_output4}, Output: {output}, Expected: {expected_output4}")

# Test case 5
s5 = " "
expected_output5 = " "
output = obj.reverseVowels(s5)
print(f"Test case 5: {output == expected_output5}, Output: {output}, Expected: {expected_output5}")

# Test case 6
s6 = "race a car"
expected_output6 = "raca e car"
output = obj.reverseVowels(s6)
print(f"Test case 6: {output == expected_output6}, Output: {output}, Expected: {expected_output6}")
