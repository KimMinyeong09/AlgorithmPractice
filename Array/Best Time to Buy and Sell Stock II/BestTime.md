![screencapture-leetcode-explore-interview-card-top-interview-questions-easy-92-array-564-2022-05-06-22_03_43](https://user-images.githubusercontent.com/70676475/167137119-0eb36847-43f0-4d93-b3f6-e08a9c99c243.png)

### 문제 주소
[Best Time to Buy and Sell Stock II](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/)

### 접근 방법
Greedy Algorithm: 구입하고 바로 다시 팔기 가능하니까  
다음 날의 가격이 지금보다 오르면(`prices[i+1]`-`prices[i]` >= 0) 즉시 팔아서 이익 얻기

### 시간복잡도
O(n)
