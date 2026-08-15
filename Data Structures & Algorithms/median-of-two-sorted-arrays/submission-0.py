class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums = nums1 + nums2
        nums.sort()

        total = len(nums)

        if total % 2 == 0:
            return (nums[total // 2 - 1] + nums[total // 2]) / 2.0
        else:
            return nums[total // 2]
                