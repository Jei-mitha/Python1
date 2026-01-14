
s=input("enter the string")
l=list(s.split())
d=0
for i in l:
    x=len(i)
    if(d<=x):
        d=x
        longest_word=i

print("the longest word in the list is",longest_word)