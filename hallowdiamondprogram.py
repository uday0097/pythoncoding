#WAP to print hollow diamond
n=int(input())
#for first line
left_space=" "*(n-1)
print(left_space+"*")
#for upper part
hollow_space=-1
for i in range(2,(n+1)):
    left_space=" "*(n-i)
    hollow_space=hollow_space+2
    print(left_space+"*"+" "*hollow_space+"*")
#for lower part
for i in range(1,(n-1)):
    left_space=" "*(i)
    hollow_space=hollow_space-2
    print(left_space+"*"+" "*hollow_space+"*")
#for last line
left_space=" "*(n-1)
print(left_space+"*")
#WAP to print hollow diamond 2
n=int(input())
#upper pattern
for i in range(0,(n)):
    star_count=n-i
    hollow_space="  "*(2*i)
    stars="* "*star_count
    right_star="* "*star_count
    print(stars+hollow_space+right_star)
#lower pattern
for i in range(1,n+1):
    star_count=n-i
    stars="* "*i
    hollow_space="  "*(2*(star_count))
    print(stars+hollow_space+stars)
#WAP to print dollar pattern
n = int(input())
for i in range(0, n):
    row_out = " " * (n-i-1)
    row_out = row_out + "$" * n
    print(row_out)






