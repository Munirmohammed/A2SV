class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()
        for i,v in enumerate(citations):
            if N-i <= v:
                return N-i
        return 0
