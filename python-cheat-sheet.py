## In case you feel rusty in Python or never even used it, here you can find the basic syntax and declarations in Python!

## Variables
price = 10
rating = 4.9
course_name = 'Python for Beginners'
is_published = True

birth_year = int(input('Birth year: ')) ## Taking user input from the console

##Conditional statements
is_hot = True
is_cold = False
if is_hot:
 print('hot day')
elif is_cold:
 print('cold day')
else:
 print('beautiful day') 

## Logical Operators
if is_hot and is_cold:
    print('Thats a weird weather forecast!')

## Loops
i = 1
while i < 5:
 print(i)
 i += 1

## For Loop
for i in range(1, 5):
 print(i)

##Lists
numbers = [1, 2, 3, 4, 5]

numbers[0]              # returns the first item
numbers[1]              # returns the second item
numbers[-1]             # returns the first item from the end
numbers[-2]             # returns the second item from the end
numbers.append(6)       # adds 6 to the end
numbers.insert(0, 6)    # adds 6 at index position of 0
numbers.remove(6)       # removes 6
numbers.pop()           # removes the last item
numbers.index(1)        # returns the index of first occurrence of 8
numbers.clear()         # removes all the items
numbers.sort()          # sorts the list
numbers.reverse()       # reverses the list
numbers.copy()          # returns a copy of the list 

## Tuples, read-only lists
coordinates = (1, 2, 3)

## Dictionaries
customer = {
 'name': 'John Smith',
 'age': 30,
 'is_verified': True
}

customer['name'] # returns “John Smith”
# customer['type'] # throws an error
customer.get('type', 'silver') # returns “silver”
customer['name'] = 'new name'

##Functions
def greet_user(name):
 print(f'Hi {name}')
       
greet_user('John')

#Classes
class Point:
 def __init__(self, x, y):
    self.x = x
    self.y = y
 
 def move(self):
    print('move')