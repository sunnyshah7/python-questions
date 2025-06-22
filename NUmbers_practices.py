import math

number = int(input("Enter the number: "))

# if number >=0:
#     print("Positive")
# else:
#     print("Negetive")    

#Even odd number finding.
# if number%2 == 0:
#     print("Even")
# elif number == 0:
#     print("Even") 
# else:
#     print("Odd")       

# N natural number finding.

# for i in range(1,number):
#     print(i,end="\n")

#sum of N natural number.

# sum = 0
# for i in range(1,number):
#     sum += i
# print("Sum of N natural number is",sum)    

# Sum of numbers in a given range

# number1 = int(input("Enter the range1: "))
# number2 = int(input("Enter the range2: "))
# sum = 0
# for i in range(number1,number2):
#     sum +=i
# print("Sum of number is",sum)  


#Leap Year Program

# if number % 4 == 0 and  number % 100 !=0 or number % 400 == 0:
#     print("Its a leap year.")
# else:
#     print("Its not a leap year.")    

#Prime number.

# flag = 0
# for i in range(2, int(math.sqrt(number)+1)):
#     if number%i == 0:
#         flag = 1
#         break
#     else:
#         flag = 0    

# if(flag == 0):
#     print("Prime Number.", number)
# else:
#     print("Not a Prime Number.")    

# prime mumber in range 

for num in range(2, 20):
    flag = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is Not a Prime Number")
