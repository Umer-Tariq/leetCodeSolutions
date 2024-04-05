class Solution(object):
    def makeGood(self, s):
        i = 0
        while i < len(s) - 1:
            if s[i].islower():
                if s[i].upper() == s[i + 1]:
                    s = s[:i] + s[i + 2:]
                    i = 0
                else:
                    i += 1
            elif s[i].isupper():
                if s[i].lower() == s[i + 1]:
                    s = s[:i] + s[i + 2:]
                    i = 0
                else:
                    i += 1
            else:
                i += 1
        return s
        