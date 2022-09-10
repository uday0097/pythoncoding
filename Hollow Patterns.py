#WAP to print Hollow sqaure pattern
n=int(input())
for i in range(0,n):
    if (i==0) or (i==(n-1)):
        print("* "*n)
    else:
        n_hallow=("  "*(n-2))
        print("* "+n_hallow+"* ")
#WAP to find Hollow right triangle
n=int(input())
for i in range(0,n):
    if i==0:
        print("* "*n)
    elif i==(n-1):
        print("  "*(n-1)+"* ")
    else:
        left_space="  "*(i)
        hallow_space="  "*(n-i-2)
        print(left_space+"* "+hallow_space+"* ")
#WAP to find Hollow right triangle 2
n=int(input())
for i in range(0,n):
    if i==0:
        print("  "*(n-1)+"* ")
    elif i==(n-1):
        print("* "*n)
    else:
        left_space="  "*(n-i-1)
        hallow_space=("  "*(i-1))
        print(left_space+"* "+hallow_space+"* ")
#WAP to find Hollow right triangle 3
n=int(input())
for i in range(1,(n+2)):
    if i==1:
        print("_"*(n+1))
    elif i==(n+1):
        print("|/")
    else:
        space=" "*(n-i+1)
        print("|"+space+"/")
#WAP to find solid right angled triangle 2
n=int(input())
for i in range(1,(n+1)):
    left_space="  "*(n-i)+"* "*i
    print(left_space)
#WAP to find inverted solid right angled triangle
n=int(input())
for i in range(0,n):
    left_space="  "*(i)+"* "*(n-i)
    print(left_space)
#WAP to find sum of the series like 2-2**3+2**5-  
x=int(input())
n=int(input())
result=0
power=1
for i in range(0,n):
    if i%2==0:
        result=((x)**power)+result
        power=power+2
    else:
        result=-((x)**power)+result
        power=power+2