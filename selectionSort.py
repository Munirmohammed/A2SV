#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        n = i
        for j in range(i, len(arr)):
            if arr[j] < arr[n]:
                n = j
        return n
    
    def selectionSort(self, arr,n):
        #code here
        for m in range(n):
            min = self.select(arr, m)
            arr[m], arr[min] = arr[min],arr[m]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
