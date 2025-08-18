#Python Programming Examples on Sets

#1.Python Program to create a Set
# s = {10,20,30,40}
# print(s)


#2.Python program to Count Even and Odd Numbers in Set
# s = {1,2,3,4,5,6,7,8,9,10}
# li = list(s)
# even = odd = 0
# for i in li:
#     if(i%2==0):
#         even += 1
#     else:
#         odd += 1
# print("Even :- ",even)
# print("odd :- ",odd)


#3.Python program to Count Positive and Negative Numbers in Set
# s = {1,2,3,4,5,-6,-7,8,9,10}
# positive = negative = 0
# li = list(s)
# for i in li:
#     if(i>0):
#         positive += 1
#     elif(i<0):
#         negative += 1
# print("Positive :- ",positive)
# print("Negative :- ",negative)


#4.Python program to Iterate Set Items
# s = {10,20,30,40,50}
# for i in s:
#     print(i)


#5.Python program to Print Largest Set Item
# s = {10,45,67,86,35,67}
# print(max(s))


#6.Python program to find Length of a set
# s = {10,45,67,86,35,67}
# print(f"Length of set :- {len(s)}")


#7.Python program to Print Even Numbers in Set
# s = {10,45,67,86,35,67}
# for i in s:
#     if(i%2==0):
#         print(i)


#8.Python program to Print Negative Numbers in Set
# s = {10,45,67,-86,35,67}
# for i in s:
#     if(i < 0):
#         print(i)


#9.Python program to Print Odd Numbers in Set
# s = {10,45,67,-86,35,67}
# for i in s:
#     if(i%2!=0):
#         print(i)


#10.Python program to Print Positive Numbers in Set
# s = {10,45,67,-86,35,67}
# for i in s:
#     if(i > 0):
#         print(i)


#11.Python program to find Sum of Even and Odd Numbers in Set
# s = {10,45,67,-86,35,67}
# even = odd = 0
# for i in s:
#     if(i%2==0):
#         even += i
#     else:
#         odd += i
# print("Even is :- ",even)
# print("odd is :- ",odd)


#12.Python program to find Smallest Set Item
# s = {10,20,30,40,56,86,43,45,7,8,45,23,5,45,75}
# print(min(s))