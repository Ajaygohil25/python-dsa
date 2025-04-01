# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic1 = {}
        for i in nums:
            value = dic1.get(i, 0) + 1
            dic1[i] = value
            if value > 1:
                return True
        return False
solation_obj = Solution()

print(solation_obj.containsDuplicate(nums = [1,2,3,1]))
print(solation_obj.containsDuplicate(nums = [1,2,3,4]))
print(solation_obj.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
