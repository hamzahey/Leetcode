class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        count_hash = {}

        for i in range(len(s)):
            count_hash[s[i]] = count_hash.get(s[i], 0) + 1
            count_hash[t[i]] = count_hash.get(t[i], 0) - 1

        for val in count_hash.values():
            if val !=0:
                return False
        
        return True


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s,t))