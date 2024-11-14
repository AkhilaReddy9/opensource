vig,ch=input().split()
if (vig=='S' and ch=='P') or (vig=='R' and ch=='S') or (vig=='P' and ch=='R'):
    print("Vignesh")
elif (vig=='P' and ch=='S') or (vig=='S' and ch=='R') or (vig=='R' and ch=='P'):
    print("Charan")
else:
    print("NULL")
