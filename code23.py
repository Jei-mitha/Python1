def biometric(n):
    l=[]
    c=0
    for i in range(n):
            t=float(input("enter the time"))
            x=int(input("roll no"))
            y=input("enter the name")
            z=input("enter the department")
            if(t<=9.0):
               l.append([x,y,z])
               c+=1
    
            else:
                 print("you are late ....")
                 print("meet the principal")
    print("tota number of staffs is:",c)
    return l
#m=float(input("enter the time"))
n=int (input("enter the total staffs"))
print("the staffs before 9'0 clock entered are:",biometric(n))
