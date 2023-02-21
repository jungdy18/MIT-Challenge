def log(a,x):
    epsilon = 0.0001
    ans = 1.0
    high = x
    low = -a**(x**(-1))
    while abs(x-a**ans)>epsilon:
        if x>a**ans:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans