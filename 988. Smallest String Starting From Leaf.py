# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        d = {
                0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
                10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
                20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
        }
        global global_min
        global_min = ''

        def recur(root, curr_value):
            global global_min
            curr_value = d[root.val] + curr_value
            if root.left == None and root.right == None:
                if len(global_min) == 0:
                    global_min = curr_value
                if curr_value < global_min:
                    global_min = curr_value
            if root.left:
                recur(root.left, curr_value)
            if root.right:
                recur(root.right, curr_value)


        
        recur(root, "")
        return global_min
        