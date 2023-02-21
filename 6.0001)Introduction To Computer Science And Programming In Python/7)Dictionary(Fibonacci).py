def fib_dict(x):
    ans = {"1":1, "2":1}
    while int(x)>len(ans):
        ans[str(len(ans)+1)] = ans[str(len(ans))] + ans[str(len(ans)-1)]
    return ans[str(x)]