l=[]
for i in range(0,5):
    x=int(input("enter tne number"))
    l.append(x)
for i in range(0,len(l)):
    if(i%2==0):
        l[i]=l[i]+5
    else:
        continue
print(l)

