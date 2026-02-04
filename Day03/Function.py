# function are the block of code that which is helps in reusablity , code readablity and maintanablity 
# it will only execute when we call the function fun()

# type of function in py 

# 1 built  defined :- int , type()

# 2 user defined : - add()

# 3 lambda function : - small anonymus function , used for single time functionality 

# 4 recursive function : - until a specific condition is not met    

# type of aruments in py: -   1) posisational arguments 
#                             2) keywardsd arguments 
#                             3) default arguments 
#                             4) *args
#                             5) **kwargs
          
# posisational arguments                  
def add(Num1,Num2):  
    return Num1,Num2 


# keywardsd arguments
def Info(name, age):
    return name,age

Info(age="20", name="Ajay")  




# default arguments
def Greeting(name, Greet="Hello"):
    pass

Greeting("Anand")

# *args 
# take arguments as a touple 

def my_fun(*args):
    for arg in args: 
        print(arg)
my_fun("my","fun","great")

# **kwargs 
# it will take arguments in form of dictionary 

def demo_fun(**args):
    pass

demo_fun(name="anad", age=20,)

# the arguments in key value pair 
    




