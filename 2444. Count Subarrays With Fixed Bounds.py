class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        minIndex = maxIndex = painIndex = -1
        count = 0
        for i in range(len(nums)):
          if nums[i] == minK:
            minIndex = i
          if nums[i] == maxK:
            maxIndex = i
          if nums[i] < minK or nums[i] > maxK:
            painIndex = i
          smaller = min(minIndex, maxIndex)
          ans = smaller - painIndex
          if ans > 0:
            count += ans
        return count
