### “Introduction to Linked List” 視頻筆記：
    an array  =  a long box with many parititions of the same size
    a linked list  =  many boxes that are connected to each other
*How a lined list can be implemented ?*
*Step1:*  
The class of the objecst is called Box,
```
	class Box {
   	 int/string data
   	 Box next
	}
```
head <->head.data     head.next<->head.next.data

*Step2:*  
```
       class Box{
             int data;
             Box next;
             Box(int data){
                 this.data = data;
            }
       }
```
*Step3:*  
the Box real name is Node,
```
class Node{
	int data;
	Node next;
	Node(int data){
	    this.data = data;
	}
      }
```
example:   
   	Node nodeA = New Node(6);              nodeA.next = nodeB;
  	 Node nodeB = New Node(3);              nodeB.next = nodeC;
  	 Node nodeC = New Node(4);              nodeC.next = nodeD;
  	 Node nodeA = New Node(2);              nodeD.next = nodeE;
  	 Node nodeA = New Node(1);
*Step4:*
```
       def countNodes(head){
          #write your code here
       }
```
     assme that head != null
     
*Step5:*
How many Linked List nodes do we have?
```
def countNodes(Node head){
	//assuming that head != null
	int count = 1;
	Node current = head;
	while (current.next != null){
	current = current.next;
	count += 1;
	}
     }
```    
*Step6:*  
DOUBLE-Linked List
```
class Node {
 	 int data;
	 Node next;
	 Node prev;
	 Node(int data){
		 this.data = data
		}
 }
 ```
