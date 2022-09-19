class Solution(object):
    def kthLargestNumber(self, nums, k):
        arr = []
        for i in nums:
            arr.append(int(i))
        arr.sort(reverse=True)
        return str(arr[k-1])
    
