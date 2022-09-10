#WAP to find multiplication table
n=int(input())
for i in range(1,11):
    mul=n*i
    print(str(n)+" "+"x "+str(i)+" = "+str(mul))
#WAP to find reverse of strings
n=input()
c=len(n)
a=""
for i in range(1,(c+1)):
    a=a+n[(c-i)]
print(a)
#WAP to find greatest of n numbers
n=int(input())
greater_num=n
for i in range(0,n):
    num=int(input())
    if num>greater_num:
        greater_num=num
print(greater_num)
#WAP to find smallest of n numbers
n=int(input())
first=int(input())
smal_num=first
for i in range((n-1)):
    num=int(input())
    if num<smal_num:
        smal_num=num
print(smal_num)
#WAP to find sum of series example 2+22 +222
n=int(input())
sum=0
for i in range(1,(n+1)):
    sum=int(str(2)*i)+sum
print(sum)
#WAP to print factors of a number
n=int(input())
for i in range(1,(n+1)):
    if (n%i==0):
        print(i)
#WAP to find sum of factors of a number
n=int(input())
sum=0
for i in range(1,(n+1)):
    if (n%i==0):
        sum=sum+i
print(sum)
#WAP to find perfect number
n=int(input())
sum=0
for i in range(1,n):
    if (n%i==0):
        sum=sum+i
if sum==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
#WAP to find Armstrong number
n=int(input())
a=str(n)
b=len(a)
sum=0
for i in range(0,b):
    sum=(int(a[i]))**b+sum
if sum==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
#WAP to find sum of the series example 1+11+111 
n=int(input())
sum=0
for i in range(1,(n+1)):
    sum=int(str(1)*i)+sum
print(sum)
#WAP to find perfect squares in a range
n=int(input())
m=int(input())
count=0
for i in range(n,(m+1)):
    if (int(i**0.5)==i**0.5):
        count=count+1
print(count)