# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):

        dummy = ListNode(-1, head)

        prevGroup = dummy

        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth_node = getKth(prevGroup, k)
            if not kth_node:
                break
            nextGroup = kth_node.next

            prev, curr = nextGroup, prevGroup.next

            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevGroup.next
            prevGroup.next = kth_node
            prevGroup = temp

        return dummy.next


def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print("->".join(vals))

if __name__ == "__main__":
    # Create linked list: 1->2->3->4->5
    nodes = [ListNode(i) for i in range(1, 6)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    print("Original list:")
    print_list(head)

    k = 2
    s = Solution()
    new_head = s.reverseKGroup(head, k)

    print(f"List after reverseKGroup with k={k}:")
    print_list(new_head)