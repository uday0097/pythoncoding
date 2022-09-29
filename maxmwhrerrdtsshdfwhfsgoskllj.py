#WAP to find mean mode and median
def get_median(arg_list):
    arg_list.sort()
    size = len(arg_list)
    if size %2 == 1:
        return arg_list[size//2]
    else:
        return (arg_list[size//2] + arg_list[size//2 -1])/2
    
    
def get_mean(arg_list):
    sum_list = 0
    for i in arg_list:
        sum_list +=i
    return round(sum_list/len(arg_list), 2)




def get_mode(arg_list):
    mode_list = sorted(set(user_list), key=user_list.count,reverse=True)
    mode_max = user_list.count(mode_list[0])
    mode_res = []
    for i in mode_list:
        if user_list.count(i) < mode_max:
            break
        mode_res.append(i)
    return sorted(mode_res)


        
user_str = input('Enter a string of integers separated by a space: ')
user_list = [int(i) for i in user_str.split()]
print('Mean :', get_mean(user_list))
print('Median :', get_median(user_list))
# Displaying mode list values separated by a space
print('Mode :', *get_mode(user_list))
#WAP to print Shift Numbers

#Given a string, write a program to move all the numbers in it to its end.Input
inputString =input("");
digits=""
letters=""
symbols=""
# Looping through a string.
for letter in inputString:
    if (letter.isdigit()):
        digits+=letter
    elif (letter.isalpha()):
        letters+= letter
    else:
        symbols+= letter
# Display a new string.
print(letters+digits+symbols)
#WAP to print the index of the last occurrence of the given number N in the list.Input
a = [int(i) for i in input("Enter list of numbers: ").split()]
b = int(input("Search number: "))
index = 0
for i in range(len(a)):
    if a[i] == b:
        index = i
print("Index of Last Occurrence: ", index)
#WAP to print sum of prime numbers in a list
#read a single line containing space-separated integer
numbersStr=input("").split(' ')
sumPN=0
for number in numbersStr:
    number=int(number)
    is_prime=True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime=False
                break
        if is_prime:
            #calculate the sum of all prime numbers from 1 to N.
            sumPN=sumPN+number


#Display the result
print(str(sumPN))
#WAP to print sum of prime numbers from m to n
m, n = int(input()), int(input())  # numbers m and n
sum = 0  # sup of primes
for i in range(m, n + 1):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True  # composite number
    if flag == False and i != 1:  # if isn't composite number
        sum += i
print(sum)































