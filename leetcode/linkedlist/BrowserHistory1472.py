class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)

    def visit(self, url: str) -> None:
        curr = ListNode(url, None, self.history)
        self.history.next = curr
        self.history = self.history.next
    def back(self, steps: int) -> str:
        idx = 0
        while idx < steps or self.history.prev is not None:
            self.history = self.history.prev
        return self.history.val
    def forward(self, steps: int) -> str:
        idx = 0
        while idx < steps or self.history.next is not None:
            self.history = self.history.next
        return self.history.val
class ListNode:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next