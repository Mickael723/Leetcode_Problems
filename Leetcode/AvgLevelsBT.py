# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root) -> list:

        current_layer = []
        children = []
        layer_vals = []
        averages = []

        current_layer.append(root)

        while current_layer:
            popped_node = current_layer.pop(-1)
            layer_vals.append(popped_node.val)

            if popped_node.left != None:
                children.append(popped_node.left)
            if popped_node.right != None:
                children.append(popped_node.right)

            if not current_layer:
                averages.append(sum(layer_vals) / len(layer_vals))
                layer_vals.clear()
                for child in children:
                    current_layer.append(child)
                children.clear()

