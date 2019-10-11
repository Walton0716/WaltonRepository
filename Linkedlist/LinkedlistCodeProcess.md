### 第一版LinkedlistCode:
__!WRONG__
```python
class Node(object):
    
    def __init__(self, value):
        self.val = value
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        i = 0
        if self.head==None:
            return -1
        else:
            while i< index-1:
                cur = cur.next
                if cur == None:
                    return -1
                i += 1
        cur = cur.next
        return cur.val
        

    def addAtHead(self, value):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addAtTail(self, value):
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.next = node
        

    def addAtIndex(self, index, value):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        cur = self.head
        i = 0
        if cur == None:
            print("This list is an enpty list")
        while i < index-1:
            cur = cur.next
            if cur == None:
                print("List is less than index")
            i += 1
        node = Node(value)
        node.next = cur .next
        cur.next = node
        if node.next == None:
            self.tail = node
                

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur = self.head
        i = 0
        if self.head == None:
            print("This list is an empty list")
        while i < index-1:
            cur = cur.next
            if cur == None:
                print("List is less than index")
            i += 1
        if index == 0 :
            self.head = cur.next
            cur = cur.next
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next == None:
            self.tail = cur
```
**第一版錯誤部分：**
```python
         def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        i = 0
        if self.head==None:
            return -1
        else:
            while i< index-1:
                cur = cur.next
                if cur == None:
                    return -1
                i += 1
        cur = cur.next
        return cur.val
 ```
 **錯誤提示爲：**__AttributeError: 'NoneType' object has no attribute 'val'__
 ##### 分析原因：
     可能由於在ClassNode部分的對象是self,而cur為self.head沒有next
     所以將cur改爲self即可
### 第二版LinkedlistCode:
__!RIGHT__
```Pyhthon
class Node(object):
    
    def __init__(self, value):
        self.val = value
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        i = 0
        if self.head==None:
            return -1
        else:
            while i< index-1:
                self = self.next
                if self == None:
                    return -1
                i += 1
        self = self.next
        return self.val
        

    def addAtHead(self, value):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addAtTail(self, value):
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.next = node
        

    def addAtIndex(self, index, value):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        cur = self.head
        i = 0
        if cur == None:
            print("This list is an enpty list")
        while i < index-1:
            cur = cur.next
            if cur == None:
                print("List is less than index")
            i += 1
        node = Node(value)
        node.next = cur .next
        cur.next = node
        if node.next == None:
            self.tail = node
                

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur = self.head
        i = 0
        if self.head == None:
            print("This list is an empty list")
        while i < index-1:
            cur = cur.next
            if cur == None:
                print("List is less than index")
            i += 1
        if index == 0 :
            self.head = cur.next
            cur = cur.next
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next == None:
            self.tail = cur


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```
