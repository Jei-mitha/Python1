l=[]
g=[]
h=[]
print("enter the numbers of list1")
for i in range(5):
    x=int(input("enter the num"))
    l.append(x)
print("enter the numbers of list2")
for i in range(5):
    y=int(input("enter the num"))
    g.append(y)
for i in l:
    for j in g:
     if(i==j):
       h.append(i)
print("the common numbers are:",h)