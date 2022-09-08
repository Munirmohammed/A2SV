class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j],nums[i]
        
        for m in range(len(nums)):
            if nums[m]==target:
                arr.append(m)
        return arr
