class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered=sorted(zip(position,speed),reverse=True)
        time=[]
        for pos,sped in ordered:
            res=(target-pos)/sped
            if time and res<=time[-1]:
                continue
            time.append(res)
        return len(time)
        