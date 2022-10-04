class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10 ** 9 + 7
        maxm = pow(2, p, MOD) - 1
        x = maxm - 1
        mid = pow(2, p-1) - 1
        
        return (pow(x, mid, MOD)* maxm) % MOD
        
        
