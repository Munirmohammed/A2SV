class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        Is = ""
        if n == 1:
            return "0"
        for i in range(n-1):
            for j in s:
                if j == '0':
                    Is += '1'
                else:
                    Is += '0'
            s = s + "1" + Is[::-1]
            Is = ""
        return (str(s[k-1]))
