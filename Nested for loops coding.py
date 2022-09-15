#WAP to find sum of even numbers
n=int(input())
sum=0
for i in range(1,(n+1)):
    if i%2==0:
        sum=sum+i
print(sum)
#WAP to find sum of odd numbers
n=int(input())
sum=0
for i in range(1,(n+1)):
    if i%2==1:
        sum=sum+i
print(sum)
#WAP to find composite number
n=int(input())
count=0
for i in range(2,n):
    if n%i==0:
        count=count+1
if count>=1:
    print("True")
else:
    print("False")
#WAP to print stripped rectangle
m=int(input())
n=int(input())
for i in range(1,(m+1)):
    if i%2==1:
        sym=("+ ")*n
    else:
        sym=("- ")*n
    print(sym)
#WAP to find Hollow Rectangle 2
m=int(input())
n=int(input())
for i in range(1,(m+3)):
    if i==1 or i==(m+2):
        sym="+"+"-"*n+"+"
    else:
        sym="|"+" "*n+"|"
    print(sym)
#WAP to print prime numbers from 1 to n
n=int(input())
for num in range(2,(n+1)):
    prime=0
    for i in range(2,num):
        if (num%i)==0:
            prime=prime+1
    if prime==0:
        print(num)
#WAP to print prime numbers from m to n
m=int(input())
n=int(input())
for i in range(m,(n+1)):
    prime=0
    for j in range(2,i):
        if i%j==0:
            prime=prime+1
    if prime==0:
        print(i)
#WAP to print half pyramid
n=int(input())
for i in range(1,(n+1)):
    sum=""
    for j in range(1,(i+1)):
        sum=sum+(str(j)+" ")
    print(sum)
#WAP to print inverted half pyramid
n=int(input())
for i in range(1,(n+1)):
    sum=""
    for j in range(1,(n-i+2)):
        sum=sum+(str(j)+" ")
    print(sum)
#WAP to print numbers in square pattern 3
n=int(input())
num=1
for i in range(1,(n+1)):
    sum=""
    for j in range(1,(n+1)):
        sum=sum+(str(num))+" "
        num=num+1
    print(sum)
#WAP to print numbers in rectangular pattern 3
m=int(input())
n=int(input())
num=1
for i in range(1,(m+1)):
    sum=""
    for j in range(1,(n+1)):
        sum=sum+(str(num))+" "
        num=num+1
    print(sum)
#WAP to print half pyramid-2
n=int(input())
num=1
for i in range(1,(n+1)):
    sum=""
    for j in range(1,i+1):
        sum=sum+(str(num))+" "
        num=num+1
    print(sum)
#WAP to print inverted half pyramid
n = int(input())

for row_num in range(0,n):
    row_output = ""
    seq_num = n-row_num
    while seq_num > 0:
        row_output = row_output + str(seq_num)
        seq_num = seq_num - 1
    print(row_output)




























































































