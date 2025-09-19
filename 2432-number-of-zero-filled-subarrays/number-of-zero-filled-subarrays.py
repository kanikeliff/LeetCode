class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0    # total zero-filled subarrays
        count = 0  # current streak length of zeros

        for i in range(len(nums)):
            if nums[i] == 0:     # check the value at index i
                count += 1       # extend the zero streak
                res += count     # add all subarrays ending here
            else:
                count = 0        # reset streak when non-zero

        return res


            