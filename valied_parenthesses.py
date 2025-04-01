# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

class Solution:
    # def isValid(self, s: str) -> bool:
    #     stackOfChar = []
    #     for i in s:
    #         if i == ')':
    #             if '(' in stackOfChar:
    #                 substring = s[s.index('(')+1: s.index(')')]
    #                 if self.isValid(substring):
    #                     stackOfChar.remove('(')
    #             else:
    #                 return False
    #         elif i == ']':
    #             if '[' in stackOfChar:
    #                 substring = s[s.index('[')+1: s.index(']')]
    #                 if self.isValid(substring):
    #                     stackOfChar.remove('[')
    #             else:
    #                 return False
    #         elif i == '}':
    #             if '{' in stackOfChar:
    #                 substring = s[s.index('{')+1: s.index('}')]
    #                 if self.isValid(substring):
    #                     stackOfChar.remove('{')
    #             else:
    #                 return False
    #         else: 
    #             stackOfChar.append(i)
    #     if len(stackOfChar) > 0:
    #         return False
    #     return True
    def isValid(self, s: str) -> bool:
        stack = []
        mapofPar = {")" : "(", "]":'[', "}":"{"}
        for char in s:
            if char in mapofPar.values():
                stack.append(char)
            elif char in mapofPar.keys():
                if not stack or mapofPar[char] != stack.pop():
                    return False
        return True


obj = Solution()
print(obj.isValid("({[])"))
print(obj.isValid("(([]){})"))
