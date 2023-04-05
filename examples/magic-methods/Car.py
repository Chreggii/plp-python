

class Car(object):
    ## Same behavior as the new keyword in other languages like Java
    ## Gets called first when the class is instantiated
    ## returns the newly instantiated object
    def __new__(cls,name):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    
    ## Afterwards, init is called
    ## Usually, you can define what happens with the passed arguments when the object is created here
    def __init__(self,name):
        print ("__init__ magic method is called")
        self.name=name

    ## Defines how a string should represent the object.
    def __str__(self):
        return 'Car name ' + self.name
       



car1 = Car('Skoda')
print(dir(car1)) ##Shows how many magic methods are inherited
print(car1)

print('Car name Skoda')