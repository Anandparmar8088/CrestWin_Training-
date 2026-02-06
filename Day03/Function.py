# Functions are blocks of code that help in reusability,
# code readability, and maintainability.
# They execute only when we call the function fun().


# Types of functions in Python

# 1. Built-in functions: int, type() 

# 2. User-defined functions: add()

# 3. Lambda functions: small anonymous functions,
#    used for single-time functionality

# 4. Recursive functions: execute until a specific condition is met



# Types of arguments in Python:
# 1) Positional arguments
# 2) Keyword arguments
# 3) Default arguments
# 4) *args
# 5) **kwargs


# Positional arguments
def add(Num1, Num2):
    return Num1, Num2
add(1,2)

# Keyword arguments
def Info(name, age):
    return name, age

Info(age="20", name="Ajay")


# Default arguments
def Greeting(name, Greet="Hello"):
    pass

Greeting("Anand")


# *args
# Takes arguments as a tuple

def my_fun(*args):
    for arg in args:
        print(arg)

my_fun("my", "fun", "great")


# **kwargs
# Takes arguments in the form of a dictionary

def demo_fun(**args):
    pass

demo_fun(name="anad", age=20)

# The arguments are in key-value pairs
