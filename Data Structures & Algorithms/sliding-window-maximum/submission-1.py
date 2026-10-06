class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rmax = [0]*len(nums)
        lmax = [0]*len(nums)

        lmax[0] = nums[0]
        rmax[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            if i % k == 0:
                lmax[i] = nums[i]
            else:
                lmax[i] = max(lmax[i - 1], nums[i])   

            if ((len(nums) - 1 - i) + 1) % k == 0:
                rmax[len(nums) - 1 - i] = nums[len(nums) - 1 - i]
            else:
                rmax[len(nums) - 1 - i] = max(rmax[(len(nums) - 1 - i) + 1], nums[len(nums) - 1 - i])

        res = [0] * (len(nums) - k + 1)
        for i in range(len(nums) - k + 1):
            res[i] = max(lmax[i + k - 1], rmax[i])
        return res
                  