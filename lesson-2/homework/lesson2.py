# Homework Exercises

## 1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
import datetime
x=datetime.datetime.now()
a=int(input('your year of birth, please in number'))
c=x.year-a
print('your age: ',c)

## 2. Extract Residence Area
Extract the residence area from the following text:
```python
txt = "I'am John. I am from London"
txt.split()[5]

## 3. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.
txt=str(input('Hoxlagan so\'zingizni kiriting: '))
txt=txt[::-1]
## 4. Count Vowels
Write a Python program that counts the number of vowels in a given string.
txt=str(input('Hoxlagan gap va so\'zingizni yozing: ' ))
a=txt.count('a')
o=txt.count('o')
i=txt.count('i')
u=txt.count('u')
e=txt.count('e')
print('Jami unlilar:', a+o+i+u+e)

## 5. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.
a=input('Enter numbers seperated by spaces: ')
num_list=list(map(int,a.split()))
print(max(num_list))
## 6. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
txt=str(input('Hoxlagan so\'zingizni kiriting: '))
ptxt=txt[::-1]
if txt=ptxt:
    print('This word is palindrome:',txt)
else
    print('This word isn\'t palindrome:', txt)

## 7. Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.
email=input('Enter your email: ')
if '@' in email:
    print(email.split('@')[1])
else:
    print("Given email format is incorrect. With'@'.")
## 8. Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.
email=input('Enter your email: ')
if '@' in email:
    print(email.split('@')[1])
else:
    print("Given email format is incorrect. With'@'.")
