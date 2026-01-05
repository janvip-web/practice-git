import numpy as np

name = "Janvi Parmar"
a1 = np.array([1,3,5,7,9,11,13,15])
mean = np.mean(a1)

print("Name of Author:", name)
print("Mean of given array:",mean)

# data types :
age = 18 #int
sum = 124.535 #float
name = "Janvi Parmar" #string etc...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci numbers:",fibonacci(10))