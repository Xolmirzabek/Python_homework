
#Given a side of square. Find its perimeter and area.
a=int(input('Bo\'yining uzunligi: '))
b=int(input('Ening uzunligi: '))
S=a*b
P=2*(a+b)
print('Yuzi S=',S)
print('Yon tomonlar yig\'indisi P=',P)

#Given diameter of circle. Find its length.
import math

Diametr = float(input("Doiraning Diametr kiriting: "))
uzunlik = 2 * math.pi * (Diametr/2)

print(f"Doiraning uzunligi: {uzunlik}")

#Given two numbers a and b. Find their mean.
a=int(input('1-sonni kiriting: '))
b=int(input('2-sonni kiriting: '))
c=(a+b)/2
print(c)
#Given two numbers a and b. Find their sum, product and square of each number.
a=int(input('1-sonni kiriting: '))
b=int(input('2-sonni kiriting: '))
S=a+b #Finding sum of numbers 
P=a*b #Finding product of numbers
Sqa=a*a #Finding 1st number square 
Sqb=b*b #Finding 2nd number square 
print('Sum of numbers',S)
print('Product of numbers',P)
print('Square of a ', Sqa)
print('Square of b ', Sqb)
