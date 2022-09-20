import math
from re import A
a=int(input("scrieti nr 1: "))
b=int(input("scrieti nr 2: "))
def sum(x,y):
    return x+y
c=sum(a,b)
print("sum of",a,"and",b,"is",c)

def prod(x,y):
    return x*y
c=prod(a,b)
print("prod of",a,"and",b,"is",c)

def media(x,y):
    return (x+y)/2
c=media(a,b)
print("media of",a,"and",b,"is",c)

def cmmdc(a,b):
    while b!=0:
        a,b=abs(b),abs(a%b)
    return a
print('Cel mai mare divizor',cmmdc(a,b))

def cmmmc(a,b):
    return abs(a*b)/cmmdc(a,b) 
print('Cel mai mic multiplu',cmmmc(a,b))

def maxim(x,y):
    t=[]
    t.extend([x,y])
    c=max(t)
    return c 
print('nr maxim =',maxim(a,b))

def minim(x,y):
    t=[]
    t.extend([x,y])
    c=min(t)
    return c 
print('nr minim =',minim(a,b))

def sum2():
    print(f"{a}+{b}={sum(a,b)}")
sum2()

def prod2():
    print(f"{a}*{b}={prod(a,b)}")
prod2()

def divizori(a,b):
    x=[]
    y=[]
    for i in range (1,a+1):
        if (a%i==0):
            x.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            y.append(j)
    c=set(x).intersection(y)
    q=list(c)
    return print("divizorii comuni lui ",a," si ",b," = ",q)
divizori(a,b)

def cinci_multipli(a,b):
    multiplii=[]
    if a>b:
        mp=a
    elif b>a:
        mp=b
    else:
        mp=a
    while len(multiplii)<5:
        if ((mp%a==0)and(mp%b==0)):
            multiplii.append(mp)
            mp +=1
        else:
            mp+=1
    return print("5 multipli comuni ale lui",a," si ",b," sunt=",multiplii)
cinci_multipli(a,b)

def comune(x,y):
    return list (set(str(x)).intersection(set(str(y))))
print("Cifrele care se contin in ambele numere :",comune(a,b))

def cifrediferite(x,y):
    return list(set(str(a)).difference(set(str(b))))
print("Cifrele care sunt in  primul numar si care nu sunt in al doilea:", cifrediferite(a,b))

def prietenie(x,y):
    if len([i for i in range(1,x+1) if x%i==0])==len([i for i in range(1,y+1) if y%i==0]):
        return 'PRIETENIE'
print("Sunt prietene:",prietenie(a,b))
