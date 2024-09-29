'''119. Pascal's Triangle II
Solved
Easy
Topics
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
'''

class Solution:
    def getRow(self, rowIndex: int):
        row = [1]  # Step 1: Initialize the row with the first element [1]
        
        for k in range(1, rowIndex + 1):
            # Step 2: Calculate the next element
            next_val = row[-1] * (rowIndex - k + 1) // k
            row.append(next_val)  # Step 3: Append the new value to the row
            
        return row  # Step 4: Return the completed row

sol = Solution()
print(sol.getRow(5))