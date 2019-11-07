# Heap Sort 流程圖、學習歷程與文字説明：:books: 
:one:**Heap Sort文字説明**  
:two:**Heap Sort學習歷程**  
:three:**Heap Sort流程圖**  

### Heap Sort文字説明:page_facing_up: 
**heap_sort代碼主要有兩部分**：`heapify()`和`heap_sort()`組成。 
> :paperclip:**heapify()部分：**
> > `front`:進行heapsort的初始位置
> > `end`:進行heapsort的結束位置
> > `n`:進行heapsort的數列的長度，用來決定進行eapsort的數列可以分成多少層
> > `a`:數列分成的層數
> > **heapify()函數的解釋：**
> > >heapify()首先決定整個函數可以分成“幾層”，讓後決定每層的元素的每個位置是多少，最後通過代碼
> > >```python
> > >for i in range(b,-1,-1):
> > >    if (2*i+1)< n:
> > >        if arr[i+width] < arr[2*i+1+width]:
> > >            temp = arr[i+width]
> > >            arr[i+width] = arr[2*i+width+1]
> > >            arr[2*i+width+1] = temp
> > >    if (2*i+2) < n:
> > >        if arr[i+width] < arr[2*i+2+width]:
> > >            temp = arr[i+width]
> > >            arr[i+width] = arr[2*i+2+width]
> > >            arr[2*i+2+width] = temp
> > >```
> > >讓每一個children與自己的father比較，如果children大於自己的father，就與自己的father交換位置

> :paperclip:**heap_sort()部分:**
> >`n`:代表的是進行heap_sort的數列的長度
> >`m`:代表的是進行heap_sort的數列最後一個數的位置
> >**heap_sort()函數解釋：**
> > > heap_sort()先讓整個數列進行一次heapify(),讓後讓root放在整個數列的end位置，讓後將front與end-1位進行heapify(),把root放在整個數列的end-1位置，以此類推。
> > > 最後，整個數列變成由小到大的順序。

### Heap Sort學習歷程:page_facing_up: 
1. 在進行HeapSort代碼的編寫之前，先瀏覽了老師推薦的《演算法圖鑑》1-7章節(堆積Heap),更加細緻地了解了Heap的相關內容，感覺很不錯。  
:paperclip:   [Heap介紹](/HeapSort/Heap的介紹.md)
2. 看完Heap的介紹後，又瀏覽了2-5章節(堆積排序heap sort)，將heap sort的排序方法了解了。
3. 一切都看完後，先將老師的代碼跑一邊，發現可行，瀏覽老師的代碼以後，發現主要思想：  
**抓住每個children與自己father的位置之間的聯繫，思考他們的位置如何通過相關的變量來控制。**
4. 掌握主要思想後，開始進行code的編寫
5. 整個code最難的是在思考：  
**如何不需要額外的空間，就可以將整個數列heapsort完後才能後，取出root,然後再進行heapsort，再取出root，以此類推，直到整個數全部取出完成。**
