class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max = [-1]*len(nums1)
        sta = []
        for i in range(len(nums2)):
            if len(sta)==0 or sta[-1]>nums2[i]:
                sta.append(nums2[i])
            else:
                for j in range(len(sta)):
                    if sta[-1]<nums2[i]:
                        temp = sta.pop()
                        if temp in nums1:
                            max[nums1.index(temp)] = nums2[i] 
                sta.append(nums2[i])
                        

        return max
