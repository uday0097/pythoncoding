#WAP to print sum of numbers
a=input()
a=int(a)
b=input()
b=int(b)
c=a+b
print(c)
#WAP to print character present at nth in given word m
a=input()
b=int(input())
c=a[b]
print(c)
#WAP to find last character of given word
a=input()
b=len(a)
c=a[b-1]
print(c)
#WAP to print half string
a=input()
b=len(a)
c_index=int(b/2)
d=a[0:c_index]
print(d)
#WAP to print given word n times
a=input()
b=int(input())
c=a*b
print(c)
#WAP to print last three charcters n times
a=input()
b=int(input())
c=len(a)
d=a[c-3:c]
e=d*b
print(e)
#WAP to print sum of three digits of a given digit
a=input()
b=int(a[0])+int(a[1])+int(a[2])
print(b)
