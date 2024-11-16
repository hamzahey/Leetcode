'''
350. Intersection of Two Arrays II
Solved
Easy
Topics
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 '''

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        result = []

        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1

        return result        

print(Solution().intersect([1,2,2,1], [2,2]))