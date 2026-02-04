# Modules in python : - module in python is a file that contain python code (defiantion and Statement) 
                    #   module helps programs to maintain in saperate files so 
                    #   it make program easy to maintain and reuse 
                    
# creating a module in py:
    
def add(a,b):  # a simple python module 
    return(a+b)


# we can import a module to a program : using 

import Control_flow 
# this will import th e controll from from the same folder 
print(Control_flow.add(10,20))


# Type of module in python 

# 1 built-in module : os, random, math \
    
import os 

if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    print("file does not exist")
    

# 2 user defined : specified by the user it self for his own purpose 
import Control_flow 
print(Control_flow.add(10,20))

#3  External :-third party module
# 
# : installed by pip install :- numpy pandas








