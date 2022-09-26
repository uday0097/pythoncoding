#WAP for create and print list
l1=["Rose",183,148,123.64,False]
print(l1)
#WAP to print list concatenation
num_list =  [10, 20, 40, 100]
n = int(input())
first_list = [n]+num_list# Add the number in the beginning
second_list = num_list+[n]# Add the number at the end

print(first_list)
print(second_list)
#WAP to print convert string to list
n=input()
print(list(n))
#WAP to find list indexing
color_list = ["Red", "Orange", "Yellow", "Pink", "Green", "Blue", "Purple", "Black", "White"]
# Write your code here
n=int(input())
list1=color_list[n]
print(list1)
#WAP to find list indexing 2
programming_languages_list = ["Python", "Java", "Ruby", "C", "C++", "Go", "R", "JavaScript", "Swift", "PHP", "Kotlin", "Perl"]
# Write your code here
n=int(input())
for i in range(n):
    num=int(input())
    print(programming_languages_list[num])
#WAP to find list repetion
m=int(input())
n=int(input())
list2=[m]*n
print(list2)
#WAP to print greater than N
num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
n=int(input())
list_a=[]
for i in num_list:
    if i>n:
        list_a=list_a+[i]
print(list_a)
#WAP to create and print list2
n=int(input())
list1=[]
for i in range(n):
    num=input()
    list1=list1+[num]
print(list1)
#WAP to find reverse order
n=int(input())
list1=[]
for i in range (n):
    num=input()
    list1=list1+[num]
for i in range (n):
    print(list1[n-i-1])
#WAP to find list conctenation 2
n=int(input())
list1=[]
for i in range (n):
    num=input()
    list1=list1+[num]
list_main=list1[:3]+list1[(n-3):n]
print(list_main)
#WAP to find create and print list3
n=int(input())
list1=[]
for i in range (1,n+1):
    num=int(input())
    list1=list1+[num]
print(list1)
#WAP to find list indexing3
n=int(input())
t=int(input())
a=[]
for i in range(0,(n)):
    num=int(input())
    a=a+[num]
for j in range(t):
    in_ex=int(input())
    print(a[in_ex])
#WAP to find first and last element in list
n=int(input())
sum=[]
for i in range(n):
    num=int(input())
    sum=sum+[num]
fi_in=sum[:2]
la_in=sum[(n-2):n]
print(fi_in+la_in)
#WAP to print split sentence
n=input()
list1=n.split()
for words in list1:
    print(words)
#WAP to print list reverse
n=input()
list1=n.split()
list2=list1[::-1]
print(list2)
#WAP to find sum of list elements
n=input()
list1=n.split()
sum=0
len_n=len(list1)
for i in range(len_n):
    sum=sum+int(list1[i])
print(sum)
#WAP to print reverse a letter in a word in a sentence
n=input()
list1=n.split()
for i in range(0,len(list1)):
    list1[i]=list1[i][::-1]
output=" ".join(list1)
print(output)
#WAP to print pattern
list_a = input().split(",")
list_b = input().split(",")

len_of_list_a = len(list_a)
n = len_of_list_a - 1

for i in range(len_of_list_a):
    num_1 = list_a[i]
    num_2 = list_b[n]
    result = str(num_1) + " " + str(num_2)
    n=n-1
    print(result)
#WAP to print last half of the list
n=int(input())
m=input().split()
list1=[]
for i in range(len(m)):
   list1=list1+[int(m[i])]
if n%2==1:
    list2=list1[((n//2)+1):]
    print(list2)
elif n%2==0:
    list2=list1[(n//2):]
    print(list2)
#WAP to print reverse of the sentence
n=input()
list1=n.split(" ")
list2=list1[::-1]
list2=" ".join(list2)
print(list2)
#WAP to print product of given list elements
n=input()
list1=n.split()

mul=1
for i in range(1,(len(list1)+1)):
    mul=mul*(int(list1[i-1]))
print(mul)
#WAP to print largest number in a list
n=input()
m=n.split()
max=int(m[0])
for i in m[1:]:
    if max<int(i):
        max=int(i)
print(max)
 #WAP to print average of the list
 n=input()
m=n.split()
sum=0
for i in range(len(m)):
    sum=sum+int(m[i])
avg=sum/len(m)
print(round(avg,2))
#WAP to find acronym 
n=input()
m=n.split()
string=""
for word in m:
    if word!="and":
        string=string+word[0]+"."
string=string.strip('.')
print(string)

       





















































































    





















