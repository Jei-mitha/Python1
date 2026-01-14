'''l=[1,2,3,4,5]
k=[0,0,0,0,0]
i=0
while( i<len(l)):
    k[len(l)-1-i]=l[i]
    i+=1
print(k)
'''

l=[23,45,67,89,78]
k=[0,0,0,0,0]
i=len(l)-1
while(i>=0):
 k[i]=l[len(l)-1-i]
 i-=1
print(k)