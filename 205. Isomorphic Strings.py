class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False
        i = j = 0
        d_s = dict()
        d_t = dict()
        while i < len(s) and j < len(t):
            if s[i] not in d_s:
                if t[j] not in d_t:
                    d_s[s[i]] = t[j]
                    d_t[t[j]] = s[i]
                else:
                    return False
            else:
                if d_s[s[i]] != t[j]:
                    return False
            i += 1
            j += 1
        return True
        