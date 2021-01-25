class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.output = []
   
        

    def push(self, x: int) -> None:
        return(self.output.append(x))
       
        

    def pop(self) -> None:
        return(self.output.pop())
        

    def top(self) -> int:
        return(self.output[-1])
        
        

    def getMin(self) -> int:
        #self.output.sort()
        return(min(self.output))


# Input["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]
# Expected
# [null,null,null,null,-3,null,0,-2]