x=input("entr the string:")
y=len(x)
c=[]
v=[]
for i in range(y) :
   if(x[i] in 'aeiou'):
     v.append(x[i])

   else:
       c.append(x[i])
       
print("vowels in the string are:",v)     
print("consonants in the string are:",c)