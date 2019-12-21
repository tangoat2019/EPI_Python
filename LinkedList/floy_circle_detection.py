class Node():
    def __init__(self, val):
        self.next = None
        self.val = val
def floyd_circle_detection(root):
    if not root.next:
        return False
    else:
        slow_cnt, fast_cnt = root, root
        while slow_cnt and fast_cnt and fast_cnt.next and slow_cnt.next and fast_cnt.next.next:
            slow_cnt = slow_cnt.next
            fast_cnt = fast_cnt.next.next
            if slow_cnt == fast_cnt:
                return True
        return False
        
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
floyd_circle_detection(root)
print(floyd_circle_detection(root))