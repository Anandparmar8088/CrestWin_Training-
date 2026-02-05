'''items are nothing but key and value pairs 
where key  = any immutable data type like tuple
and value  = any mutable data type  '''

print(__doc__)
New_Dic = {"Name":"Anand","Age":20,"city":"Indore "}

print(New_Dic)

# also use loops to print it 

for keys , values in New_Dic.items():
    print(keys,values)