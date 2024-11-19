n=int(input())
arr=list(map(int,input().split()))
alt=0
m_alt=alt

for i in arr:
    alt+=i
    m_alt=max(m_alt,alt)
print(m_alt)
