n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k=k%n
x=arr[-k:]+arr[:-k]
print(*x)
