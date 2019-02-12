def fib(n):
    x=0
    y=1
    show=0
    print(x)
    print(y)
    while(n>0):
        show=x+y
        x=y
        y=show
        print(show)
        n=n-1
fib(6)
