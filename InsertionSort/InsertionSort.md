## Insertion Sort :books:
---
##### 插入排序作法： 
    1.將資料分成已排序、未排序兩部分  
    2.依序由未排序的第一筆(正處理的值),插入到已排序的適當位置
    3.插入時由右而左比較，直到遇見第一個比正處理的值小的值
    4.再插入比較時，若遇到的值比正處理的值大或相等，則將值往右移
##### 時間複雜度(Time Complexity)
    Best Case:O(1)
     儅資料的順序恰好為由小到大時，每回合只需要比較1次
    Worst Case:O(n的平方)
     儅資料的順序恰好為由大到小時，第i回合需要比i次
    Average Case:O(n的平方)
     第n筆資料，平均比較n/2次
#### Demo :wave:
  - .[Video]()
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
