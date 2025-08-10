# Python List Programs

#1.Python Program to Append an Item to a List
# li = [10,20,30,40,50]
# print(li)
# li.append(101)
# print(li)


#2.Python Program to access List Index and Values
# li = [10,20,30,40,50]
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[-1])
# print(li[-2])


#3.Python Program to add two Lists
# li1 = [10,20,30]
# li2 = [40,50,60]
# final = []
# for i in range(len(li1)):
#     final.append(li1[i] + li2[i])
# print(final)


#4.Python Program to Change List Items
# li = [10,20,30,40,50]
# print(li)
# li[2] = 102
# print(li)


#5.Python Program for Arithmetic Operations on Lists
# add,sub,mul,div,mod,flo,exp = [],[],[],[],[],[],[]
# li1 = [1,3,5]
# li2 = [2,4,6]
# for i in range(len(li1)):
#     add.append(li1[i] + li2[i])
#     sub.append(li1[i] - li2[i])
#     mul.append(li1[i] * li2[i])
#     div.append(li1[i] / li2[i])
#     mod.append(li1[i] % li2[i])
#     flo.append(li1[i] // li2[i])
#     exp.append(li1[i] ** li2[i])
# print("Addition :- ",add)
# print("Subtraction :- ",sub)
# print("Multiplication :- ",mul)
# print("Division :- ",div)
# print("Modulus :- ",mod)
# print("Floor :- ",flo)
# print("Exponent :- ",exp)


#6.Python Program to Calculate the Average of List Items
# li = [2,3,5,7,9,34,45,6]
# count = len(li)
# total = sum(li)
# avg = total / count
# print(f"Average of list items are :- {avg}")


#7.Python Program to Clear a List
# li = [10,20,30,40]
# print(li)
# li.clear()
# print(li)


#8.Python Program to check List is Empty or Not
# li = [10,20,30]
# if(li):
#     print("List is not empty")
# else:
#     print("List is empty")


#9.Python Program to Check if the Element Exists in a List
# li = [10,20,30,40,50,60,70]
# if(101 in li):
#     print("Item exist in list")
# else:
#     print("Item does not exist in list.")


#10.Python Program to Clone or Copy a List
# li = [10,20,30,40]
# new = li.copy()
# print(li,id(li))
# print(new,id(new))


#11.Python Program to Count Occurrence of an element in a List
# li = [10,20,30,40,10,10,10]
# print(f"In li there are {li.count(10)} occrances of element 10")


#12.Python program to Count Even and Odd Numbers in a List
# li = [10,11,12,13,14,15,16,17]
# even = odd = 0
# for i in li:
#     if(i%2==0):
#         even += 1
#     else:
#         odd += 1
# print(f"Count of even in li is :- {even}")
# print(f"Count of odd in li is :- {odd}")


#13.Python program to Count Positive and Negative Numbers in a List
# li = [10,11,12,-13,-14,15,16,17]
# positive = negative = 0
# for i in li:
#     if(i>0):
#         positive += 1
#     elif(i<0):
#         negative += 1
# print(f"Total positive are :- {positive}")
# print(f"Total negative are :- {negative}")


#14.Python program to find Length of a List
# li = [10,20,30,40,50]
# print(f"Length of list :- {len(li)}")


#15.Python program to find the List Difference
# li1 = [10,20,30,40,50]
# li2 = [40,50,60,70,80]
# s1 = set(li1).difference(set(li2))
# s2 = set(li2).difference(set(li1))
# print(list(s1) + list(s2))


#16.Python Program to Find the Average of a List
# li = [1,2,3,4,5,6,7]
# total = sum(li)
# count = len(li)
# avg = total / count
# print(f"Average of list :- {avg}")


#17.Python Program to Merge Two Lists
# li = [1,2,3,4,5]
# li1 = [4,5,6,7,8]
# res = li + li1
# print(res)


#18.Python List Multiplication Program
# li = []
# while True:
#     num = int(input("Enter any list item :- "))
#     if(num == 0):
#         break
#     li.append(num)
# mul = 1
# for i in li:
#     mul *= i
# print(f"Multiplication is :- {mul}")


#19.Python program to find the Sum of All List Elements
# li = [10,20,30,40,50]
# total = 0
# for i in li:
#     total += i
# print(f"Sum of all list items :- {total}")


#20.Sum and Average of a List
# li = [10,20,30,40,50]
# total = 0
# for i in li:
#     total += i
# avg = total / len(li)
# print(f"Sum of all list items :- {total}\nAverage of list items :- {avg}")


#21.Sum of Even and Odd List Numbers
# li = [10,20,-30,-40,50,9]
# even = odd = 0
# for i in li:
#     if(i%2==0):
#         even += i
#     else:
#         odd += i
# print(f"Sum of even :- {even} \nSum of odd :- {odd}")


#22.Left Rotate a List by n
# li = [10,20,30,40,50,60,70,80,90,100]
# print("Original :- ",li)
# n = int(input("Enter how many elements want to shift ftom right to left :- "))
# for i in range(n):
#     new = li.pop(0)
#     li.append(new)
# print("Updated :- ",li)


#23.Right Rotate a List by n
# li = [10,20,30,40,50,60,70,80,90,100]
# print("Original :- ",li)
# n = int(input("Enter how many elements want to shift ftom right to left :- "))
# for i in range(n):
#     item = li.pop()
#     li.insert(0,item)
# print("Updated :- ",li)


#24.Remove an item from a List
# li = [10,20,30,40,50]
# print(li)
# li.remove(10)
# print(li)


#25.Remove the First element from a List
# li = [10,20,30,40,50]
# print(li)
# li.pop(0)
# print(li)


#26.Remove the Last Element from a List
# li = [10,20,30,40,50]
# print(li)
# li.pop()
# print(li)


#27.Iterate Over List Items
# li = [10,20,30,40,50,60,70]
# for i in li:
#     print(i)


#28.Interchange First and Last Elements in a List.
# li = [10,20,30,40,50,60,70]
# print("Original list :- ",li)
# li[0],li[-1] = li[-1],li[0]
# print("Updated list :- ",li)


#29.Swap two items in a List
# li = [10,20,30,40,50]
# print("Original list :- ",li)
# li[0],li[2] = li[2],li[0]
# print("Updated list :- ",li)