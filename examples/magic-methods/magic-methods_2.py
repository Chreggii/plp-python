

class A(object):
    def __new__(cls):
         print("Creating instance")
         return object.__new__(cls)
  
    def __init__(self):
        print("Init is called")
  
a = A()
print(a)