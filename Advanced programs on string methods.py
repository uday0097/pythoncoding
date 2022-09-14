#WAP to print word triangle
n=input()
b=len(n)
su_string=""
for i in range(0,b):
    su_string=su_string+n[i]
    print(su_string)
#WAP to shuffle String
n=input()
b=len(n)
shu_string=""
for i in range(b):
    index=int(input())
    shu_string=shu_string+n[index]
print(shu_string)
#WAP to print Prime number
n=int(input())
fact=0
for i in range(2,n):
    if (n%i)==0:
        fact=fact+1
if fact==0:
    print("Prime Number")
else:
    print("Not a Prime Number")
#WAP to print hollow rectangle
n=int(input())
m=int(input())
for i in range(1,(n+1)):
    if i==1:
        print("* "*(m))
    elif i==n:
        print("* "*(m))
    else:
        print("* "+"  "*(m-2)+"* ")
#WAP to print square pattern 1
n=int(input())
pattern=""
for i in range(1,(n+1)):
    pattern=pattern+str(i)+" "
for i in range(1,(n+1)):
    print(pattern)
#WAP to print square pattern 2
n=int(input())
for i in range(1,(n+1)):
    sub_string=(str(i)+" ")*n
    print(sub_string)
#WAP to print rectangle pattern 1
m=int(input())
n=int(input())
shu_string=""
for i in range(1,(n+1)):
    shu_string=shu_string+str(i)+" "
for i in range(1,(m+1)):
    print(shu_string)
#WAP to print rectangle pattern 2
m=int(input())
n=int(input())
for i in range(1,(m+1)):
    pattern=(str(i)+" ")*n
    print(pattern)
#WAP to print solid diamond
n=int(input())
b=n-1
for i in range(1,(n+1)):
    space=" "*b
    star="* "*i
    print(space+star)
    b=b-1
k=n-1
for i in range(1,(n)):
    star="* "*k
    space=" "*i
    print(space+star)
    k=k-1
#WAP to print pattern
n = int(input())

k = n-1
for i in range(1, n+1):
    spaces = " " * k
    stars = "* " * i
    print(spaces+stars)
    k = k - 1













































