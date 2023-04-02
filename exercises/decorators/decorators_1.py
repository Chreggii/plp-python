def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_helo():
    print("Hello")


say_helo = my_decorator(say_helo)
say_helo()

# -----------------------------------------------------------------------------------


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_helo():
    print("Hello")


say_helo()
