def intmaxmin(l):
    d=l[0]
    c=l[0]
    for i in l:
        if(d<=i):          
            d=i
    for i in l:
        if(c>=i):
            c=i
    return c,d
l=[12,45,67,89,56]
print("the greatest num is:",intmaxmin(l))


