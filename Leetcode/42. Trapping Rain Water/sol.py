'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = 0
        right_max = 0
        left = 0 
        right = len(height) -1
        trapped_water = 0
        
        while left < right:
            if height[left]<=height[right]:
                if height[left]>=left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                
                left +=1
            else:
                if height[right]>=right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -=1
            
        return trapped_water
    
myList = [0,1,0,2,1,0,1,3,2,1,2,1]

a = Solution()
print(a.trap(myList))