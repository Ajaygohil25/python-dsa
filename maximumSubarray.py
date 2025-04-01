# Maximum Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution:
    # broot force approach
    # def maxSubArray(self, nums: list[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     max_sum = 0
    #     total_i = 0
    #     for i in range(len(nums)): 
    #         for j in range(i,len(nums)):
    #             total_i += nums[j] 
    #             # print("nums[j]", nums[j], "total", total_i)
    #             if total_i > max_sum:
    #                 max_sum = total_i
    #                 # print("max-sun",max_sum)
    #         total_i =0 
    #     return max_sum
    
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf') 
        total = 0 
        for i in range(len(nums)):
            total += nums[i]
            max_sum = max(max_sum, total)
            if total < 0:
                total = 0
        return max_sum
        


obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.maxSubArray([1]))
print(obj.maxSubArray([5,4,-1,7,8]))