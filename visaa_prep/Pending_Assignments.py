x,y,z=map(int,input().split())
time=x*y
if time<=(z*24*60):
    print("YES")
else:
    print("NO")
