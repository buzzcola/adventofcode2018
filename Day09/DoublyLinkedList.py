class DoublyLinkedList:
    def __init__(self, items):
        first = ListNode(items.pop(0))
        self.head = first
        self.tail = first
        for item in items:
            self.append(item)
    
    def append(self, item):
        node = ListNode(item)
        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        return node

    def insertAfter(self, node, item):           
        if node == self.tail:
            return self.append(item)
        
        new = ListNode(item)
        new.next = node.next
        new.previous = node
        node.next.previous = new
        node.next = new
        return new

    def remove(self, *nodes):
        for node in nodes:
            if node == self.head:
                self.head = node.next
                self.head.previous = None
                node.next = None
            elif node == self.tail:
                self.tail = node.previous
                self.tail.next = None
                node.previous = None
            else:
                left = node.previous
                right = node.next
                left.next = right
                right.previous = left

    def items(self):
        current = self.head
        while True:
            yield current
            if current.next: current = current.next
            else: break

class ListNode:
    def __init__(self, data):
        self.previous = None
        self.next = None
        self.data = data