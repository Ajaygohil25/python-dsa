#  Rotate Array
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# # rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,,-100]

class Solution:

    # def rotate(self, nums: list[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     for i in range(k):
    #         self.self_rotate(nums)

    # def self_rotate(self,nums):
    #     lenght = len(nums) - 1
    #     last = nums[-1]
    #     while(lenght > 0):
    #         nums[lenght] = nums[lenght-1]
    #         lenght -= 1
    #     nums[0] = last

    # optimize approach

    # [1,2,3,4,5,6,7], k = 3 # length = 7-3 = 4

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        self.reverse_nums(nums, 0, length - k - 1) 
        self.reverse_nums(nums, length-k ,length-1)
        self.reverse_nums(nums, 0, length-1)

    def reverse_nums(self,nums, left, right):
        while(left<right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # print("nums rn", nums)



    



obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7],k=3))
print(obj.rotate([-1,-100,3,99],k=2))