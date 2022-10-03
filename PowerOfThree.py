class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        i = 0
        while (n != 1):
            if n % 3 != 0:
                return False
            n = n/3
            print(n)
        return True
        
