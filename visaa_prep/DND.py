n,m=map(int,input().split())
arr=list(map(int,input().split()))
s1=0
s2=0
for i in arr:
    if i%m==0:
        s1+=i
    else:
        s2+=i
print(s1-s2)
