n=int(input())
x=list(map(int,input().split()))
if x==sorted(x):
    print("true")
else:
    print("false")
