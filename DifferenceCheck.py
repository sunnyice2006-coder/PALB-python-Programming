class Solution:
    def minDifference(self, arr):
        
       
        def toSeconds(t):
            h, m, s = map(int, t.split(":"))
            return h*3600 + m*60 + s
        
        secs = [toSeconds(t) for t in arr]
        secs.sort()
        
        ans = float("inf")
        
       
        for i in range(1, len(secs)):
            ans = min(ans, secs[i] - secs[i-1])
        
     
        day = 24 * 3600
        ans = min(ans, day - secs[-1] + secs[0])
        
        return ans
