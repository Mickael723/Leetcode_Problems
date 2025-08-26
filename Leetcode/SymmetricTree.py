# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root) -> bool:

    queue = []
    child_layer = []
    queue.append(root)

    while queue:
        curr_node = queue.pop(-1)
        if curr_node.left:
            child_layer.append(curr_node.left)
        else:
            child_layer.append(TreeNode(-101,None,None))
        if curr_node.right:
            child_layer.append(curr_node.right)
        else:
            child_layer.append(TreeNode(-101,None,None))

        if not queue:
            left_check = 0
            right_check = len(child_layer) - 1

            while left_check <= right_check:
                
                if child_layer[left_check].val != child_layer[right_check].val:
                    return False
                left_check += 1
                right_check -= 1
                
            for node in child_layer:
                if node.val != -1:
                    queue.append(node)
            child_layer.clear()

    return True

def build_tree():
    # Symmetric tree:      1
    #                    /   \
    #                   2     2
    #                  / \   / \
    #                 3  4  4  3
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))
    return root

def build_asymmetric_tree():
    # Asymmetric tree:     1
    #                    /   \
    #                   2     2
    #                    \     \
    #                     3     3
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(3))
    root.right = TreeNode(2, None, TreeNode(3))
    return root

if __name__ == "__main__":
    print("Symmetric tree test:", isSymmetric(build_tree()))         # Expected: True
    print("Asymmetric tree test:", isSymmetric(build_asymmetric_tree())) # Expected: False
