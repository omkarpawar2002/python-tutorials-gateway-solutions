#Python Dictionary Programs

#1.Python Program to Add Key-Value Pair to a Dictionary
# d = {}
# key = input("Enter any key :- ")
# value = int(input("Enter any value :- "))
# d[key] = value
# print(d)


#2.Python program to Check if a Given key exists in a Dictionary
# d = {1:"one",2:"two",3:'three',4:"four",5:"five"}
# print(d)
# key = int(input("Enter any key :- "))
# if(key in d):
#     print(f"yes {key} key present in dictionary")
# else:
#     print(f"No {key} is not present in dictionary")


#3.Python program to Count words in a String using Dictionary
# st = input("Enter any word as a string :- ")
# new = st.split()
# d = {}
# for i in new:
#     if(i not in d):
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)


#4.Python program to Create Dictionary of keys from 1 to n and values are square of keys
# d = {}
# n = int(input("Enter how many key value pair you want :- "))
# for i in range(1,n+1):
#     d[i] = i*i
# print(d)


#5.Python program to Create Dictionary of Numbers 1 to n in (x, x*x) form
# n = int(input("Enter how many key value pairs you want :- "))
# pairs = [(i,i*i) for i in range(1,n+1)]
# print(dict(pairs))


#6.Python program to Map two lists into a Dictionary
# keys = [10,20,30,40]
# values = ["ten","twenty","thirty","fourty"]
# d = dict(zip(keys,values))
# print(d)


#7.Merge Two Dictionaries
# d1 = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'fourty'}
# d2 = {1:"one",2:"two"}
# d1.update(d2)
# print(d1)


#8.Multiply All Items in a Dictionary
# d = {1:10,2:20,3:30}
# key = 1
# value = 1
# for i,j in d.items():
#     key *= i
#     value *= j
# print("Keys :- ",key)
# print("Values :- ",value)


#9.Remove Given Key from a Dictionary
# d = {1:10,2:20,3:30}
# print(d)
# d.pop(2)
# print(d)


#10.Sum of Items in a Dictionary
# d = {1:10,2:20,3:30}
# key = 0
# value = 0
# for i,j in d.items():
#     key += i
#     value += j
# print("Keys :- ",key)
# print("Values :- ",value)