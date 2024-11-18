'''
414. Third Maximum Number
Solved
Easy
Topics
Companies
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''

class Solution:
    def thirdMax(self, nums):
        first = second = third = float('-inf')

        for num in nums:
            if num==first or num==second or num==third:
                continue
            
            if num>first:
                first, second, third = num, first, second
            elif num>second:
                second , third = num, second
            elif num>third:
                third = num

        return third if third!=float('-inf') else first

print(Solution().thirdMax([2,2,3,1]))