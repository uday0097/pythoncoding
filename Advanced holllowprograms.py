#WAP to print pythagoran triplets
l=int(input())
count=0
for a in range(1,(l+1)):
    for b in range(1,(l+1)):
        for c in range(1,(l+1)):
            if a<b and b<c:
                x=a**2
                y=b**2
                z=c**2
                if ((x+y)==z):
                    count=count+1
print(count)
#WAP to print indivisible numbers
n=int(input())
count=0
for i in range(1,(n+1)):
    is_divisible="False"
    for j in range(2,11):
        if i%j==0:
            is_divisible="True"
    if is_divisible=="False":
        count=count+1
print(count)
#WAP to print half pyramid 3
n=int(input())
k=int(input())
for i in range(0,k):
    sum=""
    for j in range(n,(n+i+1)):
        sum=sum+str(n)+" "
        n=n+1
    print(sum)
#WAP to print half pyramid 4
n=int(input())
k=int(input())
for i in range(1,(k+1)):
    sum=""
    for j in range(n,(n+i)):
        sum=sum+str(int(n+(k*(k+1)/2)-1))+" "
        n=n-1
    print(sum)
#WAP to find GCD
m =int(input())
n=int(input())
for i in range(1,(n+1)):
    if m%i==0 and n%i==0:
        Gre_com=i
print(Gre_com)
#WAP to print LCM
m=int(input())
n=int(input())
if m>n:
    greater=m
else:
    greater=n
lcm_find=False
for i in range(greater,(m*n)+1):
    if not lcm_find:
        if (i%m==0) and (i%n==0):
            lcm_find=True
            lcm=i
print(lcm)
#WAP to print full pyramid 2
n=int(input())
for i in range(1,(n+1)):
    space=""
    re_space=" "*(n-i)
    for j in range(1,(i+1)):
        space=space+str(j)+" "
    print(re_space+space)
#WAP to print inerted half pyramid 2
n=int(input())
for i in range(0,n):
    sum="* "*(n-i)
    print(sum)
#WAP to print inverted full pyramid
n=int(input())
for i in range(0,n):
    pattern=" "*i+"* "*(n-i)+" "*i
    print(pattern)
#WAP to print inverted full pyramid 2
n=int(input())
for i in range(0,(n)):
    sum=""
    for j in range(1,(n-i+1)):
        sum=sum+str(j)+" "
        pattern=" "*i+sum+" "*i
    print(pattern)
#WAP to print hollow half pyramid 1
n=int(input())
for i in range(1,n+1):
    if i>1 and i<n:
        print("* "+"  "*(i-2)+"* ")
    else:
        print("* "*i)
#WAP to print hallow inverted half pyramid 1
n=int(input())
for i in range(1,n+1):
    r=n-(i-1)
    if r>1 and r<n:
        print("* "+"  "*(r-2)+"* ")
    else:
        print("* "*r)
#WAP to print hollow half pyramid 2
n = int(input())
for i in range(1, n+1):
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i - 2)
        numbers = "1 " + hollow_spaces + (str(i) + " ")
        print(numbers)
    else:
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers + (str(j) + " ")
        print(numbers)
#WAP to print hollow inverted half pyramid 2
n = int(input())
for row in range(1, n+1):
    i = n - (row - 1)
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i - 2)
        numbers = "1 " + hollow_spaces + (str(i) + " ")
        print(numbers)
    else:
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers + str(j) + " "
        print(numbers)
#WAP to find hollow full pyramid 1
n = int(input()) 
for i in range(1, n+1):
    left_spaces = " " * (n - i)
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i-2)
        stars = "* " + hollow_spaces + "* "
        print(left_spaces + stars)
    else:
        stars = "* " * i
        print(left_spaces + stars)
#WAP to print hallow inverted full pyramid 1
n = int(input())

for row in range(1, n+1):
    i = n - (row -1)
    left_spaces = (" " * (row - 1))
    if (i >= 2) and (i < n):
        hollow = ("  " * (i - 2))
        numbers = "* " + hollow +"* "
        print(left_spaces + numbers)
    else:
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers +"* "
        print(left_spaces + numbers)
#WAP to find hollow full pyramid 2  
n = int(input()) 
for i in range(1, n+1):
    left_spaces = " " * (n - i)
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i-2)
        stars = "1 " + hollow_spaces + (str(i)+"")
        print(left_spaces + stars)
    else:
        
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers + (str(j) + " ")
        print(left_spaces + numbers)
#WAP to find hollow inverted full pyramid 2
n = int(input())

for row in range(1, n+1):
    i = n - (row -1)
    left_spaces = (" " * (row - 1))
    if (i > 2) and (i < n):
        hollow = ("  " * (i - 2))
        numbers = "1 " + hollow + (str(i) + " ")
        print(left_spaces + numbers)
    
    else:
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers + (str(j) + " ")
        print(left_spaces + numbers)
          
    
    


































































