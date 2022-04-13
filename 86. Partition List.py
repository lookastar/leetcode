from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def printList(self):
        currentNode = self
        i=0
        while currentNode != None and i<10:
            print(currentNode.val)
            currentNode = currentNode.next
            i+=1
        print()

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        currentNode, lowerCurrentNode, upperHead, upperCurrentNode = head, None, None, None
        head = None # it is the lowerHead

        if currentNode == None:
            return None

        if currentNode.val < x:
            head, lowerCurrentNode = currentNode, currentNode
        else:
            upperHead, upperCurrentNode = currentNode, currentNode

        while currentNode.next != None:
            if currentNode.next.val < x:
                if head == None:
                    head, lowerCurrentNode = currentNode.next, currentNode.next
                else:
                    lowerCurrentNode = lowerCurrentNode.next
                currentNode = currentNode.next

            else: # currentNode.next.val >= x:
                if upperHead == None:
                    upperHead, upperCurrentNode = currentNode.next, currentNode.next
                else:
                    upperCurrentNode.next = currentNode.next # necessary?
                    upperCurrentNode = upperCurrentNode.next
                if currentNode.val < x:
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next

        if head != None:
            lowerCurrentNode.next = upperHead
            if upperCurrentNode != None: upperCurrentNode.next = None
        else:
            head = upperHead

        return head


# def main():
#     sol = Solution()
#     a,b,c,d,e = ListNode(4), ListNode(3), ListNode(2), ListNode(5), ListNode(2)
#     a.next = b
#     b.next = c
#     c.next = d
#     d.next = e

#     a.printList()

#     sol.partition(a, 3)

#     a.printList()

# if __name__ == "__main__":
#     main()

