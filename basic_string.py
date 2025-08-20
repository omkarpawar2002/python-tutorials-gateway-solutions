# 1.Python Program for ASCII Value of a Single Character
'''
ch = input("Enter any character :- ")
print(ord(ch))
'''

# 2.Python program to print ASCII Value of Total Characters in a String
'''
name = input('Enter anything :- ')
for i in name:
    print(i,'----->',ord(i))
'''

# 3.Python program to Concatenate Strings
'''
st1 = input("Enter first string :- ")
st2 = input("Enter second string :- ")
print(st1 + ' ' + st2)
'''

# 4.Python program to Convert String to Uppercase
'''
st = input("Enter input :- ")
print(st.upper())
'''

# 5.Python program to Convert String to Lowercase
'''
st = input("Enter input :- ")
print(st.lower())
'''

# 6.Python program to Copy a String
'''
st = input("Enter any input :- ")
new = st[::]
print(st,id(st))
print(new,id(new))
'''

# 7.Python program to check Palindrome or Not
'''
st = input("Enter any input :- ")
if(st == st[::-1]):
    print("Yes It Is Palindrome")
else:
    print("No It'S Not A Palindrome")
'''

# 8.Python Program to Check If Two Strings are Anagram
'''
st1 = input("Enter first string :- ")
st2 = input("Enter second string :- ")
if(sorted(st1) == sorted(st2)):
    print("Yes It Is Anagram")
else:
    print("No It's Not Anagram")
'''

# 9.Python program to Print the First Occurrence of a Character in a String
'''
st = input("Enter any input :- ")
print(st.find('e'))
'''

# 10.Python program to Print the Last Occurrence of a Character in a String
'''
st = input("Enter any input :- ")
print(st.rfind(st[2]))
'''

# 11.Python program to Print Characters in a String
'''
st = input("Enter any input :- ")
for i in st:
    print(i)
'''

# 12.Python program to find String Length
'''
st = input("Enter any input :- ")
print("Length of string is :- ",len(st))
'''

# 13.Total Occurrence of a Character in a string
'''
st = input("Enter any input :- ")
print(st.count(st[2]))
'''

# 14.Toggle Characters Case
'''
st = input("Enter any input :- ")
new = ''
for i in st:
    if(i.islower()):
        new += i.upper()
    else:
        new += i.lower()
print(new)
'''