class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = j = 0
        len_list = []
        d = dict()
        while(j < len(nums)):
            if nums[j] not in d:
                d[nums[j]] = 1
                len_list.append(j - i + 1)
            else:
                while d[nums[j]] + 1 > k:
                    d[nums[i]] -= 1
                    i += 1
                d[nums[j]] += 1
                len_list.append(j - i + 1)
            j+=1
        ans = max(len_list)
        return ans