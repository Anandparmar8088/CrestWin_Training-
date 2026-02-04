# Control flow statements in Python:
# Control flow refers to the order in which statements execute within a program.
# Control flow helps developers manage the flow of execution — which statements execute in a program.


# In Python, control flow is divided into:

# Conditional statements: if-else, if-elif-else ladder
# Loop statements: for, while
# Jumping statements: break and continue


# if-else: executes the if block of code if a condition is matched,
# and the else block if it is not matched.

i = 18

if i >= 18:
    print("you can drive")
else:
    print("you can not drive")


if i == 10:
    print("hii")
elif i == 20:
    print("hello")
elif i == 25:
    print("hey")
else:
    print("good bye")


# Jump statements: if we want to go to a specific part of the code
# based on a condition, we can use jump statements.

# break: terminates the loop or iteration and exits the loop

for i in range(1, 10):
    if i == 8:
        break
    else:
        print("you are invited")


# continue: used to skip the current iteration based on a condition

for i in range(1, 15):
    if i == 9:
        continue
    else:
        print("you are invited")


# Loops: execute a specific block of code for a range
# or while the condition is true

# for loop: uses the range function to execute the block
# of code a specific number of times

lst = []
for i in range(1, 5):
    if i % 2 == 0:
        print("even")
    else:
        print("not")


# while loop: iterates until the condition becomes false

while i < 10:
    print("hii")
    i += 1


def add(a, b):
    return a + b
