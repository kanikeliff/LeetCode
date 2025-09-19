class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        left = 0  # start of the zero window

        while left < n:
            if nums[left] == 0:
                # expand the window
                right = left
                while right < n and nums[right] == 0:
                    right += 1
                length = right - left
                # number of zero-filled subarrays in this window
                res += length * (length + 1) // 2
                # move window start past this block
                left = right
            else:
                left += 1

        return res
