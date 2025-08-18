#Python Programming Examples on Tuples

#1.Python Program to add an Item to a tuple
# t = (10,20,30,40)
# print("Original tuple :- ",t)
# li = list(t)
# li.append(101)
# t = tuple(li)
# print("Modify tuple :- ",t)


#2.Python Program to create a Tuple
# t = (10,20,30,40,50)
# print(t)


#3.Python Program to create Tuple of Different Types
# t = (10,True,"welcome",54.43)
# print(t)


#4.Python Program to Find Tuple Length
# t = (10,True,"welcome",54.43)
# print("length of tuple :- ",len(t))


#5.Python Program to Remove an Item from Tuple
# t = (10,True,"welcome",54.43)
# print(t)
# li = list(t)
# li.remove("welcome")
# t = tuple(li)
# print(t)


#6.Python Program to Slice a Tuple
# t = (10,20,30,40,50,60,"welcome","new",True,34.54,23,23)
# print(t)
# print(t[1:5])
# print(t[::-1])


#7.Python Program to Unpack Tuple Items
# t = (10,True,"welcome",54.43)
# a,b,c,d = t
# print(a)
# print(b)
# print(c)
# print(d)


#8.Python Program to Create a Tuple with Numbers
# t = (10,20,30,40,50,60,70)
# print(t)


#9.Python Program to Check Item exists in Tuple
# t = (10,20,30,40,50,60,70)
# item = 40
# if(item in t):
#     print("Item exist")
# else:
#     print("Not exist")


#10.Python Program to Find Sum of Even and Odd Numbers in Tuple
# t = (1,2,3,4,5,6,7,8,9,10)
# even = odd = 0
# for i in t:
#     if(i%2==0):
#         even += i
#     else:
#         odd += i
# print("Sum of even :- ",even)
# print("Sum of odd :- ",odd)


#11.Python Program to Find Sum of Tuple Items
# t = (1,2,3,4,5,6,7,8,9,10)
# print("Sum of all tuple are :- ",sum(t))


#12.Python Program to Reverse Tuple
# t = (1,2,3,4,5,6,7,8,9,10)
# print(t)
# print(t[::-1])


#13.Count Positive and Negative Numbers in a Tuple
# t = (10,20,30,-21,20,-34,-5,324)
# positive = negative = 0
# for i in t:
#     if(i > 0):
#         positive += 1
#     elif(i < 0):
#         negative += 1
# print("Positive :- ",positive)
# print("Negative :- ",negative)


#14.Count Even and Odd Numbers in Tuple
# t = (10,20,30,-21,20,-34,-5,324)
# even = odd = 0
# for i in t:
#     if(i%2==0):
#         even += 1
#     else:
#         odd += 1
# print("Even are :- ",even)
# print("odd are :- ",odd)
