# n = 5

# for i in range (0,5):
#     print("****")


# rows = 4
# col =  4

# for i in range (rows):
#     for j in range (col):
#         if i == 0 or i == rows - 1 or j == 0 or j == col -1:
#             print("*",end= "")
#         else:
#             print(" ",end="")
#     print()


# number = int(input("Enter the number."))

# for i in range(0,number):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for j in range(0,number):
#         print("*",end="")    
#     print()


number = int(input("Enter the number: "))

# for i in range(0,number):
#     for j in range(0,i):
#         print("*",end="")
#     print()    

# for i in range(0,number):
#     for j in range(number-i-1):
#         print(" ",end="")
#     for k in range(number):
#         print("*",end="")    
#     print()   

# for i in range(number):
#     for j in range(i):
#         print("*",end="")
#     print()  

# for i in range(number):
#     pattern = 2*i + 1
#     for j in range(number-i-1):
#         print(" ",end="")
#     for k in range(pattern):
#         print("*",end="")
#     print()       


# for i in range(number):
#     pattern = 2*i + 1
#     for j in range(number-i-1):
#         print(" ",end="")
#     for j in range(pattern):
#         if i == number-1 or j == pattern -1 or j == 0 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()              


# for i in range(number):
#     pattern = 2*number - 1
#     for j in range(i):
#         print(" ",end="")
#     for k in range(pattern-2*i):
#         if i == 0 or k == pattern-2*i-1 or k == 0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(0,number,1):
#     for j in range(i):
#         print("*",end="")
#     print()    
# for i in range(number,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print() 


number = 4

# Upper half
for i in range(0, number):
    for j in range(number - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()

# Lower half
for i in range(0, number - 1):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(number - i - 1):
        print("*", end="")
    print()
     
