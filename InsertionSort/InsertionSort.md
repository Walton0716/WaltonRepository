## Insertion Sort筆記 :books:
---
##### 插入排序作法： 
    1.將資料分成已排序、未排序兩部分  
    2.依序由未排序的第一筆(正處理的值),插入到已排序的適當位置
    3.插入時由右而左比較，直到遇見第一個比正處理的值小的值
    4.再插入比較時，若遇到的值比正處理的值大或相等，則將值往右移
##### 時間複雜度(Time Complexity)
    Best Case:O(1)
     儅資料的順序恰好為由小到大時，每回合只需要比較1次
    Worst Case:O(n^2)
     儅資料的順序恰好為由大到小時，第i回合需要比i次
    Average Case:O(n^2)
     第n筆資料，平均比較n/2次
#### Demo :wave:
  - [Video](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)
  - 演算法
  ```js
  var insertionSort = function(data){
      var i, j, temp;
      for(i = 1; i < data.length; i++){
        temp = data[i];
        for(j = i; j > 0 && temp < data[j-1]; j--){
          data[j] = data[j-1];
        }
        data[j] = temp;
      }
  }
  ```
---
### InsertionSort--Example:
     step1.首先給定一組data[2,7,4,8,9,3]
     step2.因爲data[0]左邊沒有數字，所以不需要比較，直接從data[1]開始比較
     step3.data[1]為7，將data[1]與左邊data[0]比較，7>2，所以不用變化,
           得到[2,7,4,8,9,3]
     step4.data[2]作爲基準值，開始與自己左邊的數字進行比較，與data[1]比較
           得到[2,4,7,8,9,3]
           再次比較
           得到[2,4,7,8,9,3]
     step5.data[3]作爲基準值，與左邊的數字進行比較
           得到[2,4,7,8,9,3]
     step6.data[4]作爲基準值，與左邊的數字進行比較
           得到[2,4,7,8,9,3]
     step7.data[5]作爲基準值，與左邊的數字進行比較,依次
           得到[2,4,7,8,3,9]
           得到[2,4,7,3,8,9]
           得到[2,4,3,7,8,9]
           得到[2,3,4,7,8,9]
           完成InsertionSort
----     
### 實作：
##### 對於實現InsertionSort，需要兩個loops。
> **第一個loop**是將遍歷數組的未排序部分。
> >**第二個loop**是對於每個未排序的元素，遍歷已經排序的部分並搜索其正確的位置  

從兩個loop的含義可知道要將**第二個loop嵌套在第一個loop中**。找到正確的位置以插入當前元素后，我們需要移動所有剩餘的元素。爲此，我們需要一個循環。  
