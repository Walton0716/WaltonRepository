```Python3
class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.temp_min = val 
        self.next = nextNode

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
    def push(self, x: int) -> None:  
        //當head層是空的時候，直接往head層賦值就可以了
        if self.head is None:
            self.head = Node(x, None)
        else:
        //黨head曾不爲空的時候，先把原來的最小值賦值給臨時的temp
            temp = self.head.temp_min
        //運用Node函數直接把head層賦值新值，同時把原來的值賦值給next
            self.head = Node(x, self.head)
        //比較新進來的值與臨時的最小值
            if temp < self.head.val:
                self.head.temp_min = temp
                
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.temp_min
```
