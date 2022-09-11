#WAP to print given word without the character at given index
a=input()
b=int(input())
c=a[:b]
d=a[b+1:]
e=c+d
print(e)
#WAP to print validate passeord
a=input()
b=len(a)
if b>7:
    print("True")
else:
    print("False")
#WAP to print number between 25 and 75
a=int(input())
if a>25 and a<75:
    print("True")
else:
    print("False")
#WAP to print maskinf first and last
a=input()
b=len(a)
c=a[0]
d=a[b-1]
e=b-2
print(c+"*"*e+d)
#WAP to print exam result
a=int(input())
if a>50:
    print("PASS")
else:
    print("FAIL")
#WAP to print masking leaving first and last two
a=input()
b=len(a)
c=a[0:2]
d=a[b-2:b]
e=b-4
print(c+"*"*e+d)
#WAP to print eligibility1
m=int(input())
p=int(input())
c=int(input())
a=m+p+c
b=m>=70 and p>=60 and c>=60
if b or (a>=180):
    print("True")
else:
    print("False")
#WAP to print eligibility 2
m=int(input())
p=int(input())
c=int(input())
e=m+p>=100 or p+c>=100
a=e or m+c>=100
d=m+p+c
if a and d>=180:
    print("True")
else:
    print("False")
#WAP to print eligibility 3
m=int(input())
p=int(input())
c=int(input())
a=m+p
b=p+c
d=m+c
e=m>=35 and p>=35
f=e and c>=35
g=a>=90 or b>=90
h=g or d>=90
if f and h:
    print("True")
else:
    print("False")
#WAP to print eligibility 4
m=int(input())
p=int(input())
c=int(input())
a=m+p+c
b=m>=60 and p>=50
d=b and c>=45
e=d and a>=180
f=m+p
g=c+p
h=f>=120 or g>=110
if e or h:
    print("True")
else:
    print("False")
#WAP to print greatest among 2 numbers
a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)
#WAP to print equal numbers
a=int(input())
b=int(input())
if a==b:
    print("Equal")
else:
    print("Not Equal")
#WAP to print positive or negative
a=int(input())
if a>0:
    print("Positive")
if a==0:
    print("Zero")
if a<0:
    print("Negative")
#WAP for vote eligibility
a=int(input())
if a>=18:
    print("Eligible")
else:
    print("Not Eligible")
#WAP to find square or rectangle
a=int(input())
b=int(input())
if a==b:
    print("Square")
else:
    print("Rectangle")
#WAP to print bonus salary
a=int(input())
b=int(input())
if b>5:
    a=a*0.05
    print(a)
else:
    print("No Bonus")
#WAP to print valid triangle
a=int(input())
b=int(input())
c=int(input())
d=a+b+c
if d==180:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
#WAP to print valid triangle 2
a=int(input())
b=int(input())
c=int(input())
d=a+b>c and b+c>a
e=d and c+a>b
if d and e:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
#WAP to print lucky number
a=int(input())
b=int(input())
c=a+b
d=a-b
e=c==6 or d==6 
g=e or d==-6
f=a==6 or b==6
if g or f:
    print("Lucky")
else:
    print("Not Lucky")
#WAP to print greatest among 3 numbers
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)
if a==b and b==c:
    print(a)
#WAP to find honor student
a=int(input())
if a<10:
    print("HONOR STUDENT")
else:
    print("NORMAL STUDENT")
#WAP to find positive or negative
a=float(input())
if a<0:
    print("Negative")
else:
    print("Positive")
#WAP to printincrement the number
a=int(input())
if a>10:
    a=a+5
    print(a)
else:
    a=a+1
    print(a)
#WAP to find relation between numbers
a=int(input())
b=int(input())
if a<b:
    print("X < Y")
else:
    print("X >= Y")
#WAP to print sum or product
a=int(input())
b=int(input())
if a+b<10:
    c=a+b
    print(c)
else:
    c=a*b
    print(c)
#WAP to print smallest of 3 numbers
a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print(a)
if b<c and b<a:
    print(b)
if a==b and b<c:
    print(a)
if c<a and c<b:
    print(c)
if a==b and c==b:
    print(a)

#WAP to find even or odd
a=int(input())
if a%2==0:
    print("Even")
else:
    print("Odd")
#WAP to find special number
a=int(input())
b=str(a)
c=int(b[0])+int(b[1])
d=a%7
e= (c==7) or (d==0)
f=int(b[0])
g=int(b[1])
h= (f==7) or (g==7)
if h or e:
    print("Special Number")
else:
    print("Normal Number")
#WAP to find special eleven
a=int(input())
b=a%11
if b==0 or b==1:
    print("Special Eleven")
else:
    print("Normal Number")
#WAP to find lucky number 2
a=int(input())
if a%6==0:
    print("Number is divisible by 6")
elif a%3==0:
    
    print("Number is divisible by 3")
elif a%2==0:
    
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")
#WAP to find power of a number
a=int(input())
b=int(input())
c=a**b
print(c)
#WAP to print greatest among the powers
a=int(input())
b=int(input())
c=a**b
d=b**a
if c>d:
    print(c)
else:
    print(d)
#WAP to find lucky number 3
a=int(input())
b=a%9
c=str(a)
d=int(c[0])
e=int(c[1])
f=(d==9) or (e==9)
if b==0 or f:
    print("Lucky Number")
else:
    print("Unlucky Number")
#WAP to calulate double or triple
a=int(input())
if a%3==0:
    b=a*3
    print(b)
else:
    b=a*2
    print(b)
#WAP to find smallest remainder
a=int(input())
b=int(input())
c=a%b
d=b%a
if c<d:
    print(c)
else:
    print(d)
#WAP to print uncommon number
a=int(input())
b=a%2!=0 and a%3!=0
c=a%5!=0 and a%7!=0
if b and c:
    print("True")
else:
    print("False")
#WAP to compute hypotenuse
a=int(input())
b=int(input())
c=a**2
d=b**2
e=c+d
f=e**0.5
print(int(f))
#WAP to print 3 digit armstrong number
a=int(input())
b=str(a)
c=int(len(b))
d=(int(b[0]))**c
e=(int(b[1]))**c
f=(int(b[2]))**c
g=d+e+f
if g==a:
    print("True")
else:
    print("False")
























































