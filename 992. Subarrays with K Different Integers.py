class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = j = count = 0
        contains = dict()
        while j < len(nums):
            if nums[j] not in contains:
                contains[nums[j]] = 1
            else:
                contains[nums[j]] += 1
            while(len(contains.keys()) > k):
                if contains[nums[i]] == 1:
                    contains.pop(nums[i], None)
                else:
                    contains[nums[i]] -= 1
                i += 1
            count += (j - i + 1)
            j += 1
        count2 = i = j = 0
        k -= 1
        contains.clear()
        while j < len(nums):
            if nums[j] not in contains:
                contains[nums[j]] = 1
            else:
                contains[nums[j]] += 1
            while(len(contains.keys()) > k):
                if contains[nums[i]] == 1:
                    contains.pop(nums[i], None)
                else:
                    contains[nums[i]] -= 1
                i += 1
            count2 += (j - i + 1)
            j += 1
        return count - count2

                