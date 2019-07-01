"""
Now we introduce a doctest.

The doctest looks like code from an interactive python shell, along
with the output.

doctest will execute the code and verify that the output matches the
expected output exactly.

For example, changing 55 to 55.0 will cause the doctest to fail.

All of these doctests succeed, resulting in no output when run from
the command line.  To verify that the tests are being executed, you
can run the following from the command line for verbose output

    python -m doctest -v fibonacci_1.py

Note that "no output for passing" is a good thing because you can
throw all your doctests into a cron job and cron will send you a
message when your script produces an output, i.e. when tests fail.

"""

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
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

# We execute the doctest by adding in a call to testmod.
# adding the "if __name__ == "__main__"" line will cause this code
# to execute only when called from the command line

# running "python fibonacci_1.py" from the shell will execute the tests
# in this case, all tests pass and there will be no output
# doctest only displays output when the test fails.

if __name__ == '__main__':
    import doctest
    doctest.testmod()

