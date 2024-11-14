n=int(input())
k=int(input())
if n&(1<<(k-1)):
    print("true")
else:
    print("false")
