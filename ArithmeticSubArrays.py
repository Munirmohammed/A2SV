class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        s = len(nums)
        
        def good(left, right):
            k = list(sorted(nums[left:right+1]))
            if len(k) == 1:
                return True
            dif = k[1] - k[0]
            for x,y in zip(k, k[1:]):
                if y-x != dif:
                    return False
            return True
        res=[]
        for left, right in zip(l,r):
            res += [good(left, right)]
        return res
