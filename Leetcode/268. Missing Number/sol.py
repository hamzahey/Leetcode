'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_len = len(nums) + 1
        ans = 0
        for i in range(num_len):
            ans ^= i
        
        for i in nums:
            ans^=i

        return ans
    
nums = [9,6,4,2,3,5,7,0,1]
sol = Solution()
print(sol.missingNumber(nums))