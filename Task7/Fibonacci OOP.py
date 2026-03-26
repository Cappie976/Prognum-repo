#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
  
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
    
    def n_term(self):   #define first method of computing nth term of sequence
        n = self.n
        if n<0:
            raise ValueError
        elif n==0:
            return 0
        elif n==1:
            return 1
        
        a=0
        b=1  #initializing first two fibonacci numbers
        for i in range(2,n+1):
            a, b = b, a+b
        return b
    
    def divide_n_term(self):   #define second method of numbers less than n divisible by m
     
        if self.m==0:
            raise ValueError
        fib_n = self.n_term()
        
        result = []
        a=0
        b=1
        
        while a<fib_n:
            if a%self.m==0:
                result.append(a)
            a, b = b, a+b
        return result


#test
n = int(input("Enter the value n: "))
m = int(input("Enter the value m: "))

fib = Fibonacci(n, m)
    
#calling methods and printing results
nth_fib = fib.n_term()
print(f"The {n}th Fibonacci number is: {nth_fib}")
        

divisible_fibs = fib.divide_n_term()
print(f"Fibonacci numbers less than the {n}th term and divisible by {m}: {divisible_fibs}")
    
  

