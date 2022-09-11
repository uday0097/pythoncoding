#WAP to find basic arthimetic operations
a=int(input())
b=int(input())
add_1=a+b
sub_1=a-b
mul_1=a*b
print(add_1)
print(sub_1)
print(mul_1)
#WAP to find area of rectangle
length_rec=int(input())
breadth_rec=int(input())
area_rec=length_rec*breadth_rec
print(area_rec)
#WAP to find perimeter of rectangle
len_rec=int(input())
bre_rec=int(input())
per_rec=2*(len_rec+bre_rec)
print(per_rec)
#WAP to convert kilometers to meters
a=float(input())
b=a*1000
print(int(b))
#WAP to find length of string
a=input()
b=len(a)
print(b)
#WAP to find first three characters
a=input()
b=a[0:3]
print(b)
#WAP to compare first three characters
a=input()
b=input()
print(a[0:3]==b[0:3])
#WAP to find bith of the given numbers are positive and if atleast one of them is greater than 5
a=int(input())
b=int(input())
c=(a>0) and (b>0)
d=(a>5) or (b>5)
print(c and d)
#WAP to check two digits number is greater than 25  and first digit is greater than its second digit
a=int(input())
b=a>25
c=str(a)
d=c[0]>c[1]
print(b and d)
#WAP to print two strings in reverse order
a=input()
b=input()
print(b)
print("---")
print(a)
#WAP to print compare last three strings
a=input()
b=input()
c=len(a)
d=a[(c-3):c]
e=len(b)
f=b[(e-3):e]
print(d==f)
#WAP to print first letters
a=input()
b=input()
c=input()
print(a[0]+b[0]+c[0])
#WAP to find half string
a=input()
b=len(a)
c=a[(int(b/2)):]
print(c)
#WAP to print string repetition
a=input()
b=int(input())
c=(a+" ")*b
print(c)
#WAP to print first and last digit
a=int(input())
b=str(a)
print(int(b[0]))
print(int(b[3]))
#WAP to print elements in the range 10 to 20
a=int(input())
b=int(input())
c=int(input())
e=a>=10 and a<=20
f=b>=10 and b<=20
g=c>=10 and c<=20
h=e or f
print(h or g)
#WAP to print area and perimeter of a square
a=int(input())
area_1=a*a
per_1=4*a
print("Area of the square is: "+str(area_1))
print("Perimeter of the square is: "+str(per_1))
#WAP to print women population
a=int(input())
num_women=a*48/100
print(int(num_women))
#WAP to print year weeks and days
a=int(input())
b=int(a/365)
c=a%365
d=int(c/7)
e=c%7
print(b)
print(d)
print(e)


