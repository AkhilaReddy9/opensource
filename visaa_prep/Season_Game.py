N=int(input())
if 3<=N<=5:
    print("Spring")
elif 6<=N<=9:
    print("Summer")
elif 10<=N<=11:
    print("Autumn")
elif N==12 or N==1 or N==2:
    print("Winter")
else:
    print("Invalid")
