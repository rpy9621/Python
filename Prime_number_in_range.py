class Prime:
    def __init__(self,lower,uper):
        self.lower = lower
        self.upper = upper
        
    def check_prime(self,num):
      
        
        if num == 1:
            return False
        
        elif num >=1 :
            for i in range(2, num):
                if num % i == 0:
                    return False
        return True
        
    def display_prime(self):
        print(f"Prime number between {self.lower} and {self.upper} are :\t")
        for num in range(self.lower,self.upper + 1):
            if self.check_prime(num):
                print(num, end=" ")

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

prime_obj = Prime(lower, upper)
prime_obj.display_prime()
