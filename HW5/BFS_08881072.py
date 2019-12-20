# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        if s in self.graph:
            queue = []
            queue.append(s)
            check = []
            check.append(s)
            result = []
            while(len(queue)>0):
                start = queue.pop(0)
                nodes = self.graph[start]
                for w in nodes:
                    if w not in check:
                        queue.append(w)
                        check.append(w)
                result.append(start)
            return result
        else:
            return False
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        if s in self.graph:
            stack = []
            stack.append(s)
            check = []
            check.append(s)
            result = []
            while(len(stack)>0):
                start = stack[-1]
                del(stack[-1])
                nodes = self.graph[start]
                for w in nodes:
                    if w not in check:
                        stack.append(w)
                        check.append(w)
                result.append(start)
            return result
        else:
            return False
