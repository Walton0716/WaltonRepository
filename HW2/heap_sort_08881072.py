##### heap_sort_ID.py

class Solution(object):
    def heap_sort(self,nums):
        """
        :type arr: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        arr = nums
        n = len(arr) 
        m = len(arr)-1
        self.heapify(arr,1,n)
        for i in range(0,m,1):
            if (m-i) > 0:
                temp = arr[0]
                arr[0] = arr[m-i]
                arr[m-i] = temp
                self.heapify(arr,1,m-i)
        return arr;        

    def heapify(self,arr,front,end):
        n = end -front + 1
    # 判斷數列要比較幾次
        if n%2 == 0 :
            a = int(n/2)
        else:
            a =int( (n-1)/2)
        b = a-1
        width = front-1
        for i in range(b,-1,-1):
            if (2*i+1)< n:
                if arr[i+width] < arr[2*i+1+width]:
                    temp = arr[i+width]
                    arr[i+width] = arr[2*i+width+1]
                    arr[2*i+width+1] = temp
            if (2*i+2) < n:
                if arr[i+width] < arr[2*i+2+width]:
                    temp = arr[i+width]
                    arr[i+width] = arr[2*i+2+width]
                    arr[2*i+2+width] = temp
