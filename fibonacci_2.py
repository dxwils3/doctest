# in this module, we'll introduce an error
# note that we've changed the initial value of fibs to [1, 1]
# this will cause the output to shift by 1, i.e. F_0 will be 1.
# all our tests will fail, which you will see from the command line
# when executing "python fibonacci_2.py"

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
    """
    fibs = [1, 1] 
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

if __name__ == '__main__':
    import doctest
    doctest.testmod()


