# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans_list = []
        if root != None:
            ans_list.append(root.val)
        else:
            return ans_list
        if root.left != None:
            ans_list.extend(self.preorderTraversal(root.left))
        if root.right != None:
            ans_list.extend(self.preorderTraversal(root.right))
        return ans_list
        