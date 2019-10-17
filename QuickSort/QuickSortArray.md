## QuickSort-Code-Array
  * [code](#starcode)
  * [測試代碼](#star測試代碼)
  * [説明](#star説明)
  * [TimeComplexities演算法](#starTimeComplexities演算法)
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
    i = front-1
    j = front
    while j<len(list):
        if list[j]<pivot:
            i += 1
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        j += 1
    i += 1
    temp = list[i]
    list[i] = list[end]
    list[end] = temp
    return i
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
#### 對quickSorterHelper()函數的解釋：  
    首先控制條件，看輸入的front和end是否符合數列排序的要求.儅符合要求時，進行partition(),對函數進行第一次排序，并將值返回給splitpoint.讓后再次
    進行quickSortHepler(),此時進行的是小於pivot的數列和大於pivot的數列。
    因此，分成兩部分:quickSortHelper(list,front,splitpoint-1)--小於pivot的部分,quickSortHelper(list,splitpoint+1,end)--大於pivot的部分。  
#### 對quickSort()函數的解釋：
    用戶輸入時，只需打出quickSort(array1,number1,number2)即可排列數列的指定區間。
#### 對partition()函數的解釋：
**`parition()`的功能是把一個數列分成`[大於pivot]`和`[小於pivot]`兩個部分**    
變數的含義：  
* `front`為這個數列的`最前面`的index  
* `end`為這個數列的`最尾端`的index  
* `i`為所有小於pivot的數所形成的數列的最後位置
* `j`是控制while循環，讓每個數都與pivot比較的index，從front檢查到end-1，因爲end是pivot自己
* `pivot`是在數列中所挑選的基準點，可以是任意的。選擇array[end]是爲了方便
### :star:TimeComplexities演算法
### :star:流程圖:
![avater](/Images/circle.png)
![avater](/Images/circle2.jpg)
![avater](/Images/circle1.jpg)
