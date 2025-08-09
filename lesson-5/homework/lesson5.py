Homework:

1.
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

 year=int(input('Enter year which you want: '))
if year%4==0 and year%100!=0 or year%400==0:
    print('Leap year')
else:
    print('Not a leap year')    

## 2. Conditional Statements Exercise

Given an integer, `n`, perform the following conditional actions:

- If `n` is **odd**, print `Weird`
- If `n` is **even** and in the inclusive range of **2 to 5**, print `Not Weird`
- If `n` is **even** and in the inclusive range of **6 to 20**, print `Weird`
- If `n` is **even** and **greater than 20**, print `Not Weird`
n=int(input("Enter a number: "))
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
```python
## Input Format
A single line containing a positive integer, `n`.

## Constraints
- `1 <= n <= 100`

## Output Format
Print `Weird` if the number is weird. Otherwise, print `Not Weird`.

## Sample Input 0
```
3
```

## Sample Output 0
```
Weird
```


3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop. 

Give two solutions.

Solution 1 with if-else statement.

Solution 2 without if-else statement.
```python
def find_even_numbers_with_if(a, b):
    """
    Finds even numbers between two integers a and b (inclusive) using if-else statements.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    list: A list of even numbers between a and b.
    """
    if a > b:
        a, b = b, a  # Ensure a is less than or equal to b

    return [num for num in range(a, b + 1) if num % 2 == 0]
