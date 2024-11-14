n=int(input())
def co(n):
    c=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            c+=1
    return c
print(co(n))
