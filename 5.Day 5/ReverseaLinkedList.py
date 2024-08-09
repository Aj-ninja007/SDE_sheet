

class ListNode:
  def__init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        temp=None
        while curr!=None:
          temp=curr.next
          curr.next=prev
          prev=curr
          curr=temp
        return prev
    
    
  
