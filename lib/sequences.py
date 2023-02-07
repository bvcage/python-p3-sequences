#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1]
    if length == 0:
        fibonacci.clear()
    elif length == 1:
        fibonacci.pop()
    else:  
        for n in range(2, length):
            num = fibonacci[n-2] + fibonacci[n-1]
            fibonacci.append(num)
    print(fibonacci)