# Generator Function example

# normal function
# imagine that each integer is huuuuugee and takes 10 Megabytes of space to store in the memory
def first_n(n):

   num, nums = 0, []
   while num < n:
    nums.append(num)
    num += 1
    return nums
 



#Same function but with the yield keyword
def firstn(n):
        num = 0
        while num < n:
            yield num ## Instead of the return keyword, the yield keyword produces the values but does not store the entire sequence inside the memory.
            num += 1
