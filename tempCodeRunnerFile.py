def sum1(n):
    if n<=0:
        return 0
    return n+ sum(n-1)
sum1(3)