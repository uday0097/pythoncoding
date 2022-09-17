#WAP to find number diamond
n=int(input())
for i in range(1,(n+1)):
    space=""
    re_space=" "*(n-i)
    for j in range(1,(i+1)):
        space=space+str(j)+" "
    print(re_space+space)
for i in range(1,(n)):
    sum=""
    for j in range(1,(n-i+1)):
        sum=sum+str(j)+" "
        pattern=" "*i+sum+" "*i
    print(pattern)
#WAP to find shaded Diamond
n=int(input())
for i in range(1,(n+1)):
    space=""
    re_space=" "*(n-i)
    pattern="* "*(i)
    print(re_space+pattern)
for row in range(1, n):
    i = n - (row)
    left_spaces = (" " * (row))
    if (i > 2) and (i < n):
        hollow = ("  " * (i - 2))
        numbers = "* " + hollow +"* "
        print(left_spaces + numbers)
    else:
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers +"* "
        print(left_spaces + numbers)
#WAP to print solid half diamond
n=int(input())
for i in range(1,(2*n)):
    if i<=n:
        for j in range(1,i+1):
            star="* "*j
        print(star)
    elif i>n:
        for j in range(i,(2*n)):
            star="* "*(2*n-i)
        print(star)
#WAP to print butterfly
n=int(input())
for i in range(1,(n+1)):
    star="* "*i
    hallow="  "*(2*(n-i))
    print(star+hallow+star)
for i in range(n):
    star="* "*(n-i)
    hallow="  "*(2*i)
    print(star+hallow+star)
#WAP to print full pyramid 3
n=int(input())
for i in range(1,(n+1)):
    for j in range(1,(2*n+1)):
        k=(1+2*(i-1))
        zeros=(str(0)+" ")*(n-i)
        ones=(str(1)+" ")*k
        pattern=zeros+ones+zeros
    print(pattern)
#WAP to print digit 8
n=int(input())
for i in range(1,(n+2)):
    if i==1 or i==(n+1):
        pattern="* "*n
        print(pattern)
    else:
        pattern="  "*(n-2)
        print("* "+pattern+"* ")
for i in range(1,(n+1)):
    if i==n:
        print("* "*n)
    else:
        pattern="  "*(n-2)
        print("* "+pattern+"* ")
#WAP to print kth largest factor
n=int(input())
k=int(input())
count=0
fact=n
k_factor=False
for i in range(1,(n+1)):
    if not k_factor:
        if (n%fact)==0:
            count=count+1
        if count==k:
            print(fact)
            k_factor=True
    fact=fact-1
#WAP to print digit 9
n=int(input())
for i in range(1,(n+1)):
    if i==1 or i==n:
        print("* "*n)
    else:
        space="  "*(n-2)
        print("* "+space+"* ")
for i in range(1,n):
    if i==(n-1):
        print("* "*n)
    else:
        space="  "*(n-1)
        print(space+"* ")
#WAP to print Pyramid
n=int(input())
for i in range(1,(n+1)):
    for j in range(1,(2*n+1)):
        k=(1+2*(i-1))
        dot=". "*(n-i)
        zero="0 "*k
    print(dot+zero+dot)
#WAP to print armstrong of given range
a=int(input())
b=int(input())
result=False
for i in range(a,(b+1)):
    for j in range(a,(i+1)):
        num=str(j)
        l=len(num)
        sum=0
        for k in range(0,l):
            
            
            sum=(int(num[k]))**l+sum
    sng=""
    if sum==j:
        result=True
        sng=sng+str(sum)+" "
        print(sng,end="")
if not result:
    print(-1)
#WAP to print W pattern
n=int(input())
for i in range(1,(n+1)):
    if i==1:
        print("* "*(2*n-1))
    for j in range(1,(2*n)):
        first_half="* "*(n-i)
        second_half="* "*(n-i)
        hallow=" "*(i)
        hallow_mid="  "*(i-1)
    print(hallow+first_half+hallow_mid+second_half+hallow)


































