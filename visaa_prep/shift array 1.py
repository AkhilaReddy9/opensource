n=int(input())
arr=list(map(int,input().split()))
if len(arr)>1:
    arr.append(arr.pop(0))
print(*arr)
