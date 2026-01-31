def square(m,n):
    for i in m:
        d=i*i
        n.append(d)
    return n
l=[21,22,23,24,25,26,27,28,29]
k=[]
print("the squares of the given list is:",square(l,k))

