![screencapture-leetcode-problems-climbing-stairs-2022-05-10-18_52_42](https://user-images.githubusercontent.com/70676475/167601932-aa7c40fc-adae-4dad-90ea-95cca0c649ec.png)

### 문제 주소
[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

### 초기 코드
``` python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a = 1
        b = 2
        for i in range(3, n+1):
            temp = a
            a = b
            b = temp + b
        return b
```
**Runtime이 40ms정도가 걸림**

### 수정 코드
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a = 1
        b = 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b
```

### 접근 방법
1칸을 먼저 올라가면 n-1칸의 계단이 남고, 2칸을 먼저 올라가면 n-2칸이 남음  
f(n)을 n칸을 올라가는 방법의 수라고 한다면,  
`f(n) = f(n-1) + f(n-2)` 라는 식을 세울 수 있음.
**흐름은 동일하지만 다중 선언을 통해 32 ms정도가 걸림**

### 시간복잡도
O(n)
