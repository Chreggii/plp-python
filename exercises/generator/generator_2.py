# Generator Function example
import sys

 
# List comprehension  
nums_squared_list = [i ** 2 for i in range(100)] 

for i in nums_squared_list:
    print(i, end=' ')

print('\n')

# Generator Expression  Syntax
nums_squared_gc = (i ** 2 for i in range(100)) ##Creates a Generator object that can be iterated
for i in nums_squared_gc:
    print(i, end=' ')
print('\nMemory in Bytes',sys.getsizeof(nums_squared_list))
print('Memory in Bytes with the Generator Object', sys.getsizeof( nums_squared_gc))  