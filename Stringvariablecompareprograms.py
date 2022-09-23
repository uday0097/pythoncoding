#WAP to print temparature conversions
t=input()
s=t[-1]
t=t[0:len(t)-1]
t=float(t)
#celsius
if s=="C":
    f=(9/5)*t+32
    k=t+273
    print(str(round(t,2))+"C")
    print(str(round(f,2))+"F")
    print(str(round(k,2))+"K")
elif s=="F":
    c=((t)-32)*(5/9)
    k=c+273
    print(str(round(c,2))+"C")
    print(str(round(t,2))+"F")
    print(str(round(k,2))+"K")
elif s=="K":
    c=(t)-273
    f=(9/5)*int(c) + 32
    print(str(round(c,2))+"C")
    print(str(round(f,2))+"F")
    print(str(round(t,2))+"K")
#WAP to print sum of n terms in harmonic series
n=int(input())
sum=0
for i in range(1,(n+1)):
    sum=sum+(1/i)
print(round(sum,2))
#WAp to print diamond
n=int(input())
for i in range(0,(n)):
    dots=". "*(n-i-1)
    zeros="0 "*(2*i+1)
    print(dots+zeros+dots)
for j in range(1,n):
    dots=". "*j
    zeros="0 "*(2*n-((2*j)+1))
    print(dots+zeros+dots)
#WAP to print hollow diamond
n=int(input())
left_space=" "*(n-1)
print(left_space+chr(65))
hollow_space=-1
for char in range(1,(n)):
    for j in range((65+char),(66+char)):
        left_space=" "*(n-char-1)
        hollow_space=hollow_space+2
        print(left_space+chr(j)+" "*hollow_space+chr(j))
for char in range(1,(n-1)):
    for j in range((64+n-char),(65+n-char)):
        left_space=" "*char
        hollow_space=hollow_space-2
        print(left_space+chr(j)+" "*hollow_space+chr(j))
left_space=" "*(n-1)
print(left_space+chr(65))
#WAP to print root of quadratic equation
a=int(input())
b=int(input())
c=int(input())
r1=(-1*b+(b**2-4*a*c)**0.5)/(2*a)
r2=(-1*b-1*(b**2-4*a*c)**0.5)/(2*a)
print(round(r1,2))
print(round(r2,2))
#WAP to print replace character of sentence
n=input()
y=""
for char in n:
    if char !=" ":
        x=ord(char)+1
        y=y+chr(x)
    elif char==" ":
        y=y+" "
print(y)
#WAP to print cumulative sum
n=int(input())
sum=0
for i in range(1,(n+1)):
    num=int(input())
    sum=sum+num
    print(sum)
#WAP to print cumulative average
n=int(input())
sum=0
for i in range(1,(n+1)):
    num=int(input())
    sum=sum+num
    avg=sum/i
    print(round(avg,3))
#WAP to print double character
n=input()
x=""
for char in n:
    x=x+(char)*2
print(x)
#WAP to print subsequence in a string
n=input()
m=input()
sub_seq=0
for char in n:
    if char==m[sub_seq]:
        sub_seq+=1
    if sub_seq==len(m):
        break
if sub_seq==len(m):
    print("Yes")
else:
    print("No")
#WAP to find number pyramid
n = int(input())
for i in range(1, n+1):
    spaces = " "*(n - i)
    left_nums = ""
    right_nums = ""
    for j in range(1, i+1):
        left_nums = str(j) + left_nums
        right_nums = right_nums + str(j)
    print(spaces + left_nums + right_nums[1:])
#WAP to print Hyphenate letters
w=input()
x=""
for char in w:
    x=x+char+"-"
y=x.strip("-")
print(y)
#WAP to print maximum of each input
n=int(input())
maxi=0
for i in range(0,n):
    num=int(input())
    if num>maxi:
        maxi=num
    print(maxi)
#WAP to find diamond crystal
n=int(input())
for i in range(1,(n+1)):
    for j in range(0,(i)):
        left_space="  "*j
        right_space=" "*(n-i)
    print(right_space+"/"+left_space+"\\")
for i in range(1,(n+1)):
    for j in range(0,i):
        left_space="  "*(n-i)
        right_space=" "*j
    print(right_space+"\\"+left_space+"/")    



























