def f(x):
    ans = {}
    while len(x)>0:
        if not x[0] in ans:
            ans.update({x[0]:1})
        else:
            ans.update({x[0]:ans[x[0]]+1})
        x = x[1:]
    return ans

def max_word(y):
    ans = {}
    for key in f(y).keys():
        if f(y)[key] == max(f(y).values()):
            ans.update({key:f(y)[key]})
    return ans

