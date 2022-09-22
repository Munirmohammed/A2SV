class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                A[start],A[end] = A[end],A[start]
                start+=1
                end-=1
        N = len(A)
        output = []
        for i in range(N-1,-1,-1):
            maximum = i
            for j in range (i,-1,-1):
                if A[j] > A[maximum]:
                    maximum = j
            if maximum != i:
                flip(maximum)
                flip(i)
                output.append(maximum+1)
                output.append(i+1)
        return output
    
    
            
