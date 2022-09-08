#Write a program to print integers from 1 to the given integer(N)
#example input is 3 then ouput is 1 2 3
n=int(input())
for i in range(0,n):
    i=i+1
    print(i)
#WAP to print the integers from M to N
#example is input 2 and 6 ouput is 23456
m=int(input())
n=int(input())
a=0
for i in range(m,(n+1)):
    i=i+a
    print(i)
#WAP to print solid square using *
n=int(input())
for i in range(0,n):
    i="* "*n
    print(i)
#WAP to print solid rectangle of m and n
m=int(input())
n=int(input())
for i in range(0,m):
    i="* "*n
    print(i)
#WAP to print solid right angled traingle
n=int(input())
for i in range(1,(n+1)):
    i="* "*i
    print(i)
#WAP to print sum of first N natural numbers
n=int(input())
sum=0
for i in range(1,(n+1)):
    sum=i+sum
print(sum)
#WAP to read n inputs and print them example is 3 80 40 30 then output is 80 40 30
n=int(input())
for i in range(0,n):
    num=int(input())
    print(num)
#WAP to read N inputs and print sum of them
n=int(input())
sum=0
for i in range(0,n):
    num=int(input())
    sum=num+sum
print(sum)
#WAP to print the pattern 
a = input()
len_of_a = len(a)
b = a[0]
for i in range(1, len_of_a):
    b = b + "-" + a[i]
print(b)
#Advanced level for loop programs:
#WAP to print integer from n to 1
n=int(input())
for i in range(0,n):
    c=n-i
    print(c)
#WAP to read input and print product of input
n=int(input())
mul=1
for i in range(0,n):
    num=int(input())
    mul=mul*num
print(mul)
#WAP to print solid rectangle pattern
m=int(input())
n=int(input())
for i in range(0,m):
    c="+ "*n
    print(c)
#WAP to print the pattern
n=int(input())
for i in range(1,(n+1)):
    c="* "*i
    print(c)
for j in range(1,(n+1)):
    c="* "*j
    print(c)