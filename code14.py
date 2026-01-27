#count
c=0
l=[]
for i in range(5):
    x=int(input("enter"))
    l.append(x)
for i in range(len(l)):
    if(i==l[i-1::]):
        c+=1
    print(c)