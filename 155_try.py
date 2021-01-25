# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.top = None
#         self.count = 0
#         self.minimum = 0
        

#     def push(self, x: int) -> None:
#         self.top = x
#         self.count =+ 1
#         if (self.minimum > x):
#             self.minimum = x
#         return(self.append(x))
        

#     def pop(self) -> None:
#         y = len(self)
#         z=self[y]
#         self.remove(y)
#         return(self)
        
        

#     def top(self) -> int:
#         return(self[0])
        
        

#     def getMin(self) -> int:
#         self.sort()
#         return(self[0])
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()