#Advanced Number Programs

#1.Python Program to do Arithmetic Calculations using Functions
# def calculate(n1,n2,op):
#     if(op == '+'):
#         return n1 + n2
#     elif(op == '-'):
#         return n1 - n2
#     elif(op == '*'):
#         return n1 * n2
#     elif(op == '/'):
#         return n1 / n2
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))
# op = input("Enter any operator :- ")
# res = calculate(num1,num2,op)
# print(f"Result is :- {res}")


#2.Python Program to Count Number of Digits in a Number
# num = int(input("Enter any number :- "))
# st = str(num)
# print("Number of digits are :- ",len(st))


#3.Python Program to find Factors of a Number
# def check_factor(num):
#     li = []
#     for i in range(1,num+1):
#         if(num%i==0):
#             li.append(i)
#     return li
# num = int(input("Enter any number :- "))
# res = check_factor(num)
# print(f"Factors of number {num} is :- {res}")


#4.Python Program to find the Factorial of a Number
# def check_fact(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     return fact
# num = int(input("Enter any number :- "))
# res = check_fact(num)
# print(f"Factorial of number is :- {res}")


#5.Python program to print the First Digit of a Number
# num = int(input("Enter any number :- "))
# st = str(num)[0]
# print(int(st))


#6.Python program to print Last Digit in a Number
# num = int(input("Enter any number :- "))
# st = str(num)
# print(st[-1])


#7.Python program to find the GCD of Two Numbers
# n1 = int(input("ENter first number :- "))
# n2 = int(input("Enter second number :- "))
# d1 = []
# d2 = []
# for i in range(1,n1+1):
#     if(n1%i==0):
#         d1.append(i)
# for i in range(1,n2+1):
#     if(n2%i==0):
#         d2.append(i)
# final = []
# for i in d1:
#     if(i in d2):
#         final.append(i)
# print(final[-1])


#8.Python program to find LCM of Two Numbers
# n1 = int(input("ENter first number :- ")) #12
# n2 = int(input("Enter second number :- ")) #15
# l1 = []
# l2 = []
# for i in range(1,11):
#     l1.append(i*n1)
# for i in range(1,11):
#     l2.append(i*n2)
# for i in l1:
#     if(i in l2):
#         print("Least common multiplier is :- ",i)
#         break


#9.Python program to check a Palindrome Number
# num = int(input("Enter any number :- "))
# st = str(num)
# if(st == st[::-1]):
#     print(f"{int(st)} is palindrome")
# else:
#     print(f"{int(st)} is not palindrome")


#10.Python Program to Print Palindrome Numbers from 1 to 100
# for i in range(1,101):
#     if(str(i) == str(i)[::-1]):
#         print(i)


#11.Python Program to Reverse a Number
# num = int(input("Enter any number :- "))
# print("Original number :- ",num)
# st = str(num)[::-1]
# print("Updated number :- ",int(st))


#12.Python program to find the Sum of Digits in a Number
# num = int(input("Enter any number :- "))
# total = 0
# st = str(num)
# for i in st:
#     total += int(i)
# print("Total is :- ",total)


#13.Python Program to Swap Two Numbers
# n1 = int(input("Enter first number :- "))
# n2 = int(input("Enter second number :- "))
# print("Here n1 is :- ",n1)
# print("Here n2 is :- ",n2)
# temp = n1
# n1 = n2
# n2 = temp
# print("Here updated n1 is :- ",n1)
# print("Here updated n2 is :- ",n2)