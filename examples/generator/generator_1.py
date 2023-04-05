# Generator Function example

# normal function
# imagine that each integer is huuuuugee and takes 10 Megabytes of space to store in the memory
def some_function(n):
      
      return n


 



#Same function but with the yield keyword
def some_functionn(n):

            
            yield n ## Instead of the return keyword, the yield keyword produces the values but does not store the entire sequence inside the memory.
            yield n + 3


print(some_function(5))
print(some_functionn(5))

# In order to get the the value now, you need to iterate over the generator function now

# for i in some_functionn(5):
#         print(i)

## or through the next() function
# x = some_functionn(5)
# print(next(x))
# print(next(x))

