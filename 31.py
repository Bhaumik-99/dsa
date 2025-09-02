class Solution(object):
    def nextPermutation(self, nums):
        # Find first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # If found, swap with next greater element from the end
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse the elements after i
        nums[i + 1:] = reversed(nums[i + 1:])
