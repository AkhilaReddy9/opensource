n=int(input())
si=-1 if n<0 else 1
s=int(str(abs(n))[::-1])*si
if s>2**31-1 or s <-2**31:
    print(0)
else:
    print(s)
