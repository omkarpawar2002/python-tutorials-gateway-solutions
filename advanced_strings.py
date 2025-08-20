# 1.Python program to Count the Occurrence of a Character in a String.
'''
string = input("Enter any string :- ")
ch = input("Enter any character :- ")
print(f"Total count of occurances of {ch} is :- {string.count(ch)}")
'''

# 2.Python Program to Count Character Frequency in a String
'''
string = input("Enter any string :- ")
d = {}
for i in string:
    if(i not in d):
        d[i] = 1
    else:
        d[i] += 1
print(d)
'''

# 3.Python program to Count Total Characters in a String
'''
string = input("Enter any string :- ")
print(f"Total characters in string are :- {len(string)}")
'''

# 4.Python program to Count the Total Number of Words in a String
'''
string = input("Enter any string :- ")
st = string.split()
print(f"Total number of words in st is :- {len(st)}")
'''

# 5.Python program to Count Vowels in a String
'''
string = input("Enter any string :- ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
total = 0
for i in string:
    if(i in vowels):
        total += 1
print(f"Total Count Of Vowels are :- {total}")
'''

# 6.Python program to Count Vowels and Consonants in a String
'''
string = input("Enter any string :- ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
count_vowels = 0
count_consonants = 0
for i in string:
    if(i in vowels):
        count_vowels += 1
    else:
        count_consonants += 1
print(f"Total Count Of Vowels are :- {count_vowels}")
print(f"Total Count Of Consonants are :- {count_consonants}")
'''

# 7.Python program to Count Alphabets Digits and Special Characters in a String
'''
string = input("Enter any input :- ")
special_symbols = ['!','@','#','$','%','^','.']
alphabet = 0
digit = 0
symbols = 0
for i in string:
    if(i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        alphabet += 1
    elif(i >= '0' and i <= '9'):
        digit += 1
    elif(i in special_symbols):
        symbols += 1
print(f"\n Total alphabets are :- {alphabet} \n digits are :- {digit} \n special symbol are :- {symbols}")
'''

# 8.Python program to Replace Blank Space with Hyphen in a String
'''
string = input("Enter any input string :- ")
print(string)
print(string.replace(' ','-'))
'''

# 9.Python program to Replace Characters in a String
'''
string = input("Enter any input string :- ")
print("Original character :- ",string)
updated_char = string.replace('e','z')
print("Updated character :- ",updated_char)
'''

# 10.Python program to Remove Odd Characters in a String
'''
string = input("Enter any input string :- ")
print("Original character :- ",string)
st = ''
for index,value in enumerate(string):
    if(index % 2 != 0):
        st += value
string = st
print("Final updated :- ",string)
'''

# 11.Python program to Remove Odd Index Characters in a String
'''
string = input("Enter any input string :- ")
print("Original character :- ",string)
st = ''
for index,value in enumerate(string):
    if(index % 2 == 0):
        st += value
string = st
print("Final updated :- ",string)
'''

# 12.Python program to Remove the First Occurrence of a Character in a String
'''
string = input("Enter any input string :- ")
ch = input("Enter any character :- ")
li = list(string)
print(li)
li.remove(ch)
string = ''.join(li)
print(string)
'''

# 13.Python program to Remove Last Occurred Character in a String
'''
string = input("Enter any input string :- ")
print("Original :- ",string)
ch = input("Enter any character :- ")
li = list(string)
li.reverse()
li.remove(ch)
li.reverse()
string = ''.join(li)
print("Updated :- ",string)
'''

# 14.Python Program to Remove Punctuations from a String
'''
string = input("Enter any string input :- ")
print("Original string :- ",string)
new = ''
for i in string:
    if(i.isalpha() or i == ' '):
        new += i
print(new)
'''

# 15.Python program to Reverse a String
'''
string = input("Enter any string input :- ")
print("Original string :- ",string)
updated = string[::-1]
print("Updated string :- ",updated)
'''