# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:23:15 2019

@author: asus
"""

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def add(self,key):
        if self.next:
            return self.next.add(key)
        else:
            self.next = ListNode(key)
            return True
    
    def remove(self,key):
        if self.val == key:
            if self.next:
                self.val = self.next.val
                self.next = self.next.next
                return self.remove(key)
            else:
                self.val = None
                return True
        else:
            if self.next:
                return self.next.remove(key)
            else:
                return False
    
    def contains(self,key):
        if self.val == key:
            return True
        else:
            if self.next:
                return self.next.contains(key)
            else:
                return False
            
class MyHashSet:
    def __init__(self,capacity=5):
        self.capacity = capacity
        self.data = [None]*capacity
        
    def add(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = int(h.hexdigest(),16)
        modnumber = x % 5
        if self.data[modnumber]:
            return self.data[modnumber].add(key)
        else:
            self.data[modnumber] = ListNode(key)
            return True
        
    def remove(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = int(h.hexdigest(),16)
        modnumber = x % 5
        if self.data[modnumber]:
            return self.data[modnumber].remove(key)
        else:
            return False
        
    def contains(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = int(h.hexdigest(),16)
        modnumber = x % 5
        if self.data[modnumber]:
            return self.data[modnumber].contains(key)
        else:
            return False
        
