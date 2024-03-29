class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = max(nums)
        count = count_max = 0
        n = len(nums)
        i = j = 0
        while j < n:
            if nums[j] == maxi:
                count_max += 1
            while count_max >= k:
                count += (n-j)
                if nums[i] == maxi:
                    count_max -= 1
                i += 1
            j += 1
        return count
        