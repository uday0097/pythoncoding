#WAP to find factorial of N
n=int(input())
fact=1
for i in range(1,(n+1)):
    fact=fact*i
print(fact)
#WAP to print sum of numbers from n to m
n=int(input())
m=int(input())
sum=0
for i in range(n,(m+1)):
    sum=sum+i
print(sum)
#WAP to find sum of first N even  numbers
n=int(input())
sum=0
for i in range(1,(n+1)):
    if i%2==0:
        sum=i+sum
print(sum)
#WAP to find sum of first N odd numbers
n=int(input())
sum=0
for i in range(1,(n+1)):
    if i%2!=0:
        sum=sum+i
print(sum)
#WAP to find sum of even numbers from n to m
n=int(input())
m=int(input())
sum=0
for i in range(n,(m+1)):
    if i%2==0:
        sum=i+sum
print(sum)
#WAP sum of odd numbers from n to m
n=int(input())
m=int(input())
sum=0
for i in range(n,(m+1)):
    if i%2!=0:
        sum=sum+i
print(sum)
#WAP to find sum of numbers divisible by T
t=int(input())
m=int(input())
n=int(input())
sum=0
for i in range(m,(n+1)):
    if i%t==0:
        sum=i+sum
print(sum)
#WAP to find sum of squares
n=int(input())
sum=0
for i in range(1,(n+1)):
    sum=sum+(i**2)
print(sum)
#WAP to find sum of cubes
n=int(input())
sum=0
for i in range(1,(n+1)):
    sum=sum+(i**3)
print(sum)
#WAP find sum and avg of 10 numbers
total=0
for i in range(10):
    number=int(input())
    total=total+number
    average=(total)/10
print(total)
print(average)
#WAP to find sum of digits
a=input()
b=len(a)
sum=0
for i in range(0,b):
    sum=sum+int(a[i])
print(sum)
#WAP to find power of n with m with out using power operator
n=int(input())
m=int(input())
power=1
for i in range(1,(m+1)):
    power=power*n
print(power)
#WAP to find sum of kth power of first n natural numbers
n=int(input())
k=int(input())
sum=0
for i in range(1,(n+1)):
    sum=sum+(i**k)
print(sum)
#WAP to find product of numbers from n to m
n=int(input())
m=int(input())
mul=1
for i in range(n,(m+1)):
    mul=mul*i
print(mul)
#WAP to find count of no of digits from 1 to n
n=int(input())
sum=0
for i in range(1,(n+1)):
    digits=len(str(i))
    sum=sum+digits
print(sum)