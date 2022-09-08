#WAP to print integer from 1 to n
n=int(input())
count=0
a=0
while count<n:
    a=a+1
    print(a)
    count=count+1
#WAP to print integers from m to n
m=int(input())
n=int(input())
while (m<=n):
    print(m)
    m=m+1
#WAP to print solid square
a=int(input())
count=0
while count<a:
    seq="* "*a
    print(seq)
    count=count+1
#WAP to print solid rectangle
a=int(input())
b=int(input())
count=0
while count<a:
    print("* "*b)
    count=count+1
#WAP to print solid right angled traingle
a=int(input())
count=1
while count<=a:
    print("* "*count)
    count=count+1
#WAP to print sum of n numbers
a=int(input())
count=1
while count<=a:
    print("* "*count)
    count=count+1
#WAP to read n inputs and print them
a=int(input())
count=0
while count<a:
    num=int(input())
    print(num)
    count=count+1
#WAP to print sum of given numbers
a=int(input())
count=0
sum=0
while count<a:
    num=int(input())
    sum=num+sum
    count=count+1
print(sum)
#WAP to print python
a = input()
counter = 0
length_of_a = len(a)
while counter < (length_of_a):
    print(a[counter])
    counter = (counter + 1)
#WAP to print integers from n to 1
n=int(input())
count=0
while count<n:
    print(n)
    n=n-1
#WAP to print solid rectangle
m=int(input())
n=int(input())
count=0
while count<m:
    print("+ "*n)
    count=count+1
#WAP to print product of inputs
a=int(input())
count=0
mul=1
while count<a:
    num=int(input())
    mul=num*mul
    count=count+1
print(mul)
#WAP to print the pattern
a=int(input())
count=1
count_1=1
while count<=a:
    print("* "*count)
    count=count+1
while count_1<=a:
    print("* "*count_1)
    count_1=count_1+1