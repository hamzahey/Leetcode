'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            start = i + 1
            end = len(nums)-1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum == target:
                    s.add((nums[i],nums[start],nums[end]))
                    start +=1
                    end -=1
                elif sum>target:
                    end -=1
                else:
                    start +=1
        output = list(s)
        return output
            
nums =[-4, -1, -1, 0, 1, 2]
a = Solution()
print(a.threeSum(nums))

            

        