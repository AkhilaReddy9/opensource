n=input().strip().lower()
c1=0
c2=0
a='aeiou'
for ch in n:
    if ch.isalpha():
        if ch in a:
            c1+=1
        else:
            c2+=1
print(f"{c1},{c2}")
