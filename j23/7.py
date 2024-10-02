def ali(func):
    def wrapper():
        # Do stuff before func...
        print("Before func!")
        func()
        # Do stuff after func...
        print("After func!")

    return wrapper


@ali
def foo():
    print("Hello World!")


foo()
# Before func!
# Hello World!
# After func!
