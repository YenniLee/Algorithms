# Notes from 3/18 with Brian Doyle 

# print that factorial of n 

def rec_factorial(n):
    print(n)
    # base case 
    if n <= 1:
        return 1
    # what step can we do recursively?
    
    return n * rec_factorial(n-1)

print(rec_factorial(5))


# Notes from 3/19 with Brian Doyle

# [0, 1, 1, 2, 3, 5, 8, 13, 21]
cache = {}

def rec_fib(n):
    #base cases
    # if n == 0:
    #    return 0
    # if n == 1:
    #   return 1
    if n in cache: 
        return cache[n]

    # if it's not in the cache, we must
    n_minus_1 = rec_fib(n-1)
    n_minus_2 = rec_fib(n-2)
    cache[n] = n_minus_1 + n_minus_2

    return cache[n]
