'''
Module to demonstrate memoization and dynamic programming
'''
import time

def fibonacci(n, md):
    if n in md:
        return md[n]
    if n in (0, 1):
        r = 1
    else:
        r = fibonacci(n-1, md) + fibonacci(n-2, md)
    md[n] = r
    return r

def main():
    ts = time.perf_counter()
    print(fibonacci(n=899, md={}))
    print(time.perf_counter() - ts)

if __name__ == '__main__':
    main()