# not reversal of list
'''l=[]
for i in range(5):
    x=int(input("enetr the numbers"))
    l.append(x)
print(l)
i=4
while(i>=0):
    l[4-i]=l[i]
    i-=1
print("the reversed list is :",l)'''

# not reversal of list
l=[]
for i in range(5):
    x=int(input("enetr the numbers"))
    l.append(x)
print(l)
n=len(l)
for i in range(n//2):
    t=l[i]
    l[i]=l[n-i-1]
    l[n-i-1]=t

print("the reversed list is :",l)

