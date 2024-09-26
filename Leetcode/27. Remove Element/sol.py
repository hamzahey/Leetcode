'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next position to place an element not equal to 'val'
        
        # Iterate through the array
        for i in range(len(nums)):
            # If current element is not equal to val
            if nums[i] != val:
                # Place the non-val element at index 'k'
                nums[k] = nums[i]
                k += 1  # Increment k for the next position
        
        # Return the number of elements that are not equal to val
        return k

# Example usage:
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
solution = Solution()
k = solution.removeElement(nums, val)

print(f"The number of elements not equal to {val}: {k}")
print(f"Modified array: {nums[:k]}")  # Only the first 'k' elements matter
