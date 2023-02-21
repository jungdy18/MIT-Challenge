def f(x):
    ans = {}
    while len(x)>0:
        if not x[0] in ans:
            ans.update({x[0]:1})
        else:
            ans.update({x[0]:ans[x[0]]+1})
        x = x[1:]
    return ans
