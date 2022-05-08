![screencapture-leetcode-explore-interview-card-top-interview-questions-easy-93-linked-list-603-2022-05-08-23_06_28](https://user-images.githubusercontent.com/70676475/167300084-7f503945-54e7-4179-bce2-14b86db0e256.png)

### 문제 주소
[Remove Nth Node From End of List](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/)

### 접근 방법
빈 list(`values`)에 노드 값 전부 담아두고 지우려는 노드의 바로 이전 노드로 이동(`delete_prev`)  
Case1: 지우려는 것이 Head인 경우 -> head를 next로 바꿔줌
Case2: 지우려는 것이 Head가 아닌 경우 -> `delete_prev`에 위치한 노드의 next를 하나 건너뛰고 연결(temp.next = temp.next.next)

### 시간복잡도
O(n)