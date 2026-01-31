def numlist(p,q):
    l=[]
    for i in p:
        if(i!=q):
            l.append(i)

        else:
            continue
    return l    
p=[34,67,89,807,45,4655,467565]
q=int(input("enter the number"))
print("the deleted element and the remaining list",q,numlist(p,q))
