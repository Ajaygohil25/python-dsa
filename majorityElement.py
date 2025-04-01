# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

class Solution:
    # not optimise
    # def majorityElement(self, nums: list[int]) -> int:
    #     dic1 = {}
    #     for i in nums:
    #         if i in dic1.keys():
    #             dic1[i] += 1
    #         else:
    #             dic1[i] = 1
        
    #     for i in dic1:
    #         if dic1[i] >  (len(nums)-1) // 2:
    #             return i
    

    # use of count function, not expected, not optimize
    # def majorityElement(self, nums: list[int]) -> int:
    #     for i in nums:
    #        if nums.count(i) > (len(nums)-1) // 2:
    #             return i

    # not optimal
    # def majorityElement(self, nums: list[int]) -> int:
    #     dic1 = {}
    #     for i in nums:
    #         if i in dic1.keys():
    #             dic1[i] += 1
    #             if dic1[i] > (len(nums)-1) // 2:
    #                 return i
    #         else:
    #             dic1[i] = 1
    #     return i
        
    def majorityElement(self, nums: list[int]) -> int:
        occurance = {}
        greater_key =  None
        greater_value = 0
        for i in nums:
            value = occurance.get(i, 0) + 1
            occurance[i] = value
            if value > greater_value:
                greater_value = value
                greater_key = i
        return greater_key




s_obj = Solution()

print(s_obj.majorityElement([3,2,3]))
print(s_obj.majorityElement([2,2,1,1,1,2,2]))