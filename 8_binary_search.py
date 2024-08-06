#Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.

#1. Binary search

class Solution:
    def search(self, nums, target) -> int:
        low = nums[0]
        high = nums [-1]
        if high >= low:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                return Solution.search(nums, low, mid - 1, target)
            
            else:
                return Solution.search(nums, mid + 1, high, target)
        else:
            return -1
        