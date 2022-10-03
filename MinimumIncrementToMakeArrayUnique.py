class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        print(nums)
        ans = 0
        for i in range(1,N):
            if nums[i-1] >= nums[i]:
                print(nums[i-1],nums[i])
                ans += (nums[i-1] - nums[i]) + 1
                nums[i] = nums[i-1] + 1
        return ans
        
