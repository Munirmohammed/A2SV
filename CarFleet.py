class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        
        for i in range(len(position)):
            time.append((position[i], speed[i]))
        time.sort(key=lambda x: x[0])

        for idx, distSpeed in enumerate(time):
            time[idx] = float(target - distSpeed[0]) / distSpeed[1]

        fleetCount = 0
        fleetLeaderTime = 0
       
        for i in range(len(time) - 1, -1, -1):
            curr = time[i]
            if curr > fleetLeaderTime:
                fleetCount += 1
                fleetLeaderTime = curr
        
        return fleetCount
