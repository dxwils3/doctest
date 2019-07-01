# Here, the developer decides to improve the code by caching the results.
# In this case, that just means making fibs a module level variable.
# If we've already computed the n_th fibonacci number, it'll
# be stored in fibs and we can just return it.  This should reduce
# the time spend recomputing Fibonacci numbers.

# here, we can see the advantage of having good unit tests in our doctest.
# we can run "python fibonacci_6.py" and see that our tests fail!
# we refactored working code into non-working code, but we know
# that if we fix the code and pass the tests, then we are done.

fibs = [0, 1]
def fibonacci(n):
    """
    Return the n_th Fibonnaci number $F_n$.  The Fibonacci sequence
    starts 0, 1, 1, 2, 3, 5, 8, ..., and is defined as
    $F_n = F_{n-1} + F_{n-2}.$

    >>> fibonacci(0)
    0
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    >>> fibonacci(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be a non-negative integer
    >>> fibonacci(2.3)
    Traceback (most recent call last):
    ...
    ValueError: n must be a non-negative integer
    >>> fibonacci('a')
    Traceback (most recent call last):
    ...
    ValueError: n must be a non-negative integer
    """
    if not isinstance(n, int):
        raise ValueError('n must be a non-negative integer')
    if n < 0:
        raise ValueError('n must be a non-negative integer')                
    if len(fibs) >= n: # we've already computed this one!
        return fibs[n]
    for i in range(len(fibs), n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
