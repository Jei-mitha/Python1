l=[]
for i in range(5):
    x=int(input("enter the numbers"))
    l.append(x)
c={}
for i in l:
    if i in c:
       c[i]+=1
    else:
        c[i]=1
print("count of individual numbers ",c)
