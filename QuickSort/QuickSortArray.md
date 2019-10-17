## QuickSort-Code-Array
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
### :star:流程圖:
![avatar](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R5Vtbc5s4FP41fkxGF66PcZxuZ9qd3Zmks%2B2jgmWMFyMXy7G9v34lEAaEHNMasJN4MhMkHR3BOfrOTTDC98vdHylZzf9kUxqPEJjuRngyQghB3xL%2FZM8%2B74HQAXlPmEZT1Vd2PEb%2FUdVZkG2iKV3XCDljMY9W9c6AJQkNeK2PpCnb1slmLK6vuiIhbXQ8BiRu9v4TTfn88Bh%2BOfCZRuFcLe0hNx94JsG%2FYco2iVpvhPAs%2B%2BXDS1LwUg%2B6npMp21a68MMI36eM8fxqubunsRRuIbZ83qcjo4f7TmnC20x4%2FPzt2xMMwpV3%2FyXczv76utklN7Z6mBcSb2jxHE4sGI5nTPAVt833SlTOzw0rBm7WmSLvBAEGq105KK5C%2BX9MwygpWImbyrnlY0oeB8ZI3KhQt2iMt%2FOI08cVCeTIVmw50Tfny1i04GHmC0053R0VAzwIV%2BxaypaUp3tBoibYyM6nqA1rKfVsK8q3nbxvXtW7oiNqv4UHzqXMxYUS%2B6%2BowDOoQBdQMr2Te120gpis11FgkgudNrb6SalUHtsGzacu%2BlIaEx691NmbRKFW%2BJtF2e5RQncAuq2LHSJNnmu2SQOq5lW38UlWSGfFSRpS3mAlJEj2FbKVJFj%2Fyk0jUIOYuMh5lso%2FSPaM%2FeCfDUlkhOQqepHtSRyt%2Bcgeiz01sicF6%2Be0IIsEySyVDGFzcFEMNofagj0zmVRKAJwGvOSkfAYGHRkADMzbp2YBDFiAsC8T4BgQL7D8qJos5XMWsoTED2XvuC7HkuYrYyslvQXlfK%2FERzactZHtaSMi7jPD6msPBMwqONuM4JrqnJbI7wqarn8NehLaSPff1WDW%2BCGZC1ulmpOdWixv7VWrc%2F2KSC2T92sSO4LFMzcCBABq7kQHZ0dOQKyE6vGCq4VZpybAQbxGoZHOvcZCXJClNMsZs5gmwnfkLmTS2uTP2fJ5s76MuUdeXX%2B4pbnvLeBz4EcI%2BKAWO2H82wGfzsrSWXUW8DVWgkNA17oGr9Kld8AtvYNjDxImuP6wYYIHL6FQuov498p1JSgQrTImkI0iJLjG0KL15vF72Tw%2BqqcHELj9WBvPqi%2FkOK8HFjo9BN4QxgkfjSvWK5L8flyhstBFHkZUIow8TS0ji3yZNxBZOG0Tyf4iC%2Be9eRK7rTFwB%2FEkvjWsJyme%2F5yo3jOhLxqhcfbXQ82mC2hZmgf3DNBCBmg5vUHLe2%2FQci%2FrZ3VoHdzZYNg6%2F%2BgD2SZscSqdWVFmjYxF1urggXTxGukiJ82YXytqIdbyJx8acFtU0Wq1VdAXcIvo7f0A128J3J5qbw3gIgBuQeWHBoWxZyieXLAme2gMnzi13Rc9FeexW89P3J4qsth%2FPQ86OUGr4PaUN3VwimeM3BZvK3KDwL506Obal7AQRTmmLMH8qIy0K8d0aB3c4t2ak17DGcZrYHRJr1GIo4fECk9kcgXfDECha1TE5eDqXoND7xJ6TlvoecNAz2pZ0ewMbM75YOs20zr27kt9%2BMqzLaBnWxC5Bl%2Frm9It%2FQStM%2FR6761OMhQobd2g9g1K02uHXXjAlPJNKg8GoqtFju4CLdNLoIM6Pc9qaOMTide0ISvx1LwukJQKjZDnjEDKT%2BVPgtoeZ1ZsLPGSay2bQOIoTKQtpDPJSooyCkh8p7q5xJw83AmiJHzKAHhj9XOC4mopo%2BndDN%2BgBr0K350amvX2j6AG7cjTdJA1rBqaAcNTunnnWnBA%2FTjRNWjBG1QLzQL5x9OCbShfDKoF%2F3im2vYA3vyFxoMIcluesg%2F7fYalBUa2f%2BthjDxZuHMBhk1X3dH3GqJZfo6Tx1nlR0%2F44X8%3D =100x100)
