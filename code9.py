s=input("enter the string")
s=s.split()
wordcount={}
for i in s:
    if i in wordcount:
        wordcount[i]+=1
    else:
        wordcount[i]=1
print(wordcount)
for k,v in wordcount.items():
    if v>1:
        print(k,v)
