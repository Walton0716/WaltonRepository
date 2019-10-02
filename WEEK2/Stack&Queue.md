## Stack&Queue

#### Stack的特徵：
先進來的后出去，類似於在桌子上擺盤子.

#### Queue的特徵：
先進來的先出去，不能從中間插入資料，類似於排隊.

#### 爲什麽要有Stack?
* 編輯器(如word等等)中的undo
* 網頁瀏覽器的 `回到前一頁`的功能
* 任何recursion形式的演算法，都可以用Stack改寫，例如：Depth-First Search(DFS,深度優先搜尋)

#### 爲什麽要有Queue？
* 演算法：Breadth-First Search(廣度優先搜尋)與tree的Level-Order Traversal會用到Queue
* 作業系統：被多個程式共享的資源，一次只能執行一個需求

#### Stack的必有功能：
1.`Push` 把資料放進Stack  
2.`Pop` 把最上面的資料從Stack中**移除**  
3.`Top` 回傳最上面的資料，**并沒有把最上面的資料移除**  
4.`IsEmpty` 確認箱子裏面是否有資料  
5.`getSize` 回傳Stack裏面的資料，記錄目前資料的個數  

#### Queue的必有功能：
1.`Push(data)` 把資料從Queue的後面放進Queue,並更新成新的back  
2.`Pop` 把front所指向的資料從Queue中移除，并更新front  
3.`getFront` 回傳front所指向的資料  
4.`getBack` 回傳back所指向的資料  
5.`IsEmpty` 確認Queue裏面是否有資料  
6.`getSize` 回傳Queue裏面的資料個數  

