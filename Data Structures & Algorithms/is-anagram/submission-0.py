class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            for j in range(len(t)):
                if sorted(s) == sorted(t):
                    return True
        return False