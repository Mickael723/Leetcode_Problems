"""
# Definition for a QuadTree node.

"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid) -> Node:

        def dfs(n, row, column):

            isLeaf = True
            for i in range(n):
                for j in range(n):
                    if grid[row][column] != grid[row + i][column + j]:
                        isLeaf = False
                        break
            
            if isLeaf:
                return Node(grid[row][column], isLeaf, None, None, None, None)
            
            n = n // 2
            topleft = dfs(n, row, column)
            topright = dfs(n, row, column + n)
            bottomleft = dfs(n, row + n, column)
            bottomright = dfs(n, row + n, column + n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)
        return dfs(len(grid), 0, 0)

def print_quad_tree(node, indent=0):
    if not node:
        return
    prefix = " " * indent
    print(f"{prefix}Node(val={node.val}, isLeaf={node.isLeaf})")
    if not node.isLeaf:
        print(f"{prefix} topLeft:")
        print_quad_tree(node.topLeft, indent + 2)
        print(f"{prefix} topRight:")
        print_quad_tree(node.topRight, indent + 2)
        print(f"{prefix} bottomLeft:")
        print_quad_tree(node.bottomLeft, indent + 2)
        print(f"{prefix} bottomRight:")
        print_quad_tree(node.bottomRight, indent + 2)

if __name__ == "__main__":
    # Example grid
    grid = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    s = Solution()
    quad_tree_root = s.construct(grid)
    print_quad_tree(quad_tree_root)