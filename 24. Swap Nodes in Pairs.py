# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currentNode, prev, newHead  = head, None, None
        if head != None: newHead = head.next
        
        while currentNode != None and currentNode.next != None:
            followingNode=currentNode.next # increment
            if prev != None: prev.next = followingNode
            currentNode.next = followingNode.next

            followingNode.next = currentNode
            prev = currentNode # increment
            currentNode = currentNode.next # increment
            
        return newHead or head
