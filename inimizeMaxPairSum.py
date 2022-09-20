class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maxp=0
        i=0
        j=len(nums)-1
        
        while i<j:
            maxp = max(maxp, nums[i]+nums[j])
            i+=1
            j-=1
        return maxp
