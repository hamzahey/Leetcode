class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0
        end = len(numbers)-1
        currSum = 0

        while end>start:
            currSum = numbers[end] + numbers[start]
            if currSum>target:
                end -= 1
            elif currSum<target:
                start += 1
            else:
                return [start+1, end+1]
        
a = Solution()
print(a.twoSum([2,7,11,15],9))