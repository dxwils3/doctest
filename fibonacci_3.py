# fibonacci only makes sense for non-negative integers.
# in this module, we'll add testing the input for that property
# we'll also add some tests to see what happens with doctest
# when we run "python fibonacci_3.py" from the command line
# we'll see that doctest executes fibonacci(-1) (as an example)
# and gets a stacktrack back as a result.
# in the doctest below, we indicated that there would be no
# output, so the test fails, along with the two other new ones

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

