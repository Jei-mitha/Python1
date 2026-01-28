x=input("enter the string")
y=x.split()
#l=[] 
m=""
for i in y:
    for j in range(len(i)):
        if (j==0):
            #l.append(i[j]) 
            m=m+i[j]
print("the abbreviated form of the name is",m)
