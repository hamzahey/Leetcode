'''76. Minimum Window Substring
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""

        map = [0]*128
        start = 0
        end = 0
        startIndex = 0
        count = len(t)
        min_len = float('inf')

        for char in t:
            map[ord(char)]+=1

        while end < len(s):
            if map[ord(s[end])]>0:
                count -= 1
            map[ord(s[end])] -=1
            end +=1

            while count == 0:
                if end - start < min_len:
                    min_len = end - start
                    startIndex = start
                if map[ord(s[start])]==0:
                    count +=1
                map[ord(s[start])]+=1
                start+=1
        
        return "" if min_len == float('inf') else s[startIndex:startIndex + min_len]
        
# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
result = solution.minWindow(s, t)
print(result)  # Expected output: "BANC"