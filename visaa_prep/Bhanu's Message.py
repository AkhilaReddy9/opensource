def isv(msg):
    if len(msg)<10 or len(msg)>20:
        return False
    if msg[0]=='+':
        msg=msg[1:]
    if not all(c.isdigit() or c==' ' for c in msg):
        return False
    n=msg.split()
    if len(n)==2:
        co,ph=n[0],n[1]
        if not(len(co)==2 and co.isdigit()):
            return False
    elif len(n)==1:
        ph=n[0]
    else:
        return False
    if len(ph)!=10 or not ph.isdigit():
        return False
    sd=sum(int(d) for d in ph)
    return sd>0
msg=input().strip()
if isv(msg):
    print("Correct")
else:
    print("Incorrect")
