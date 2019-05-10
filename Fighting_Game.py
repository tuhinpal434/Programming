t = int(input())
if(t>10 and t<1):
    sys.exit()
for i in range(0, t):
    n = int(input())
    if(n>1000 and n<1):
        break
    vil = []
    vil_i=[]#villian energy
    pl = []
    pl_i=[]#Player energy
    f = True
    vil = [j for j in input().split(" ") if len(vil)<=n]
    pl = [k for k in input().split(" ") if len(pl)<=n]
    for m in range(0,n):
        vil_i.append(int(vil[m]))
        pl_i.append(int(pl[m]))
    vil_s=sorted(vil_i,reverse=True)
    pl_s =sorted(pl_i,reverse=True)
    for l in range(0,n):
        if((pl_s[l]>10000 or vil_s[l]>10000) and (pl_s[l]<1 or vil_s[l]<1)):
            break
        if(pl_s[l]>vil_s[l]):
            f=True
        else:
            f=False
    if (f):
        print("WIN")
    else:
        print("LOSE")