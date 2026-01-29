def play(l):
    c=0
    for i in l:
        c+=i
    return c
l=[23,24,56,78,90]
e=play(l)
print("sum of the list is:",e)
d=e/len(l)
print("the avg is:",d)
    