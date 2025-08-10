#List Sort, Remove, Reverse, Print Items Programs

#1.Python program to Print Elements in a List
# li = [10,20,30,40]
# print(li)


#2.Python Program to Print List Items in Reverse Order
# li = [10,20,30,40,50]
# print("Original :- ",li)
# li.reverse()
# print("Updated :- ",li)


#3.Python Program to Print List Items Greater Than Average
# li = [10,20,30,40,50,60,70,80,90,100]
# avg = sum(li) / len(li)
# print("Average :- ",avg)
# for i in li:
#     if(i > avg):
#         print(i)


#4.Python Program to Print List Items at Even Position
# li = [10,20,30,40,50,60,70,80,90,100]
# for i in li[::2]:
#     print(i)


#5.Python Program to Print List Items at Odd Position
# li = [10,20,30,40,50,60,70,80,90,100]
# for i in li[1::2]:
#     print(i)


#6.Python Program to Print Even Numbers in a List
# li = [11,12,13,14,15,16,17,18]
# for i in li:
#     if(i%2==0):
#         print(i)


#7.Python program to Print Odd List Numbers
# li = [11,12,13,14,15,16,17,18]
# for i in li:
#     if(i%2!=0):
#         print(i)


#8.Python program to Put Even and odd Numbers in Separate List
# li = [11,12,13,14,15,16,17,18]
# even = []
# odd = []
# for i in li:
#     if(i%2!=0):
#         odd.append(i)
#     else:
#         even.append(i)
# print("Even :- ",even)
# print("Odd :- ",odd)


#9.Python program to Print Positive Numbers
# li = [10,20,-4,5,50,-5,-4,-3,23]
# for i in li:
#     if(i>0):
#         print(i)


#10.Python program to Print Negative Numbers
# li = [10,20,-4,5,50,-5,-4,-3,23]
# for i in li:
#     if(i<0):
#         print(i)


#11.Python program to Put Positive and Negative Numbers in Separate List
# li = [10,20,-4,5,50,-5,-4,-3,23]
# positive = []
# negative = []
# for i in li:
#     if(i>0):
#         positive.append(i)
#     else:
#         negative.append(i)
# print("Positive :-",positive)
# print("Negative :- ",negative)


#12.Python program to Print the Largest Number in a List
# li = [12,54,67,43,34,6,87,45,47,86]
# high = li[0]
# for i in range(len(li)):
#     if(li[i] > high):
#         high = li[i]
# print("Highest number is :- ",high)


#13.Python program to Print the Second Largest Number in a List
# li = [12,54,67,43,34,6,87,45,47,86]
# li.sort()
# print("Second largest number :- ",li[-2])


#14.Python program to Print the Largest and Smallest Number
# li = [12,54,67,43,34,6,87,45,47,86]
# small = min(li)
# large = max(li)
# print("larger is :- ",large)
# print("Small is :- ",small)


#15.Python program to Print the Smallest Element in a List
# li = [12,54,67,43,34,6,87,45,47,86]
# small = li[0]
# for i in range(len(li)):
#     if(li[i] < small):
#         small = li[i]
# print(f"Smallest element is :- {small}") 


#16.Python program to Remove Duplicates from List
# li = [10,20,30,10,10,20,30,40,50,60,70]
# print("Original with duplicate :- ",li)
# s = set(li)
# print(list(s))


#17.Python program to Remove Even Numbers in a List
# li = [1,2,3,4,5,6,7,8,9,10]
# print("Original list :- ",li)
# li = [i for i in li if(i%2!=0)]
# print("Updated li :- ",li)


#18.Python program to Reverse List Items
# li = [1,2,3,4,5,6,7,8,9,10]
# print(li)
# li.reverse()
# print(li)


#19.Python program to Sort List Items in Ascending Order
# li = [34,6,23,56,87,5,56]
# print("Original list :- ",li)
# li.sort()
# print("Update list :- ",li)


#20.Python Program to Sort List Items in Descending Order
# li = [34,6,23,56,87,5,56]
# print("Original list :- ",li)
# li.sort(reverse=True)
# print("Update list :- ",li)