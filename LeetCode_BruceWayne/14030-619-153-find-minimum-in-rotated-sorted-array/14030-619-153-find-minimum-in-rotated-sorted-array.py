class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            else:
                mid = (l + r) // 2
                res = min(res, nums[mid])

                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        return res
        