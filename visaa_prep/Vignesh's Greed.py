n=int(input())
side=list(map(int,input().split()))
def tri(side):
    side.sort(reverse=True)

    for i in range(len(side)-2):
        if side[i]<side[i+1]+side[i+2]:
            return side[i]+side[i+1]+side[i+2]
    return -1
print(tri(side))
