# we can replace all the stuff in the middle of the stacktrace with
# an ellipsis.  This means that we don't have to worry about getting
# the stacktrace exactly correct, and we can use the same expected
# output for all 3 tests.

# execute "python fibonacci_5.py" to see that all tests pass (i.e
# doctest produces no output.)

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
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

