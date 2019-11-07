# Merge Sort 流程圖、學習歷程與文字説明：:books: 
1.**Merge Sort流程圖**    :page_facing_up:   
2.**Merge Sort文字説明**    :page_facing_up:       
3.**Merge Sort學習歷程**  :page_facing_up: 

### :one:Merge Sort流程图
#### 舉例説明： 
![](https://i.imgur.com/UcZ9UOK.jpg)
### :two:Merge Sort文字説明 
**merge_sort代碼主要有兩部分**：`mergesort()`、`mergify()`和`merge_sort()`組成。 
> :paperclip:**mergesort()部分：**
> > mergesort()函數主要是運用遞歸的來將所要進行mergesort的數列分成左右兩部分，一層一層進行排序，在一層一層返回

> :paperclip:**mergeify()部分:**
> >`left_len`:代表此時左邊數列的長度
> >`right_len`:代表此時右邊數列的長度
> >`left_arr`:表示的是左半部分的數列
> >`right_arr`:表示的是右半部分的數列
> >`left_num`:表示此時在左半部分數列進行比較的數字的位置
> >`right_num`:表示此時右半部分數列進行比較的數字的位置
> >mergify()的説明：
> > > 整個函數是將此時進行mergesort的數列從中間“切開”分成左右兩部分數列，分別數字儲存在left_arr和right_arr數組中，再依次將兩個數組中的數字進行比較，最後，將比較中小的數字儲存在原序列中。

> :paperclip:**merge_sort()部分:**
> > 將上面兩個函數結合在一起，進行mergesort排序



### :three:Heap Sort學習歷程
1. 首先學習了《演算法圖鑒》2-6章節(合并排序mergr sort)，對mergesort排序法進行了瞭解。:paperclip: [MergeSort的介紹](/MergeSort/MergeSort介绍.md)
2. 觀看了網站（http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html）
的思路后，瞭解到需要運用到**遞歸**的思想
3. 看了一下大概思路后，開始自己進行代碼的編寫，感覺最難理解的地方是：
**要把遞歸思想理解透徹，讓後運用到mergesort代碼中。**
