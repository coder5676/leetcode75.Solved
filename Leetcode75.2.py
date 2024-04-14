st1="aaaaaaaaaa"
st2="aaaaa"
a=[]
b=[]
res=""
l1=len(st1)
l2=len(st2)
for i in range(1,min(l1,l2)+1):
    if(l1%i==0 and l2%i==0):
        a.append(i)

print(a)

        
        
        




        
