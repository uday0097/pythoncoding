#WAP to find relation between two numbers
a=int(input())
b=int(input())
if a>b:
    print("A > B")
elif a<b:
    print("A < B")
else:
    print("A == B")
#WAP to find get grades
a=float(input())
if a>85:
    print("A")
elif (a>70) and (a<=85):
    print("B")
elif (a>=60) and (a<=70):
    print("C")
elif a<60:
    print("F")
#WAP to find greeting message
a=int(input())
if (a>=4) and (a<12):
    print("Good Morning")
elif (a>=12) and (a<16):
    print("Good Afternoon")
elif (a>=16) and (a<20):
    print("Good Evening")
elif (a>=20) or (a<4):
    print("Good Night")
#WAP to find name of polygon
a=int(input())
if a<3:
    print("Not Polygon")
elif a==3:
    print("Triangle")
elif a==4:
    print("Quadrilateral")
elif a==5:
    print("Pentagon")
elif a>5:
    print("Big Polygon")
#WAP to find get season
a=int(input())
if a==1 or a==11 or a==12:
    print("Winter")
elif a==2 or a==3:
    print("Spring")
elif a==4 or a==5 or a==6:
    print("Summer")
elif a==7 or a==8:
    print("Rainy")
elif a==9 or a==10:
    print("Autumn")
#WAP to find permission to attend exam
a=input()
b=input()
c=len(a)
d=int((a[0:(c-1)]))
if d>=75:
    print("Allowed to write exam")
elif (d<75) and b=="Y":
    print("Allowed to write exam")
elif (d<75) and b=="N":
    print("Cannot write exam")
#WAP to find electricity bill
a=int(input())
if a<=50:
    b=a*2
    sur_charge=b*0.2
    total_charge=b+sur_charge
    print(total_charge)
elif a>=51 and a<=150:
    b=(2*50)+3*(a-50)
    sur_charge=b*0.2
    total_charge=b+sur_charge
    print(total_charge)
elif a>=151 and a<=250:
    b=(2*50)+(3*100)+5*(a-150)
    sur_charge=b*0.2
    total_charge=b+sur_charge
    print(total_charge)
elif a>=251:
    b=(2*50)+(3*100)+(5*100)+8*(a-250)
    sur_charge=b*0.2
    total_charge=b+sur_charge
    print(total_charge)
#WAP to find day name
a=int(input())
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
#WAP to find relation between two numbers 2
a=int(input())
b=int(input())
if a==b:
    print("A == B")
elif a>b:
    print("A > B")
elif a<b:
    print("A < B")
#WAP to find profit or loss
a=int(input())
b=int(input())
if a==b:
    print("No Profit - No Loss")
elif a>b:
    print("Loss")
elif a<b:
    print("Profit")
#WAP to find leap year
a=int(input())
if (a%100==0) and (a%400==0):
    print("True")
elif (a%4==0) and (a%100!=0):
    print("True")
else:
    print("False")
#WAP to find weather condition
a=float(input())
if a<0:
    print("Freezing weather")
elif 0<=a<10:
    print("Very Cold weather")
elif 10<=a<20:
    print("Cold weather")
elif 20<=a<30:
    print("Normal")
elif 30<=a<40:
    print("Hot")
elif a>=40:
    print("Very Hot")
#WAP to find sum of digits 2
a=int(input())
b=str(a)
c=len(b)
if 0<=a<=9:
    print(int(b))
elif 10<=a<=99:
    d=int(b[c-c])+int(b[c-1])
    print(int(d))
elif 100<=a<=999:
    d=int(b[c-c])+int(b[c-2])+int(b[c-1])
    print(int(d))
elif 1000<=a<=9999:
    d=int(b[c-c])+int(b[c-3])+int(b[c-2])+int(b[c-1])
    print(int(d))
elif a==10000:
    d=int(b[c-c])+int(b[c-4])+int(b[c-3])+int(b[c-2])+int(b[c-1])
    print(int(d))
#Simple calculator
a=input()
b=int(input())
c=int(input())
if a=="+":
    d=b+c
    print(d)
elif a=="-":
    d=b-c
    print(d)
elif a=="*":
    d=b*c
    print(d)
elif a=="/":
    d=b/c
    print(d)
elif a=="%":
    d=b%c
    print(d)
#WAP to find denominations
a=int(input())
b=a/100
print("100:"+str(int(b)))
c=a%100
d=c/50
print("50:"+str(int(d)))
e=c%50
f=e/10
print("10:"+str(int(f)))
g=e%10
print("1:"+str(int(g)))
#WAP to find max no of hand shakes
a=int(input())
b=(a-1)*a
c=b/2
print(int(c))
#WAP to find denominations-2
a=int(input())
b=a/100
print("100 Notes: "+str(int(b)))
c=a%100
e=c/50
print("50 Notes: "+str(int(e)))
f=c%50
g=f/20
print("20 Notes: "+str(int(g)))
h=f%20
i=h/10
print("10 Notes: "+str(int(i)))
#WAP to find denominations-4
a=int(input())
b=a/2000
c=a%2000
d=c/500
e=c%500
f=e/200
g=e%200
h=g/50
i=g%50
j=i/20
k=i%20
l=k/5
m=k%5
n=m/2
o=m%2
p=o/1
print("2000:"+str(int(b))+" "+"500:"+str(int(d))+" "+"200:"+str(int(f))+" "+"50:"+str(int(h))+" "+"20:"+str(int(j))+" "+"5:"+str(int(l))+" "+"2:"+str(int(n))+" "+"1:"+str(int(p)))
#WAP to find denominations 3
a=int(input())
b=a/500
c=a%500
d=c/50
e=c%50
f=e/10
g=e%10
h=g/1
print("500: "+str(int(b))+" "+"50: "+str(int(d))+" "+"10: "+str(int(f))+" "+"1: "+str(int(h)))
#WAP to find day name -2
a=input()
b=int(input())
if a=="Sunday":
    day=0
elif a=="Monday":
    day=1
elif a=="Tuesday":
    day=2
elif a=="Wednesday":
    day=3
elif a=="Thursday":
    day=4
elif a=="Friday":
    day=5
elif a=="Saturday":
    day=6
as_day=day+b-1
as_day=as_day%7
if as_day==0:
    print("Sunday")
elif as_day==1:
    print("Monday")
elif as_day==2:
    print("Tuesday")
elif as_day==3:
    print("Wednesday")
elif as_day==4:
    print("Thursday")
elif as_day==5:
    print("Friday")
elif as_day==6:
    print("Saturday")
#WAP to find string repetition
a=input()
b=int(input())
c=a+" "
d=c*b
print(d)
#WAP to find first place
a=int(input())
b=str(a)
c=len(b)
d=b[c-1]
print(int(d))
#WAP to find day conversion
a=int(input())
b=a/365
c=a%365
d=c/7
e=c%7
print(str(int(b))+" years"+" "+str(int(d))+" weeks"+" "+str(int(e))+" days")
#WAP to find finding difference
a=int(input())
b=int(input())
c=a-b
if c>0:
    print(c)
elif c<0:
    c=-1*c
    print(c)
#WAP to find hand game
a=input()
b=input()
if a==b:
    print("Tie")
elif a=="Paper" and b=="Rock":
    print("Abhinav Wins")
elif a=="Rock" and b=="Paper":
    print("Anjali Wins")
elif a=="Scissors" and b=="Paper":
    print("Abhinav Wins")
elif a=="Paper" and b=="Scissors":
    print("Anjali Wins")
elif a=="Rock" and b=="Scissors":
    print("Abhinav Wins")
elif a=="Scissors" and b=="Rock":
    print("Anjali Wins")
#WAP to find Name of month
a=int(input())
if a<1 or a>12:
    print("Invalid Month Number")
elif a==1:
    print("January")
elif a==2:
    print("February")
elif a==3:
    print("March")
elif a==4:
    print("April")
elif a==5:
    print("May")
elif a==6:
    print("June")
elif a==7:
    print("July")
elif a==8:
    print("August")
elif a==9:
    print("September")
elif a==10:
    print("October")
elif a==11:
    print("November")
elif a==12:
    print("December")    
#WAP to find Triangles
a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print("Equilateral")
elif a==b or b==c:
    print("Isosceles")
elif a==b or a==c:
    print("Isosceles")
elif a!=b and b!=c:
    print("Scalene")
#WAP to find Denominations
a=int(input())
b=a/1000
print("1000:"+str(int(b)))
c=a%1000
d=c/500
print("500:"+str(int(d)))
e=c%500
f=e/100
print("100:"+str(int(f)))
g=e%100
h=g/50
print("50:"+str(int(h)))
i=g%50
j=i/20
print("20:"+str(int(j)))
k=i%20
l=k/5
print("5:"+str(int(l)))
m=k%5
print("1:"+str(int(m)))




















