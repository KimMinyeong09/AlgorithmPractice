class Solution:
    def countBits(self, n: int) -> List[int]:
        List = [i.bit_count() for i in range(0, n+1)]
        
        return List