![screencapture-leetcode-problems-maximum-subarray-2022-05-09-11_26_18](https://user-images.githubusercontent.com/70676475/167330410-ae7d5639-cea0-4968-b015-4b5527b450c9.png)

### 문제 주소
[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

### 초기 코드
``` python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = []
        sub_sum.append(nums[0])
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            sub_sum.append(max(nums[i], sub_sum[i-1]+nums[i]))
            if max_sum < sub_sum[i]:
                max_sum = sub_sum[i]
        return max_sum
```
**Runtime이 1000ms가 넘어감**

### 수정 코드
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = [0 for i in range(len(nums))]
        sub_sum[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            sub_sum[i] = max(nums[i], sub_sum[i-1]+nums[i])
            if max_sum < sub_sum[i]:
                max_sum = sub_sum[i]
        return max_sum
```

### 접근 방법
빈 list(`sub_sum`)을 생성하고 `nums[i]`와 `sub_sum[i-1]+nums[i]` 중 더 큰 값을 `sub_sum`에 저장 
`sub_sum[i-1]+nums[i]`가 크면 계속해서 누적되어서 값이 저장되지만  
`nums[i]`이 커지는 순간 이전에 누적된 값이 `nums[i]`로 변경되면서 다시 값을 비교하면서 저장  
**흐름은 동일하지만 list comprehension(sub_sum = [0 for i in range(len(nums))])을 사용해서 Runtime을 줄임**

### 시간복잡도
O(n)
