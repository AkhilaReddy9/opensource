n=int(input())
c=1
for i in range(1,n+1):
    for j in range(i):
        print(c,end=" ")
        c+=1
    print()
