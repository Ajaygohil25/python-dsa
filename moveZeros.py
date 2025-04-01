# 283. Move Zeroes
# Easy
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 
class Solution:
    # def moveZeroes(self, nums: list[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     length = len(nums)
    #     i = 0
    #     if length == 1:
    #         return nums
        
    #     for i in range(length):
    #         if nums[i] == 0:
    #             nums.pop(i)
    #             nums.append(0)

    #     print("nums",nums)
    # def moveZeroes(self, nums: list[int]) -> None: 
    #     temp = []
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             temp.append(nums[i])
    #     print("temp", temp)
    #     lenTemp = len(temp)
    #     for i in range(len(nums)):
    #         if lenTemp <=0:
    #             nums[i]= 0 
    #         else:
    #             nums[i] = temp[i]
    #             lenTemp -=1
    #     print(nums)
    def moveZeroes(self, nums: list[int]) -> None: 
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for j in range(i+1, len(nums)):
        #             if j > 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
                        # i += 1
        i = 0 
        for j in range(len(nums)):
            if nums[j] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1
        print("nums",nums)
                        

                
                
            





obj =  Solution()
obj.moveZeroes(nums=[0,1,0,3,12])

