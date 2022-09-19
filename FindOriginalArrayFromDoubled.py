class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        length = len(changed)//2
        i = 0
        j = 1
        while len(changed) > length:
            if j>=len(changed):
                return []
            elif changed[i]*2 == changed[j] and i != j:
                changed.pop(j)
                i+=1
            else:
                j+=1
        if len(changed) == length:
            return changed
        else:
            return []
