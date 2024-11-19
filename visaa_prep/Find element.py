n=int(input())
arr=list(map(int,input().split()))
k=int(input())
f=-1
for i in range(0,len(arr)):
    if arr[i]==k:
        f=i
        break
if f!=-1:
    print(f)
else:
    print(-1)
