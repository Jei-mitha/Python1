y=input("enter start:")
i=0
while(i<=10):
    x=int(input("enter the integers"))
    d=x
    i+=1
    for j in range(i):
       if(x>=d):
          d=x
z=input("shall we stop y/n??")
if(z=='y'):
  print("the greatest number is ",d)



