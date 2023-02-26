def bisection_search(list_name,target):
    bisection = int(len(list_name)/2)
    if len(list_name)==0:
        return "no " + target + " in here"
    elif target == list_name[bisection]:
        return target
    elif target > list_name[bisection]:
        return bisection_search(list_name[bisection+1:],target)
    else:
        return bisection_search(list_name[:bisection],target)


a = ["a","c","b","x","y","t"]
a.sort()
t = bisection_search(a,"t")

print(t)
