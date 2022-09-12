#WAP to findDate Format - 2 Given seconds as input, write a program to print in D days H hours M minutes S seconds.Input
#Soluiton1:
n=int(input())
a=n/86400
b=n%86400
c=b/60
d=b%60
e=d%60
f=n/3600
g=n%3600
h=g/60
i=g%60

if n%86400==0:
    print(str(int(a))+" Days")
elif n%3600==0:
    print(str(int(f))+" Hours")
elif n>86400:
    print(str(int(a))+" Days"+" "+str(int(c))+" Hours"+" "+str(int(e))+" Minutes")
elif n<3600:
    print(str(int(h))+" Minutes"+" "+str(int(i))+" Seconds")
elif n>3600 and n<86400:
    print(str(int(f))+" Hours"+" "+str(int(h))+" Minutes"+" "+str(int(i))+" Seconds")
#Solution2:
totalSeconds = int(input())

secondsPerMinute = 60
secondsPerHour = 60 * secondsPerMinute
secondsPerDay = 24 * secondsPerHour

days = totalSeconds // secondsPerDay
hours = (totalSeconds - days * secondsPerDay) // secondsPerHour
minutes = (totalSeconds - days * secondsPerDay - hours * secondsPerHour) // secondsPerMinute
seconds = totalSeconds - days * secondsPerDay - hours * secondsPerHour - minutes * secondsPerMinute

if days > 0:
    print(days, 'Days', end=' ')
if hours > 0:
    print(hours, 'Hours', end=' ')
if minutes > 0:
    print(minutes, 'Minutes', end=' ')
if seconds > 0:
    print(seconds, 'Seconds', end=' ')
print()   
#WAP for product 
#WAP to find factorial
#WAP to find greater of 4 numbers
#Solution1:
numbers=[]
for i in range(0,4):
    number=int(input())
    numbers.append(number)
print(max(numbers))
#solution 2
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b:
    if a>c:
        if a>d:
            print(a)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)
else:
    if b>c:
        if b>d:
            print(b)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)

#WAP to print following pattern
n = int(input())
for i in range(n-1):
    print(' '*(n-1-i),'/',' '*i,'|',sep ='')
print('/','_'*(n-1),'|',sep ='')   
#sol:2
n = int(input())
for i in range(n):
	print(' ' * (n - i) + '/', end = '')
	if i < n-1:
		print(' ' * i, end = '')
	else:
		print('_' * i, end = '')
	print('|')
    
    
    