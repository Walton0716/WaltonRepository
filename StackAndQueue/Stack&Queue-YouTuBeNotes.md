### Stack&Queue YouTuBe視頻筆記

* [視頻播放](https://www.youtube.com/watch?v=wjI1WNcIntg)

Stack and Queue are both flexible with their sizes, so we don't have to allocate initially them to have a size, we can just add elements if we want and then also shrink it down.   
**The main difference** comes in how elements are removed from the stack or from the queue.
* A stack is what would be called a LIFO(last in first out) data structure.
* A queue is what would be called a FIFO(first in first out) data structure.

**The framework of queue class:**
```Java
public static class Queue{
    private static class Node{
        private int data;
        private Node next;
        private Node(int data){
            this.data = data;
        }
    }
}

    private Node head;//remove from the head  
    private Node tail;//add things to the tail
    public boolean isEmpty{
        return head == null;
    }
    
    public int peek(){
        return head.data;
    }
    
    public void add(int data){
        Node node = new Node(data);
        if (tail != null){
            tail.next = node;
        }
        tail = node;
        if (head == null){
            head = node;
        }
    }
    
    pubic int remove(){
        int data = head.data;
        head = head.next;
        if(head == null){
            tail = null;
        }
        return data;
    }
```
**The framework of stack class:**
```Java
public static class Queue{
    private static class Node{
        private int data;
        private Node next;
        private Node(int data){
            this.data = data;
        }
    }
}

    private Node top;
    
    public boolean isEmpty{
        return top == null;
    }
    
    public int peek(){
        return top.data;
    }
    
    public void push(int data){
        Node node = new Node(data);
        node.next = top;
        top = node;
    }
    
    public int pop(){
        int data = top.data;
        top = top.next;
        return data;
    }
```
