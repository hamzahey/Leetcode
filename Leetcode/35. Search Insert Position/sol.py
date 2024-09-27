'''
35. Search Insert Position
Solved
Easy
Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if not nums:
            return 0
        
        def binarySearch(array, x, low, high):
            if high >= low:
                mid = low + (high - low) // 2
                if x == array[mid]:
                    return mid
                elif x > array[mid]:
                    return binarySearch(array, x, mid + 1, high)
                else:
                    return binarySearch(array, x, low, mid - 1)
            else:
                # Return the insertion point
                return low

        high = len(nums) - 1  # Changed from len(nums) to len(nums) - 1
        low = 0
        return binarySearch(nums, target, low, high)


# Create an instance of the Solution class
solution = Solution()


# Example 1: Target found
nums = [1, 3, 5, 6]
target = 5
print("Example 1:")
print("Input: nums =", nums, ", target =", target)
print("Output:", solution.searchInsert(nums, target))  # Output: 2


# Example 2: Target not found, insertion point
nums = [1, 3, 5, 6]
target = 2
print("\nExample 2:")
print("Input: nums =", nums, ", target =", target)
print("Output:", solution.searchInsert(nums, target))  # Output: 1


# Example 3: Target not found, insertion point at end
nums = [1, 3, 5, 6]
target = 7
print("\nExample 3:")
print("Input: nums =", nums, ", target =", target)
print("Output:", solution.searchInsert(nums, target))  # Output: 4


# Example 4: Empty array
nums = []
target = 5
print("\nExample 4:")
print("Input: nums =", nums, ", target =", target)
print("Output:", solution.searchInsert(nums, target))  # Output: 0


# Example 5: Single-element array
nums = [5]
target = 5
print("\nExample 5:")
print("Input: nums =", nums, ", target =", target)
print("Output:", solution.searchInsert(nums, target))  # Output: 0