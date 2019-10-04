### Stack代碼
* 错误版本：  
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
运行结果为：`ArrtibuteError:'NoneType' Object has no attribute 'data'`  

更正：将push中的 self.next = cur 更改为 self.head.next = cur
* 正确代码:
```python
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
            self.head.next = cur
            if temp_min < self.head.data:
                self.head.temp_min = temp_min
                
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.data

    def getMin(self) -> int:
        return self.head.temp_min
```
* 错误原因：**next对象应该是Node class的 MinStack中的self代指的是Minstack对象,所以  而self.head才是node对象 需要用self.head.next**
