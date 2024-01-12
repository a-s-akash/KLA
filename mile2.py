import math
def distance(a,b):
    return (abs(a-b))
def points(dia, ang):
    z = math.radians(ang)
    x = (dia/2) * math.cos(z)
    y = (dia/2) * math.sin(z)
    return x, y
for ts in range(1,5):
    qloc = open(f"Workshop2024//Milestone2//Input//Testcase{ts}.txt",'r')
    x = []
    for i in qloc:
        j = (i.split(":"))
        x.append(j[1])
    sizea,sizeb = x[1].split("x")
    shifta,shiftb = x[2].split(',')
    refa,refb = x[3].split(',')
    shifta = int(shifta[1:])
    shiftb = int(shiftb[:-2])
    refa = int(refa[1:])
    refb = int(refb[:-1])
    sizea = int(sizea)
    sizeb = int(sizeb)
    dia = int(x[0])
    x = []
    for i in range(0,180):
        x.append(points(dia,i))
    y = []
    for i in x:
        a = i[0]*-1
        b = i[1]*-1
        y.append((a,b))
    z1 = x+y
    x = ((1, 2), (3, 4))
    z = tuple(i for s in z1 for i in s)
    flag = 0
    m = min(z)
    n = max(z)
    start = (shifta+refa,shiftb+refb)
    still = True
    remember = []
    pop = 0
    do = 0
    first = True
    a = (start[0]-sizea/2,start[1]-sizeb/2)
    remember.append(a)
    godown = 0
    iloc = 0
    jloc = 0
    adder= open(f"Workshop2024//Milestone2//Input//abc{ts}.txt",'w')
    adder.write(f'({iloc},{jloc}) : ({a[0]} , {a[1]})\n')
    loc = [(iloc,jloc)]
    while still:   
        if do == 0:
            a = (a[0]-sizea,a[1]) # left
            iloc-=1
        elif do ==1:
            a = (a[0]+sizea,a[1]) #right
            iloc+=1
        b = (a[0],a[1]+sizeb)
        c = (b[0]+sizea,b[1])
        d = (a[0]+sizea,a[1])
        if (a[0]>m and a[1]>m and a[0]<n and a[1]<n) or (b[0]>m and b[1]>m and b[0]<n and b[1]<n) or (c[0]>m and c[1]>m and c[0]<n and c[1]<n) or (d[0]>m and d[1]>m and d[0]<n and d[1]<n):
            adder.write(f'({iloc},{jloc}) : ({(a[0])} , {(a[1])})\n')
        else:
            if pop==0:
                a = remember[-1]
                iloc,jloc = loc[-1]
                pop =1
                do = 1
            elif pop == 1:
                a = remember[-1]
                iloc,jloc = loc[-1]
                pop = 0
                k = 0
                if godown == 0:
                    k = (a[0],a[1]+sizeb)#up
                    jloc+=1
                elif godown == 1:
                    k = (a[0],a[1]-sizeb) #down
                    jloc-=1
                else:
                    still = False
                    break
                if (k[0]>m and k[1]>m and k[0]<n and k[1]<n):
                    a = k
                    remember.append(a)
                    loc.append((iloc,jloc))
                else:
                    godown += 1
                    remember = [remember[0]]
                    loc = [loc[0]]
                do = 0
