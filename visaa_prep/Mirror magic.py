n=int(input())
mat=[]
for _ in range(n):
    r=list(map(int,input().split()))
    mat.append(r)
for i in mat:
    print(*i[::-1])
