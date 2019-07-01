# in this module, we'll add our expected output for fibonacci(-1)
# from our previous test, we know it'll be a stacktrace
# in fact, we can copy the stacktrace and paste it into this
# doctest as the expected output.
# Run "python fibonacci_4.py" to see that the test passed
# and that there are 2 remaining failures.
# We could copy the stacktrace for the other two, but that's
# really quite messy.  Luckily, doctest gives us an easier way,
# which we'll see in fibonacci_5

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
      File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/doctest.py", line 1329, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.fibonacci[3]>", line 1, in <module>
        fibonacci(-1)
      File "fibonacci_3.py", line 28, in fibonacci
        raise ValueError('n must be a non-negative integer')
    ValueError: n must be a non-negative integer
    >>> fibonacci(2.3)
    >>> fibonacci('a')
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

