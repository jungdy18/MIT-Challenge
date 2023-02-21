def Fibonacci(x):
    if x==1 or x==2:
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)