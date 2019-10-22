## QuickSort-Code-Array
  *[補充：因爲.ipynb文件load不出來，所以將文件類型改爲.md。代碼是可以完整運行的。]*  
  *[補充：本次code有參考網路代碼]*
  * [code](#starcode)
  * [測試代碼](#star測試代碼)
  * [説明](#star説明)
  * [流程圖](#star流程圖)
  
### :star:code:
```python3
def quickSortHelper(list, front, end):
    if front < end :
        splitpoint = partition(list, front, end)
        quickSortHelper(list, front, splitpoint - 1)
        quickSortHelper(list, splitpoint +1, end)

def quickSort(list):
    quickSortHelper(list, 0, len(list)-1)

def partition(list, front, end):
    pivot = list[end]
    a = front-1
    b = front
    while b<len(list):
        if list[b]<pivot:
            a += 1
            temp = list[a]
            list[a] = list[b]
            list[b] = temp
        b += 1
    a += 1
    temp = list[a]
    list[a] = list[end]
    list[end] = temp
    return a
```
### :star:測試代碼：
```python
list = [23,46,12,3,56,28,45]
quickSort(list)
print(list)
```
```python
[3, 12, 23, 28, 45, 46, 56]
```
### :star:説明：
#### 對quickSorterHelper()函數的説明：  
    首先控制條件，看輸入的front和end是否符合數列排序的要求.儅符合要求時，進行partition(),對函數進行第一次排序，并將值返回給splitpoint.讓后再次
    進行quickSortHepler(),此時進行的是小於pivot的數列和大於pivot的數列。
    因此，分成兩部分:quickSortHelper(list,front,splitpoint-1)--小於pivot的部分,quickSortHelper(list,splitpoint+1,end)--大於pivot的部分。  
#### 對quickSort()函數的説明：
    用戶輸入時，只需打出quickSort(array1,number1,number2)即可排列數列的指定區間。
#### 對partition()函數的説明：`parition()`的功能是把一個數列分成`[大於pivot]`和`[小於pivot]`兩個部分   
    在parition()整個code裏面，a所控制的是：儅pivot大於arry[b]，arry[a+1]與arry[b]交換。
    在parition()函數里,pivot的位置在循環比較裏面並未有變換，但是是以pivot爲基准，在循環比較后將得到：小於pivot+大於pivot+pivot
    接著，讓a=a+1，將pivot與array[a]交換，可得到：小於pivot+pivot+大於pivot
每一個變數的含義：  
    `front`為這個數列的`最前面`的index    
    `end`為這個數列的`最尾端`的index    
    `a`為所有小於pivot的數所形成的數列的最後位置  
    `b`是控制while循環，讓每個數都與pivot比較的index，從front檢查到end-1，因爲end是pivot自己  
    `pivot`是在數列中所挑選的基準點，可以是任意的。選擇array[end]是爲了方便  
### :star:流程圖:
![avater](/Images/circle.png)
![avater](/Images/circle2.jpg)
![avater](/Images/circle1.jpg)
