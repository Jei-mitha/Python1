


def nested(l,m,n):
   t=play(x,y) 
   print("greatest numbers among x and y is :",t)
   for i in l:
      if(i%2==0):
         n.append(i)
      else:
         m.append(i)
   return n,m
def play(x,y):
   if(x>y):
      return x
   else:
      return y
x=int(input("enter the num"))
y=int(input("enter the num"))
l=[2,34,5,67,88,90,456,765,233]
m=[]
n=[]
print("the even and odd num lists are:",nested(l,m,n))