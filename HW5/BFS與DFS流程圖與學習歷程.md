 本次學習歷程、流程圖與心得體驗 :hatched_chick: 
==========================
## ·Breadth-First-Search(BFS)學習歷程:smile:

:books: **通過閱讀《演算法圖鑑》，了解了BFS的基本知識：**
廣度優先搜尋法是屬於圖形搜尋的演算法。搜尋者本身可能並不了解圖形的全貌，同時假設自己在某一個「頂點」（也可以稱為**起點**），從起點開始進行搜尋，知道找到**目標頂點**。
:books:**BFS的搜尋方式：**
通過與binary tree對比到，BFS搜尋的方式為將每一級搜尋完以後，在進行下一級的搜尋。如圖片所示：
![](https://i.imgur.com/MHNSZgR.png)
```
Step1：進行level1的搜尋，若果沒有目標值，就進行下一級
Step2：進行level2的搜尋，先進行對B的搜尋，再進行C的搜尋
Step3：進行level3的搜尋....
........以此類推
```
所以，BFS演算法的主要**特征**為：   
**1.起點是由搜尋者自己進行選擇；  
2.每一級搜尋完，再進行下一級的搜尋**
## ·Breadth-First-Search(BFS)流程圖:smile:
![](https://i.imgur.com/1kFGUAe.jpg)
## ·Breadth-First-Search(BFS)代碼解釋:smile:

`queue`：用來存放接下來所要進行的搜尋的節點，並且每個節點的出現按照順序
`check`：用於存放已經出現的節點，當準備把某個節點放進`queue`時，需要先與`check`中的元素進行對比，看是否已經存在
`reslut`：用於存放整個搜尋後按順序從`queue`中取出的元素
整個代碼首先將queue、check和result設置成為空數組，將起始點（start）加入到queue和check中，說明start已經出現過，接下來再進行對start的節點進行搜尋，通過for循環，再依次尋找
## ·Depth-First-Search(DFS)學習歷程:smile:
:books: **DFS的基本知識：**
深度優先搜尋一樣是一種圖形搜尋的演算法。這項演算法的目的同樣也是從起點抵達指定頂點。
:books:**DFS的搜尋方式：**
DFS在搜尋時，先探查單一路徑，直到無法繼續前進，再折返探查下一選擇路徑。如圖片所示：
![](https://i.imgur.com/O46SPSz.png)
```
Step1：首先對A-B-D進行搜尋，如果沒有找到，則進行Step2
Step2：沒有找到的話，從D返回B，再對E-G進行搜尋
Step3：如果未找到，則從G返回E,對H進行搜尋
......(以此類推）
```
所以，DFS演算法的主要**特征**為：  
**1.起點是由搜尋者自己進行選擇；   
2.把每條路徑搜尋到最深處，再返回，進行其他路徑的搜尋。**
## ·Dreadth-First-Search(BFS)流程圖:smile:
![](https://i.imgur.com/QL5wXer.jpg)

## ·Depth-First-Search(DFS)代碼解釋:smile:

`stack`：用來存放接下來所要進行的搜尋的節點，並且每個節點的出現按照順序
`check`：用於存放已經出現的節點，當準備把某個節點放進`stack`時，需要先與`check`中的元素進行對比，看是否已經存在
`reslut`：用於存放整個搜尋後按順序從`stack`中取出的元素
整個代碼首先將stack、check和result設置成為空數組，將起始點（start）加入到stack和check中，說明start已經出現過，接下來再進行對start的節點進行搜尋，通過for循環，再依次尋找,唯一不同的是，stack裡面是取最後一個元素。
