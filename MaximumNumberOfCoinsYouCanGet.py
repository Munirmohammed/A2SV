class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        sum = 0
        i = count = 1      
        while i < len(piles) and count < len(piles):
            sum += piles[i]
            i += 2
            count += 3
        return sum
