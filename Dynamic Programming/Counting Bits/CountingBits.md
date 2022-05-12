![screencapture-leetcode-problems-counting-bits-2022-05-12-23_54_03](https://user-images.githubusercontent.com/70676475/168104827-085ce822-9c04-446d-bed1-c6cbebbf3c17.png)

### 문제 주소
[Counting Bits](https://leetcode.com/problems/counting-bits/)

### 초기 코드
``` python
class Solution:
    def countBits(self, n: int) -> List[int]:
        List = [ 0 for _ in range(n+1)]
        
        for i in range(1, n+1):
            List[i] = i.bit_count()
            
        return List
```
**Runtime이 112ms정도가 걸림**

### 수정 코드
``` python
class Solution:
    def countBits(self, n: int) -> List[int]:
        List = [i.bit_count() for i in range(0, n+1)]
        
        return List
```
for 반복문 안에서 `.bit_count`를 돌리지 않고  
밖으로 빼내서 처음부터 `List` 안에 저장

### 접근 방법
0부터 n까지의 숫자들의 이진수에서 1의 개수를 구하는 것이기 때문에  
숫자가 커질수록 이전 데이터가 누적됨  
`bit_count`라는 함수를 사용하여 `i`의 이진수에서 1의 개수를 `List`에 저장

### 시간복잡도
O(n)
