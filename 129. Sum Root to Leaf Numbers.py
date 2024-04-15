# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        tsum = 0
        
        def recur(root, seq):
            nonlocal tsum
            seq += str(root.val)
            if root.left != None:
                recur(root.left, seq)
            
            if root.right != None:
                recur(root.right, seq)
            
            if root.left == None and root.right == None:
                tsum += int(seq)
        
        recur(root, "")
        return tsum
        