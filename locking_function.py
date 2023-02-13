'''
The caching_fibonacci() function has a cache of pre-calculated Fibonacci numbers. 
Inside it contains the function fibonacci(n), which will directly calculate the Fibonacci 
number itself. The caching_fibonacci() function returns the fibonacci function.

If the Fibonacci number is stored in the cache dictionary, 
the fibonacci function returns the number from the cache. 
If it is not in the cache, then calculates the number and puts it in the cache, 
and returns it from the fibonacci function.
'''

def caching_fibonacci():

    cache = {}

    def fibonacci(n):
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    return fibonacci


if __name__ == "__main__":
    a = caching_fibonacci()
    print(a(7))
