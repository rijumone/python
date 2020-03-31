def foo(bar):
    return bar + 1

print(foo)
print(foo(4))
print(type(foo))


def call_foo_with_arg(func, arg):
    return func(arg)

print(call_foo_with_arg(foo, 3))


print "======= Example 1 start ======="

def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper # this line is return of my_decorator; returning the above function


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()

print "======= Example 1 end ======="

print "======= Example 2 start ======="

def my_decorator(some_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")

just_some_function = my_decorator(just_some_function)

just_some_function()

print "======= Example 2 end ======="