def fib(nterms):
    n1, n2 = 1, 1
    count = 0

    while count < nterms:
        nth = n1 + n2
        n1, n2 = n2, nth
        count += 1
    return n1
