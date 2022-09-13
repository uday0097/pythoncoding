#WAP to print date format
date=input()
date_format=date.replace("-","/")
print(date_format)
#WAP to print lower and upper
string=input()
lower=string.lower()
upper=string.upper()
print(lower)
print(upper)
#WAP to print Palindrome
string=input()
c=len(string)
revs=""
original=string[0:len(string)]
upper=original.upper()
for i in range(1,(c+1)):
    revs=revs+string[c-i]
upper_revs=revs.upper()
if upper==upper_revs:
    print("Palindrome")
else:
    print("Not a Palindrome")
#WAP to print valid password
string=input()
val=False
for ev_char in string:
    is_dig=ev_char.isdigit()
    if is_dig:
        val=True
if val:
    print("Valid Password")
else:
    print("Invalid Password")
#WAP to print valid password 2
string=input()
lowe=string.lower()
if lowe==string:
    print("Invalid Password")
else:
    print("Valid Password")
#WAP to print valid password 3
string=input()
upp=string.upper()
low=string.lower()
val=False
case=(not(upp==string))and(not(low==string))
for eac_car in string:
    dig=eac_car.isdigit()
    if dig:
        val=True
if case and val:
    print("Valid Password")
else:
    print("Invalid Password")
#WAP to print swap case
string=input()
a=""
result=""
for eac_char in string:
    if eac_char==eac_char.upper():
        result=result+eac_char.lower()
        
    elif eac_char==eac_char.lower():
        result=result+eac_char.upper()
        
print(result)
#WAP to print palindrome2
string=input()
a=len(string)
rev=""
original=string[0:a]
upper=original.upper()
for i in range(1,(a+1)):
    rev=rev+string[a-i]
up_rev=rev.upper()
if upper==up_rev:
    print("True")
else:
    print("False")
#WAP to print palindrome3
string=input()
string=string.upper()
string=string.replace(" ","")
string=string.replace("'","")
a=len(string)
rev=""
for i in range(1,(a+1)):
    rev=rev+string[a-i]
up_rev=rev.upper()
if string==up_rev:
    print("True")
else:
    print("False")
#WAP to print remove vowels in a sentence
string=input()
vowels=("A","E","I","O","U")
for i in string:
    if i.upper() in vowels:
        string=string.replace(i,"")
print(string)
#WAP to print digit upper lower and special character
string=input()
a=string.upper()
b=string.lower()
if string.isdigit():
    print("Digit")
elif string.isupper():
    print("Uppercase Letter")
elif string.islower():
    print("Lowercase Letter")
else:
    print("Special Character")






















































