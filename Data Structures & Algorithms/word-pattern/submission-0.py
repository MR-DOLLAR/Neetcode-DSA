class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        li = list(s.split())
        if len(pattern) != len(li):
            return False
        if len(set(pattern)) != len(set(li)):
            return False
        
        freq = {}
        for p, w in zip(pattern, li):
            if p in freq:
                if freq[p] != w:
                    return False
            else:
                freq[p] = w
        return True