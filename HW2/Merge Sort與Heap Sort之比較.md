# Merge_sort和Heap_sort排序法的比較：:books:

* `Merge_sort`是將想要排序的數列分割成幾乎等長的兩個數列，知道無法再分割（每個群組只剩下一個數）時，再將各組數列整合在一起。數的分割是不需要耗費執行時間的。
* `Heap_sort`是運用tree的形狀，將每個元素分別放置在各個節點上，再將children node與father node進行比較，選擇較小的數字擔任father,最後，選擇出root。以此類推。

#### 將兩者代碼進行比較后：
1. **空間利用不同**--**mergesort排序法**需要**額外的空間**，left_arr[]和right_arr[]用來放置左右兩個幾乎等長的數列;**Heap_sort排序法**則**不需要額外的空間**用來放置數字。
2. **執行時間相同**--**Mergesort排序法**和**Heap_sort排序法**的執行時間都是**O(nlog n)**

