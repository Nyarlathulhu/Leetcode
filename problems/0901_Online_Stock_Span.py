# RELATED TOPICS:
# Stack | Design | Monotonic Stack | Data Stream

from collections import deque


class StockSpanner:

    def __init__(self):
        self.mono_stack = deque()
        self.span = -1
        

    def next(self, price: int) -> int:
        self.span += 1
        if not self.mono_stack or self.mono_stack[-1][1] > price:
            self.mono_stack.append([self.span, price])
        else:
            while self.mono_stack and self.mono_stack[-1][1] <= price:
                self.mono_stack.pop()
            self.mono_stack.append([self.span, price])
        
        return self.span + 1 if len(self.mono_stack) == 1 else self.span - self.mono_stack[-2][0]
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
    
