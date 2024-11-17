n,m=map(int,input().split())
gr=[list(map(int,input().split())) for _ in range(n)]
r=[False]*n
c=[False]*m
for i in range(n):
    for j in range(m):
        if gr[i][j]==0:
            r[i]=True
            c[j]=True
for i in range(n):
    for j in range(m):
        if r[i] or c[j]:
            gr[i][j]=0
for r in gr:
    print(*r)
