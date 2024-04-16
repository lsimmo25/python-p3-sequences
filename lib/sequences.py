#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fib = []
    elif length == 1:
        fib = [0]
    else:
        fib = [0, 1]

    while len(fib) < length:
        new_fib = fib[-1] + fib[-2]
        fib.append(new_fib)
    
    print(fib)