# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:24:56 2019

@author: asus
"""
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self,root,val):
        if root.val == None:
            root.val = val
        else:
            if val <= root.val:
                if root.left:
                    Solution().insert(root.left,val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    Solution().insert(root.right,val)
                else:
                    root.right = TreeNode(val)
        return root
    
    def preorder(self,root,list):
        if root.val == None:
            if root.left:
                Solution().preorder(root.left,list)
            if root.right:
                Solution().preorder(root.right,list)
        else:
            list.append(root.val)
            if root.left:
                Solution().preorder(root.left,list)
            if root.right:
                Solution().preorder(root.right,list)
        return list
    
    def onlydelete(self,root,target):
        if root.val == target:
            root.val = None
        if root.left:
            Solution().onlydelete(root.left,target)
        if root.right:
            Solution().onlydelete(root.right,target)
        return root
    
    def delete(self,root,target):
        list = []
        Solution().onlydelete(root,target)
        Solution().preorder(root,list)
        length = len(list)
        newroot = TreeNode(list[0])
        for i in range(1,length,1):
            Solution().insert(newroot,list[i])
        return newroot
    
    def search(self,root,target):
        if root.val == None:
            return False
        if target < root.val:
            if root.left:
                return Solution().search(root.left,target)
            else:
                return False
        elif target == root.val:
            return root
        elif target > root.val:
            if root.right:
                Solution().search(root.right,target)
            else:
                return False 
            
    def modify(self,root,target,new_val):
        if root.val == None:
            return False
        else:
            if target < root.val:
                if root.left:
                    Solution().modify(root.left,target,new_val)
                else:
                    return False
            elif target == root.val:
                root.val = new_val
            elif target > root.val:
                if root.right:
                    Solution().modify(root.right,target,new_val)
                else:
                    return False
        return root
        
#################################
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(7)
node3 = TreeNode(8)
node4 = TreeNode(6)
node5 = TreeNode(3)

root.left = node1
root.right = node2
root.right.right = node3
root.right.left = node4
root.left.left = node5
"""
list = []
print(Solution().preorder(root,list))
root1 = Solution().insert(root,5)
list = []
print(Solution().preorder(root1,list))
root2 = Solution().delete(root,5)
list = []
print(Solution().preorder(root2,list))
print(Solution().search(root,3) == root.left.left)
"""
root3 = Solution().modify(root,7,8)
list = []
print(Solution().preorder(root3,list))
