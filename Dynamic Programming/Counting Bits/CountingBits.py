class Solution:
    def countBits(self, n: int) -> List[int]:
        List = [ 0 for _ in range(n+1)]
        
        for i in range(1, n+1):
            List[i] = i.bit_count()
            
        return List