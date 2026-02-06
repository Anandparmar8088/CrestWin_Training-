# Modules in Python:
# A module in Python is a file that contains Python code
# (definitions and statements).
# Modules help programs to be maintained in separate files,
# making programs easier to maintain and reuse.


# Creating a module in Python:

def add(a, b):  # a simple Python module
    return a + b


# We can import a module into a program using:

import Control_flow
# This will import the control flow module from the same folder
print(Control_flow.add(10, 20))


# Types of modules in Python

# 1. Built-in modules: os, random, math

import os

if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    print("file does not exist")


# 2. User-defined modules: specified by the user for their own purpose

import Control_flow
print(Control_flow.add(10, 20))


# 3. External modules (third-party modules)
# Installed using pip, for example: numpy, pandas

pip install django 
pip install djangorestframework  