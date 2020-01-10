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
        if root == None:
            root = TreeNode(val)
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
        return Solution().search(root,val)
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
                return Solution().search(root.right,target)
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
"""
root = TreeNode(5)
node1 = TreeNode(3)
node2 = TreeNode(3)
node3 = TreeNode(-5)
node4 = TreeNode(8)
node5 = TreeNode(7)
node6 = TreeNode(6)
node7 = TreeNode(10)

root.left = node1
root.left.left = node2
root.left.left.left = node3
root.right = node4
root.right.left = node5
root.right.left.left = node6
root.right.right = node7

list=[]
print(Solution().preorder(root,list))

import copy
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
print(Solution().insert(root1,4) == root1.left.right)

root2=Solution().delete(root2,3)
print(root2.val==5 and root2.left.val==-5 and root2.left.left==None and root2.left.right== None)
print(root2.right.right.val==10 and root2.right.left.val==7 and root2.right.left.left.val==6)
print(root2.right.right.right==None and root2.right.right.left==None and root2.right.left.right==None)
print(root2.right.left.left.left==None and root2.right.left.left.right==None and root2.right.val==8)

print(Solution().search(root3,10) == root3.right.right)


root4 = Solution().modify(root,7,4)
"""
