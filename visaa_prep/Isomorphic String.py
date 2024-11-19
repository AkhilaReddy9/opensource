
n=int(input())
s=input().strip()
t=input().strip()
if len(set(zip(s,t)))==len(set(s))==len(set(t)):
    print("true")
else:
    print("false")
