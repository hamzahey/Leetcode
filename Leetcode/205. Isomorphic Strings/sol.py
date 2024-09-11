'''
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
    
        dict_s_to_t = {}
        dict_t_to_s = {}

        for i, j in zip(s, t):
            if i in dict_s_to_t:
                if dict_s_to_t[i]!=j:
                    return False

            if j in dict_t_to_s:
                if dict_t_to_s[j]!=i:
                    return False
            
            dict_s_to_t[i]=j
            dict_t_to_s[j]=i

        return True
    
isomorphic = Solution()
print(isomorphic.isIsomorphic("egg", "add"))