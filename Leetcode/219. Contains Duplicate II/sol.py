'''
219. Contains Duplicate II
Solved
Easy
Topics
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_hash = {}
        for i, num in enumerate(nums):
            if num in num_hash and abs(i-num_hash[num])<=k:
                return True

            num_hash[num] = i

        return False
            
nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))