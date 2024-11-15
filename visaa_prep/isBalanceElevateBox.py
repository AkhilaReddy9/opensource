n=int(input())
arr=list(map(int,input().split()))
res=[]
t=sum(arr)
ls=0
for i in range(len(arr)):
    rs=t-ls-arr[i]
    bal=abs(ls-rs)
    res.append(bal)
    ls+=arr[i]
print(" ".join(map(str,res)))
    
