Homework: List and Tuple Exercises
1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.
list_fruits=['apple','banana','mango','orange','peach']
list_fruits[3-1]

2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.
l1_numbers=[1,5,52,5,8,52,74,14,15]
l2_numbers=[45,100,152,47,26,78,93,44]
print(l1_numbers+l2_numbers) # this first way 
l2_numbers +=l1_numbers # We concatenate in the l2_numbers list
print(l2_numbers) 
3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
l1_numbers=[1,5,52,5,8,52,74,14,15]
print(l1_numbers[0]+l1_numbers[len(l1_numbers)//2]+l1_numbers[len(l1_numbers)-1])

4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.
l1_movies=['Wednesday','Squid Game','Fors vs Ferrari','Baxodir Yalangto\'sh','Padington','Titanic']
l1_movies_tuple=tuple(l1_movies)
type(l1_movies_tuple)
5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.
l1_Cities=['Tashkent','New York','Paris','Tokyo','Seul']
if 'Paris' in l1_Cities:
    print('There is Paris in cities_names')
else: 
        print('There is not  Paris in cities_names')

6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.
l1_numbers=[1,5,52,5,8,52,74,14,15]
duplicate_l1_numbers=l1_numbers.copy() # I copy method is used to duplicate the list
print(duplicate_l1_numbers) # For knowing the result of duplication

7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.
l1_numbers=[1,5,52,5,8,52,74,14,15] 
l1_numbers[0], l1_numbers[-1] = l1_numbers[-1], l1_numbers[0]  # Swap first and last elements
print(l1_numbers)  # Print the modified list to see the result

8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
t1_numbers=(1,2,3,4,5,6,7,8,9,10)
print(t1_numbers[3:8])  # Print a slice from index 3 to 7 (exclusive)
9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.
lc_colors=['red','blue','green','blue','yellow','blue']
print(lc_colors.count('blue'))  # Count occurrences of 'blue' in the list
10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".
t1_animals=('cat', 'dog', 'lion', 'tiger', 'elephant')
print(t1_animals.index('lion'))  # Find the index of 'lion' in the tuple

11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.
t1_numbers=(1,2,3,4,5)
t2_numbers=(6,7,8,9,10)
t3_numbers=t1_numbers+t2_numbers
print(t3_numbers)

12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.
l1_numbers=[1,5,52,5,8,52,74,14,15]
t1_numbers=(1,2,3,4,5,6,7,8,9,10)
print(len(l1_numbers))  # Length of the list
print(len(t1_numbers))  # Length of the tuple       

13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.
t1_numbers=(1,2,3,4,5)
l1_numbers=list(t1_numbers)
print(l1_numbers)

14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.
t1_numbers=(1,2,3,4,5)
print(max(t1_numbers))  # Find the maximum value in the tuple
print(min(t1_numbers))  # Find the minimum value in the tuple
15. Reverse a Tuple
Create a tuple of words and print it in reverse order.
t1_words=('apple', 'banana', 'cherry', 'date')
print(t1_words[::-1])  # Print the tuple in reverse order
