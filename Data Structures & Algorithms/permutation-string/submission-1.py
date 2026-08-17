class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1_c, window_c = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            s1_c[ord(s1[i]) - 97] += 1
            window_c[ord(s2[i]) - 97] += 1
            
        for i in range(len(s1), len(s2)):
            if s1_c == window_c: return True
            window_c[ord(s2[i]) - 97] += 1          
            window_c[ord(s2[i - len(s1)]) - 97] -= 1 
        return s1_c == window_c