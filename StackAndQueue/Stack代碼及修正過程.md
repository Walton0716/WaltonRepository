### Stack代碼
```python3
class Node:
    def __init__(self, val):
        self.data = val
        self.temp_min = val
        self.next = None

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x)
        else:
            temp_min = self.head.temp_min
            cur = self.head
            self.head = Node(x)
            self.next = cur
            if temp_min < self.head.data:
                self.head.temp_min = temp_min
                
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.data

    def getMin(self) -> int:
        return self.head.temp_min
```
