# Generator Function example
import sys

# normal function
def count_Numbers(): 
  
    #some complex logic, used in a reaaaaalllyy big data set

    print('results from each data point')





 
# List comprehension  
nums_squared_list = [i ** 2 for i in range(100)]  
print('Memory in Bytes',sys.getsizeof(nums_squared_list))

# Generator Expression  Syntax
nums_squared_gc = (i ** 2 for i in range(100))  ##Creates a Generator object that can be iterated
print('Memory in Bytes', sys.getsizeof( nums_squared_gc))  