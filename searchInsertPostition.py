# Search Insert Position

# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where 
# it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 
# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1
        # mid = 0
        # while left <= right:
        #     mid = (nums[left] + nums[right]) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        if target in nums:
            return nums.index(target)
        else:
            for i in range(0, len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] < target and nums[j] > target:
                        return j 
                    
        if target < nums[0]:
            return 0
        else:
            return len(nums)



                
        
obj = Solution()
print(obj.searchInsert([1,3,5,6], 24))