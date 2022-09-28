#WAP to print return the given argument
def func(arg_1):
    res=arg_1
    return res
    # Write your code here


n = int(input())
result = func(n)
print(result)
#WAP to print welcome message
def say_wishes(arg_1):
    msg="Welcome "+arg_1
    print(msg)
    return msg
    # Write your code here

name = input()
say_wishes(name)
#WAP to print multiply with 3
def multiply_with_three(arg_1):
    mul=arg_1*3
    print(mul)
    return mul
    # Write your code here

n = int(input())
multiply_with_three(n)
#WAP to print divisible by 7
def divisible_by_seven(arg_1):
    msg=arg_1
    if msg%7==0:
        print("True")
    else:
        print("False")
    # Write your code here


n = int(input())
divisible_by_seven(n)
#WAP to print perimeter of square
def perimeter_of_square(arg_1):
    per=arg_1*4
    return per
    # Write your code here

side = int(input())
result = perimeter_of_square(side)
print(result)
#WAP to print add two numbers
def add(arg_1, arg_2):
    addition=arg_1+arg_2
    print(addition)
    return addition
    # Complete this function


a = int(input())
b = int(input())
# Call the add function
add_1=add(a,b)
#WAP to print second character in a word
def second_character(arg_1):
    msg=arg_1
    sec_char=msg[1]
    print(sec_char)
    return sec_char
    # Complete this function

word = input()
# Call the second_character function
char=second_character(word)
#WAP to print indexing 2
def indexing(arg_1, arg_2):
    msg=arg_1
    indx=msg[index]
    print(indx)
    return indx
    # Complete this function

word = input()
index = int(input())
# Call the indexing function
calli=indexing(arg_1=word,arg_2=index)
#WAP to print printing message
def message(arg_1, arg_2):
    msg=arg_1+" is "+str(arg_2)+" years old."
    print(msg)
    return msg
    # Complete this function

name = input()
age = int(input())
# Call the message function
greet=message(arg_1=name,arg_2=age)
#WAP to print no of lower case and upper case letters
def count_of_lowercase_and_uppercase_letters(arg_1):
    count_of_uppercase=0
    count_of_lowercase=0
    for i in arg_1:
        
        if i==i.upper():
            count_of_uppercase=count_of_uppercase+1
        elif i==i.lower():
            count_of_lowercase=count_of_lowercase+1
        
        
    
    # Complete this function

    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
# Call the count_of_lowercase_and_uppercase_letters function
calli=count_of_lowercase_and_uppercase_letters(word)
#WAP to print squares in a list
def get_list(string_a):
    list_a = string_a.split(',')
    len_list_a = len(list_a)
    for i in range(len_list_a):
        list_a[i] = int(list_a[i])**2
    return list_a


string_a = input()
numbers_list = get_list(string_a)
print(numbers_list)
#WAP to print team points
def calculate_league_points(wins, draws, losses):
    wi_nn=wins*4
    dra_w=draws*2
    los_s=losses*(-1)
    tot_point=wi_nn+dra_w+los_s
    print(tot_point)
    return tot_point
    # Complete this function


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
# Call the calculate_league_points function
calli=calculate_league_points(wins,draws,losses)
#WAP to print speed meter
def get_speed_status(speed):
    spe_d=speed
    if spe_d<60:
        print("Normal")
    elif (spe_d>=60) and (spe_d<80):
        print("Warning")
    elif spe_d>=80:
        print("Over Speed")
    # Complete this function


speed = int(input())
# Call the get_speed_status function
calli=get_speed_status(speed)
#WAP to print weather reporter
def get_weather_report(temperature):
    tem_p=temperature
    if tem_p<22:
        print("Cold")
    elif (tem_p>=22) and (tem_p<35):
        print("Warm")
    elif tem_p>=35:
        print("Hot")
    # Complete this function


temperature = int(input())
# Call the get_weather_report function
calli=get_weather_report(temperature)
#WAP to print discount
def get_discount(amount):
    dis_c=amount
    if dis_c<500:
        print("5%")
    elif (dis_c>=500) and (dis_c<2500):
        print("10%")
    elif dis_c>=2500:
        print("20%")
    # Complete this function


amount = int(input())
# Call the get_discount function
calli=get_discount(amount)
#WAP to print calculate bill
def calculate_bill(amount):
    bill=amount
    if bill<500:
        disc_ount=bill*(0.05)
        total=(bill)-(disc_ount)
        print(round(total,3))
    elif (bill>=500) and (bill<2500):
        disc_ount=bill*(0.1)
        total=(bill)-(disc_ount)
        print(round(total,3))
    elif bill>=2500:
        disc_ount=bill*(0.2)
        total=(bill)-(disc_ount)
        print(round(total,3))
        # Complete this function


amount = int(input())
# Call the calculate_bill function
calli=calculate_bill(amount)
#WAP to print fizz buzz
def fizz_buzz(number):
    buzz=number
    if (buzz%3==0) and (buzz%5==0):
        print("FizzBuzz")
    elif (buzz%3==0):
        print("Fizz")
    elif (buzz%5==0):
        print("Buzz")
    else:
        print(buzz)
    # Complete this function


number = int(input())
calli=fizz_buzz(number)
# Call the fizz_buzz function
#WAP to print squares from m to n
def sum_of_squares_m_to_n(m, n):
    arg_1=m
    arg_2=n
    add=0
    for i in range(arg_1,(arg_2+1)):
        add=add+(i)**2
    print(add)
    # Complete this function


m = int(input())
n = int(input())
# Call the sum_of_squares_m_to_n function
calli=sum_of_squares_m_to_n(m,n)
#WAP to print sum of cubes from m to n
def sum_of_cubes_m_to_n(m, n):
    arg_1=m
    arg_2=n
    add=0
    for i in range(arg_1,(arg_2+1)):
        add=add+(i)**3
    print(add)
    # Complete this function


m = int(input())
n = int(input())
calli=sum_of_cubes_m_to_n(m,n)
# Call the sum_of_cubes_m_to_n function
#WAP to print labelling numbers
def show_numbers(number):
    arg_1=number
    for i in range(arg_1+1):
        if i%2==0:
            print(str(i)+" EVEN")
        else:
            print(str(i)+" ODD")
    # Complete this Function


number = int(input())
# Call the show_numbers function
calli=show_numbers(number)
#WAP to print upper case and lower case letters
def get_lower_and_upper_case_letters(word):
    arg_1=word
    upp=""
    low=""
    for i in arg_1:
        if i==i.upper():
            upp=upp+i
        elif i==i.lower():
            low=low+i
    print(upp)
    print(low)
    # Complete this function


word = input()
# Call the get_lower_and_upper_case_letters function
calli=get_lower_and_upper_case_letters(word)
#WAP to print count vowels
def count_the_vowels(word):
    arg_1=word
    vowels="aeiou"
    count=0
    for i in arg_1:
        for j in vowels:
            if i==j:
                count=count+1
    print(count)
    # Complete this function


word = input()
# Call the count_the_vowels function
calli=count_the_vowels(word)
#WAP to print four passengers and driver
def number_of_cars_needed(no_of_people):
    arg_1=no_of_people
    count=0
    arg_2=arg_1%5
    j=(arg_2==1) or (arg_2==2)
    k=(arg_2==3) or (arg_2==4)
    for i in range(1,(arg_1+1)):
        if i%5==0:
            count=count+1
    if j or k:
        count=count+1
    print(count)
    # Complete this function


no_of_people = int(input())
# Call the number_of_cars_needed function
calli=number_of_cars_needed(no_of_people)
#WAP to print ATM pin code validation
def validate_atm_pin_code(pin):
    arg_1=pin
    arg_2=arg_1.isdigit()
    if arg_2==True:
        if (len(arg_1)==4) or (len(arg_1)==6):
            print("Valid PIN Code")
        else:
            print("Invalid PIN Code")
    else:
        print("Invalid PIN Code")
    
    
    # Complete this function


pin = input()
# Call the validate_atm_pin_code function
calli=validate_atm_pin_code(pin)






















































































































































































































































































