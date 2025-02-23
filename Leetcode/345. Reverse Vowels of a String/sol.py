'''
345. Reverse Vowels of a String
Solved
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 '''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u','A','E', 'I','O','U']
        s = list(s)
        start = 0 
        end = len(s)-1

        while start<end:
            while start<end and s[start] not in vowels:
                start+=1
            while start<end and s[end] not in vowels:
                end-=1
            s[start], s[end] = s[end], s[start]
            start +=1
            end -=1
        
        return "".join(s)



s = "IceCreAm"
print(Solution().reverseVowels(s)) 