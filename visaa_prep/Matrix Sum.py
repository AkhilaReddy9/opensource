n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
re=[]
for i in range(n):
    rs=sum(mat[i])
    cs=sum(mat[j][i] for j in range(n))
    re.append(rs+cs)
print(" ".join(map(str,re)))
    
