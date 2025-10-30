# 1. Write a program that takes a number n and prints the first n numbers in the Fibonacci sequence.
# Use both Recursion and regular method
number = int(input("Enter a number: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(number):
    print(fibonacci(i), end = "\t")

##iterative method
number = int(input("Enter a number: "))
a, b = 0, 1
for i in range(number):
    print(a, end="\t")
    a, b = b, a + b

