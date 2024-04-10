class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        skip = False
        deck.sort()
        result = []
        for x in range(len(deck)):
            result.append(0)
        j = 0
        i = 0
        n = len(deck)
        while i < n:
            if result[j] == 0:
                if skip == False:
                    result[j] = deck[i]
                    i += 1
                    skip = True
                else:
                  skip = False
                j = (j + 1)%n
            else:
                j = (j + 1)%n
        return result
