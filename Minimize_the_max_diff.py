class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()

        ans = arr[n - 1] - arr[0]

        small = arr[0] + k
        large = arr[n - 1] - k

        if small > large:
            small, large = large, small

        for i in range(1, n - 1):
            subtract = arr[i] - k
            add = arr[i] + k

            if subtract < 0:
                continue

            new_min = min(small, subtract)
            new_max = max(large, add)

            ans = min(ans, new_max - new_min)

        return ans
