def match(m,n):
   # m=m.split()
    #n=n.split()
    v=[]
    for i in range(len(m)):
        for j in range(len(n)):
          if(m[i]==n[j]):
             
           v.append(m[i])
    return v
for i in v:
     if(count(i)==1):
      v.append(i)
     else:
      count(i)=count(i)-1
      v.append(i)
return v
m=input("enter the name 1 ")
n=input("enetr the name 2")
print("the common words in the two names are:",match(m,n))




        
