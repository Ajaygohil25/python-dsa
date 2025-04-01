# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21



class Solution:
    # not working for reverse number 
    # def reverse(self, x: int) -> int:
    #     reverse_num = 0
    #     while x != 0:
    #         reminder =  x % 10
    #         if reverse_num > 2**31 // 10 or (reverse_num == 2**31 // 10 and reminder > 7):
    #             return 0
    #         if reverse_num < -2**31 // 10 or (reverse_num == -2**31 // 10 and reminder < -8):
    #             return 0
    #         x //= 10
    #         reverse_num = reverse_num * 10 + reminder
    #     return reverse_num
    
    def reverse(self, x: int) -> int:
        reverse_num = ""
        x  = str(x)
        if x[0] == '-':
            reverse_num = int(x[1:][::-1] ) * -1 
        else:
            reverse_num = int(x[::-1])
        if reverse_num > 2** 31 - 1 or reverse_num < -2**31:
            return 0
        return int(reverse_num)
        
    
solution_obj =  Solution()
print(solution_obj.reverse(123))
print(solution_obj.reverse(120))
print(solution_obj.reverse(-123))


