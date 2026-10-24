class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq={}
        if len(s)!=len(t):
            return False

        for i in s:
            freq[i]=freq.get(i,0)+1
        
        for c in t:
            if c not in freq:
                return False
            
            freq[c]-=1

            if freq[c]<0:
                return False
        return True
        