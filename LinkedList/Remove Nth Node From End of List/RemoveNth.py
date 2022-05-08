# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        values = []
        while temp is not None:
            values.append(temp.val)
            temp = temp.next
            
        # 지우려는 것 앞의 노드로 이동
        delete_prev = len(values) - n - 1 
        
        temp = head
        counter = 0
        
        # 지우려는 것이 Head인 경우
        if delete_prev < 0:
            head = temp.next
            return head
        # Head가 아닌 경우
        while temp is not None:
            if counter == delete_prev:
                temp.next = temp.next.next
                return head
            counter += 1
            temp = temp.next        
        