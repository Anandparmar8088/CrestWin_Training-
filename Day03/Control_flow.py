# control flow statement in python :- control flow refers to the order in which statement execute within the program 
# control flow helps dev in manage the flow of execution  which statement execute in a program  


# in pyhton control flow is divided in :
     
    #  conditional statement : if-else , if-else ladder 
    #  loop statement: for ,while 
    #  jumping statement : break and continue
     

# if else: execute if   block of code if a condtion is matched  and else block if not matched 

i = 18

if i >=18:
    print("you can drive")
else :
    print("you can not drive")
    

    
if i==10:
    print("hii")
elif i==20:
    print("hello")
elif i ==25:
    print("hey")
else:
    print("good by")

# jump statement : if we want to go to specific part of the code based on the condition we can use jump statement 

# break:- terminate the loop or  itration and get out of iteration 

for i in range(1,10):
    if i ==8:
        break
    else:
        print("you are invited ")
    
# continue : used to skips the current iteration based in condition 

for i in range(1,15):
    if i ==9:
        continue
    else:
        print("you are invited ")


# loops: specific block of code execution in a range or while the condion is true 

# for loop : it uses the range function to execute the block of code for specific number of times 
lst = []
for i in range(1,5):
    if i%2==0:
        print("even")
    else:
        print("not")

# while: iterate until the condition get false
while i <10:
    print("hii")
    
    i+=1
    
def add(a,b):
    return(a+b)



    