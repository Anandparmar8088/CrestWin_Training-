#  Data types in python
''' in python data types are way to classify data item ''' 
        
''' in python we can divide the data types in several types '''


'''  INT : used to store the numeric data 
'''
# int data type
A = 10

# float data type 
B = 10.2

#  complex the mix of real and imagenary data
i = 0
# c = 2+3i  
# here i is the imagenary part 

''' Boolean Data type in python '''
# this data type used in control statement 
a = True 

if 5>10:
    a =False
    print("True and Right ")
    
# Now the sequence data type in python

''' 1) list :- is indexed collection of data where firt element sart  with 0 
             list is mutable , can have duplicate data type 
             and have several in built method support 

'''

lst = [1,2,3,5]

print(lst)

#   list inbulit mehtod : append add the data at the end of the list 
# extend will add multiple value at the end and many more 


# touple 

# touple is another bulit in data type in python which is indexeds and indexing start with 0 

# touple are not mutable 
tp = ('Apple','Banana','Mango')
print(tp)


# string 

# String is another bulit in data type in python which is aslo immutable 

st = 'Anand'


# we can not change the string once it is ccreated because   it maintain a hash table internally and
# becuse the rafernce get changed if we do any changes in string  
st = 'Anand '
st = st+'parmar'

print(st)

# in this case a new obj is created here and the changes are performed there 
# that is why string are immutable in python



# dictionary in python : dictionary is the collection items 

'''items are nothing but key and value pairs 
where key  = any immutable data type like tuple
and value  = any mutable data type  '''

print(__doc__)
New_Dic = {"Name":"Anand","Age":20,"city":"Indore "}

print(New_Dic)

# also use loops to print it 

for keys , values in New_Dic.items():
    print(keys,values)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# sequence data type : indexed based acces 

# no nsequence based data type : hash bssed 


# Sequence = position-based memory → indexing
# Non-sequence = hash-based memory → no indexing