# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:

        queue = []
        queue.append((root, float('-inf'), float('inf')))

        while queue:
            curr_node, min_val, max_val = queue.pop(-1)
            if not curr_node:
                continue
            
            if curr_node.val < min_val or curr_node.val > max_val:
                return False
            #Check left and right nodes
            if curr_node.left:
                queue.append((curr_node.left, min_val, curr_node.val))
            if curr_node.right:
                queue.append((curr_node.right, curr_node.val, max_val))
            
        return True
            
