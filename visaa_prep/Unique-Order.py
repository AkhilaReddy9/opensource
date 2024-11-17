n=int(input())
arr=list(map(int,input().split()))
uni=[]
se=set()
for n in arr:
    if n not in se:
        uni.append(n)
        se.add(n)
print(*uni)
