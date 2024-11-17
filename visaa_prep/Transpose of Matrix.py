n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
def tra(mat):
    r=len(mat)
    col=len(mat[0])
    trans=[[mat[j][i] for j in range(r)] for i in range(col)]
    return trans
for r in tra(mat):
    print(*r)
