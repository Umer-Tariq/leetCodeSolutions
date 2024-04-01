class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = j = count = max = 0
        unordered_set = set()
        while j < len(s):
            if s[j] not in unordered_set:
                unordered_set.add(s[j])
            else:
                while s[j] in unordered_set:
                    unordered_set.discard(s[i])
                    i += 1
                unordered_set.add(s[j])
            count = j - i + 1
            if count > max:
                max = count
            j+=1
        return max

        