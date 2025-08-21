
class Fibonacci:
    def __init__(self,num):
        self.num = num
        
    def num_check(self):
        if self.num == 0:
            return [0]
        elif self.num == 1:
            return [1] 
        a = 0
        b = 1 
        fib_series = [a,b]
        for i in range(2,self.num):
            c = a + b
            fib_series.append(c)
            a = b 
            b = c
        return fib_series

n = int(input("Enter the number of term's : "))
obj = Fibonacci(n)
print(obj.num_check())
            
            
           
            
