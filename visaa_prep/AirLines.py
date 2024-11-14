x,n=map(int,input().split())
t=x*100
l=n-t
res=l/100
if res>int(res):
    print(int(res)+1)
else:
    print(int(res))
