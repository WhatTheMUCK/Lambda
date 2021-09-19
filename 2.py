def Kolvo(a,b,c):
    if a==b==c:
        return 3
    if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        return 2
    if (a!=b) and (a!=c) and (b!=c):
        return 0
