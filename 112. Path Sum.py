# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def recur(root, num, targetSum):
            if not root:
                return False
            num = num + root.val
            if root.left == None and root.right == None:
                if num == targetSum:
                    return True
                else:
                    return False
            return recur(root.left, num, targetSum) or recur(root.right, num, targetSum)
        ans = recur(root, 0, targetSum)
        return ans
            
        
        