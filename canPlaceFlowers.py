#  Can Place Flowers
# Easy
# Topics
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:

                if i == length - 1:
                    if flowerbed[i-1] == 0 and i >= 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i > 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i+1] == 0 and i <= length:
                        flowerbed[i] = 1
                        n -= 1
        return n <=0

obj = Solution()
# Test case 1
flowerbed = [1, 0, 0, 0, 1]
n = 1
print("Test case 1",obj.canPlaceFlowers(flowerbed, n))  # Expected output: True
# Test case 2      
flowerbed = [1, 0, 0, 0, 1]
n = 2
print("Test case 2",obj.canPlaceFlowers(flowerbed, n))  # Expected output: False
# Test case 3
flowerbed = [0, 0, 0, 0, 0]
n = 3
print("Test case 3",obj.canPlaceFlowers(flowerbed, n))  # Expected output: True
# Test case 4
flowerbed = [1, 0, 0, 0, 0, 1]
n = 2
print("Test case 4",obj.canPlaceFlowers(flowerbed, 2))  # Expected output: False