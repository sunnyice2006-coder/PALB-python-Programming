class Solution(object):
    def searchRange(self, nums, target):

        def firstPos(nums, target):
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def lastPos(nums, target):
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [firstPos(nums, target), lastPos(nums, target)]
