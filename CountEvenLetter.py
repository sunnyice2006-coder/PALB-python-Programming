class Solution:
    def count(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        ans = 0
        for ch in freq:
            if freq[ch] % 2 == 0:
                ans += 1
        
        return ans
