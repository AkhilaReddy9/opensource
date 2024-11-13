s=input().strip()
out=[]
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        out.append(s[i-1]+str(count))
        count=1
out.append(s[-1]+str(count))
print(''.join(out))
