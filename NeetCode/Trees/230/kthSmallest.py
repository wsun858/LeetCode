# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            k -= 1
            curr = stack.pop()
            if k == 0:
                return curr.val
            
            curr = curr.right