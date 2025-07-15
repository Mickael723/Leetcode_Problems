#Setup a BST for range max query
class Node:
    def __init__(self, key, value, aug_val):
        self.key = key
        self.value = value
        self.aug_val = aug_val
        self.left = None
        self.right = None

#Updates aug_val to the sum of node's descendants
def recalculate_aug(node: Node):
    if node is None:
        return 0
    if node.left is None:
        left_aug = 0
    else: left_aug = node.left.aug_val
    
    if node.right is None:
        right_aug = 0
    else: right_aug = node.right.aug_val

    node.aug_val = max(node.value, left_aug, right_aug)
    return node.aug_val

def insert_node(root: Node, key: int, value: int):
    if root is None:
        return Node(key, value, value)
    if root.key == key:
        root.value = max(root.value, value)
    if root.key < key:  
        root.right = insert_node(root.right, key, value)
    else:
        root.left = insert_node(root.left, key, value)
    recalculate_aug(root)
    return root

#Range max query to BST to get the max augments
def range_max(root: Node, k: int):

    if root is None: return 0

    if k < root.key:
        return range_max(root.left, k)
    else:
        if root.left is None:
            left_aug = 0
        else:
            left_aug = root.left.aug_val
        ans = max(left_aug, root.value)
        if k > root.key:
            ans = max(ans, range_max(root.right, k))
        return ans

if __name__== "__main__":

    n = int(input())
    sequence = list(map(int, input().split()))
    
    #Initialize BST
    root = None

    max_lis_sum = 0
    for key in sequence:
        #Query BST to get LIS for previous elements and insert into BST
        prev_max = range_max(root, key - 1)
        curr_lis_sum = prev_max + key
        root = insert_node(root, key, curr_lis_sum)
        #Update max sum
        max_lis_sum = max(max_lis_sum,curr_lis_sum)

    print(max_lis_sum)