#1.Python program for Hello World
# print("Hello World")


#2.Python program to add Two Numbers
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))
# print(f"Addition of {num1} and {num2} :- {num1+num2}")


#3.Python program to subtract two numbers
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))
# print(f"Subtraction of {num1} and {num2} :- {num1-num2}")


#4.Python Program to Multiply Two numbers
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))
# print(f"Multiply of {num1} and {num2} :- {num1*num2}")


#5.Python program for Arithmetic Operations
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))
# print(f"Addition of {num1} and {num2} :- {num1+num2}")
# print(f"Subtraction of {num1} and {num2} :- {num1-num2}")
# print(f"Multiply of {num1} and {num2} :- {num1*num2}")
# print(f"Division of {num1} and {num2} :- {num1/num2}")
# print(f"Floor Division of {num1} and {num2} :- {num1//num2}")
# print(f"Modulus of {num1} and {num2} :- {num1%num2}")
# print(f"Exponent of {num1} and {num2} :- {num1**num2}")


#6.Python program to print Calendar
# import calendar
# year = int(input("Enter any year :- "))
# month = int(input("Enter any month :- "))
# print(calendar.month(year,month))


#7.Python program to find Largest of 2 Numbers
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter Second number :- "))
# if(num1 > num2):
#     larger = num1
# else:
#     larger = num2
# print(f"larger between {num1} and {num2} :- {larger}")


#8.Python program to find Largest of 3 Numbers
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter Second number :- "))
# num3 = int(input("Enter Third number :- "))
# if((num1 > num2) and (num1 > num3)):
#     larger = num1
# elif(num2 > num3):
#     larger = num2
# else:
#     larger = num3
# print(f"larger between {num1}, {num2} and {num3} :- {larger}")


#9.Python program for Leap Year
# year = int(input("Enter any year :- "))
# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print(f"{year} is leap year.")
#         else:
#             print(f"{year} not leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


#10.Python Program to Print Negative Numbers in a Range
# for i in range(-10,0):
#     print(i)


#11.Python Program to Print Positive Numbers in a Range
# for i in range(1,15):
#     print(i)


#12.Python program to find Positive or Negative
# num = int(input("Enter any number :- "))
# if(num > 0):
#     print(f"{num} is positive ")
# elif(num < 0):
#     print(f"{num} is negative")
# else:
#     print(f"{num} is zero")


#13.Python program to check Number Divisible by 5 and 11
# num = int(input("Enter any number :- "))
# if((num % 5 == 0) and (num % 11 == 0)):
#     print(f"{num} is divisible by 5 and 11.")
# else:
#     print(f"{num} is not divisible by 5 and 11.")


#14.Python Program to Find the Sum and Average Of Three Numbers
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))
# num3 = int(input("Enter third number :- "))
# total = num1 + num2 + num3
# avg = total / 3
# print(f"Sum of three number is :- {total} \n Average of three number is :- {avg}")


#15.Python Program to Find the Average Of Two Numbers
# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))
# total = num1 + num2
# avg = total / 2
# print(f"Average of two number is :- {avg}")


#16.Python Program to Get Current Date and Time
# import datetime
# today = datetime.datetime.today()
# print(today)