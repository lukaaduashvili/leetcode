class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        curr_idx = 0
        curr = self.head
        if index >= self.length:
            return -1
        while curr_idx < index:
            curr_idx = curr_idx + 1
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.length += 1
        if self.head is None:
            self.head = ListNode(val)
        else:
            next_n = self.head
            self.head = ListNode(val, next_n)
            return

        if self.tail is None:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        self.length += 1
        if self.tail is None:
            self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
            return

        if self.head is None:
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return

        self.length += 1
        curr_idx = 0
        curr = self.head
        while curr_idx < index - 1:
            curr_idx = curr_idx + 1
            curr = curr.next
        new_n = ListNode(val, curr.next)
        curr.next = new_n

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == 0:
            self.length -= 1
            self.head = self.head.next
            return

        curr_idx = 0
        curr = self.head
        while curr_idx < index - 1:
            curr_idx = curr_idx + 1
            curr = curr.next

        if index == self.length - 1:
            self.tail = curr
            self.tail.next = None
        else:
            curr.next = curr.next.next
        self.length -= 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == '__main__':
    ll = MyLinkedList()
    values = ["addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
    params = [[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
    idx = 0
    for value in values:
        if value == "addAtHead":
            print("addAtHead", params[idx][0])
            print("operation idx:", idx)
            ll.addAtHead(params[idx][0])
            ll.printSize()
        elif value == "addAtTail":
            print("addAtTail", params[idx][0])
            print("operation idx:", idx)
            ll.addAtTail(params[idx][0])
            ll.printSize()
        elif value == "addAtIndex":
            print("addAtIndex", params[idx][0], params[idx][1])
            print("operation idx:", idx)
            ll.addAtIndex(params[idx][0], params[idx][1])
            ll.printSize()
        elif value == "deleteAtIndex":
            print("deleteAtIndex", params[idx][0])
            print("operation idx:", idx)
            ll.deleteAtIndex(params[idx][0])
            ll.printSize()
        elif value == "get":
            print("get", params[idx][0])
            print("operation idx:", idx)
            ll.get(params[idx][0])
            ll.printSize()
        idx += 1

