#WAP to print first prime number in range
m=int(input())
n=int(input())
if not (m>1):
    m=2
non_prime=True
for i in range(m,(n+1)):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)
        non_prime=False
        break
if non_prime:
    print("No prime numbers in the given range")
#WAP to print first negative number in range
n=int(input())
for i in range(1,(n+1)):
    b=int(input())
    if b<0:
        print(b)
        break
#WAP to print first uppercase
a=input()
for char in a:
    if char==char.upper():
        if not char.isdigit():
            print(char)
            break
#WAP to print first word in uppercase
n=input()
first_index=0
for char in  n:
    if char==" ":
        break
    else:
        first_index=first_index+1
fir_wor=n[:first_index]
upca_word=fir_wor.upper()
new_sen=upca_word+n[first_index:]
print(new_sen)
#WAP to print prime or not
n = int(input())
is_prime = True
for i in range(2, n):
    if (n % i) == 0:
        is_prime = False
        break
print(is_prime)
#WAP to print kth largest factor of n
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
            break
            k_factor=True
    fact=fact-1
if count<k:
    print(1)
#WAP to print composite number in the range
m=int(input())
n=int(input())
for i in range(m,(n+1)):
    num=0
    for j in range(1,i):
        if i%j==0:
            num=j
    if num>1:
        print(i)
#WAP to print first prime number
n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    isPrime=True
    if number > 1:
        for j in range(2, number):
            if (number % j) == 0:
                isPrime=False
                break
        if isPrime==True:
            numbers.append(number)
                
print(str(numbers[0]))
#WAP to print multiple of 5 break
n=int(input())
for i in range(0,n):
    number = int(input())
    if number % 5 != 0:
      print(number)
    else:
       break
#WAP to print multiple of 3 continue
n=int(input())
for i in range(0,n):
    number = int(input())
    if number % 3 == 0:
      print(number)
      continue
#WAP to print even and odds
m=int(input())
n=int(input())
count=0
odd=0
for i in range(m,(n+1)):
    if i%2==0:
        count=count+1
        
    elif i%2==1:
        odd=odd+1
print(odd)
print(count)
#WAP ro print special characters vowel and consonants
a=input()
b=a.upper()
count=0
cons=0
for char in b:
    if (char=="A"or char=="E" or char=="I" or char=="O" or char=="U"):
        count=count+1
    elif char==" ":
        pass
    
    else:
        cons=cons+1
print(count)
print(cons)
#WAP to change one color
n=input()
g=0
r=0
for char in n:
    if char=="G":
        g=g+1
    else:
        r=r+1
if g>r:
    print(r)
else:
    print(g)
#WAP to print alphabetic symbols
n=int(input())
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=""
for i in range(0,n):
    s=s+string[i]+" "
    print(s)
#WAP to print right triangle
n=int(input())
for i in range(1,(n+1)):
    s=""
    k=""
    for j in range(1,(i+1)):
        s=s+(str(j))
    for j in range(i-1,0,-1):
        k=k+str(j)
    print(s+k)
#WAP to print case conversion
n=input()
main=True
for ch in n:
    if main:
        res=ch.lower()
    elif ch.isupper():
        res=res+"_"+ch.lower()
    else:
        res=res+ch
    main=False
print(res)
#WAP to print sum of non primes
n = int(input())
sum=0
for i in range(n):
    count=0
    index = int(input())
    if index > 1:
        for j in range(2,index):
            if index % j == 0:
                count=count+1
        if count>=1:
            sum=sum+index
print(sum)
#WAP to print sandglass star
n=int(input())
for i in range(0,n):
    pattern=" "*i+"* "*(n-i)+" "*i
    print(pattern)
for i in range(1,n):
    pattern=" "*(n-i-1)+"* "*(i+1)+" "*(n-i-1)
    print(pattern)



















































    
    





















































