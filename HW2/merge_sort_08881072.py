#### [思路參考：http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html]
###### merge_sort_ID.py

class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        arr = nums
        end = len(arr) - 1
        self.mergesort(arr,0, end)
        return arr;
    
    def mergesort(self,arr,front,end):
        if front < end:
            if (front+end)%2 == 0:
                mid = int((front+end)/2)
            else:
                mid = int((front+end-1)/2)
            self.mergesort(arr,front,mid)
            self.mergesort(arr,mid+1,end)
            self.mergeify(arr,front,mid,end)
            
    def mergeify(self,arr,front,mid,end):
        left_len = mid-front+1
        right_len = end-mid
        left_arr = [0]*left_len
        right_arr = [0]*right_len
        for i in range(0,left_len,1):
            left_arr[i] = arr[front+i]
        for j in range(0,right_len,1):
            right_arr[j] = arr[mid+1+j]
        left_num = 0
        right_num = 0
        for m in range(front,end+1,1):
            if left_arr[left_num] < right_arr[right_num]:
                arr[m] = left_arr[left_num]
                if left_num < (left_len-1):
                    left_num = left_num +1
                else:
                    left_arr[left_num] = float('inf')
            else:
                arr[m] = right_arr[right_num]
                if right_num < (right_len-1):
                    right_num += 1
                else:
                    right_arr[right_num] = float('inf')
