'''Virtual enviroment: virtual enviroment allow you to  manage dependencies saparately for all the differant project that you make.
                    to privent the conflicts in bw the different dependancies 
                    to privent conflicts between different py projects  
                    virtual env provide the indipenadate lightweight isolated py dev enviroment
                    

how to make virtual enviroment by commands : 
    
       python -m   newpro_venv       venv
         |          |           |
      python  |    Name     | virtual env
      version |   ofvirtual |
                
                     
                     
to activte the virtual env in windows : 
    
    venc/Scripts/activate 
    
to ensure it is activate we can see the (.venv) in terminal 


To Deactivate virtual env command :

Deactivate 


Now to install the dependencies :
    pip install dajango
    
to see how many dependencies we do have in our project cmd:
    pip list 
    
    django 
    corsheader we have drf all .etc 
    



How to enable the virtual env in IDE(vs code):
    
   1) ctrl+shift+p
   2) Select create enviroment 
   3) Select venv 
   4) python latest version (Or the version you want)
   5) Activate the env : venv/Scritps/activate
   

Why We  need the virtual enviroment ?

the ANSWEER is the  PYTHTHON IS not good in handling DEPENDENCIES.
    
    if we did not specify the virtual enviroment than it will add external dependencies  into the  the base pyhton installion 
    in the  Site/packages folder 
    '''
   
   
   
   
# Folder structure of venv :-   
# venv\
# │
# ├── Include\               :- have c headerfiles 
# │
# ├── Lib\                   :- external pyhton packages 
# │   │
# │   └── site-packages\
# │
# ├── Scripts\               :- executable file 
# │   ├── Activate.ps1
# │   ├── activate
# │   ├── activate.bat
# │   ├── deactivate.bat
# │   ├── pip.exe
# │   ├── pip3.12.exe
# │   ├── pip3.exe
# │   ├── python.exe
# │   └── pythonw.exe
# │
# └── pyvenv.cfg          :- brain of env has:    HOME  location of venv installation 
#                                            :    include_system_file = False  
#                                            :    version 3.2.3
                                                            

'''
pip inside the virtual env : 
    
    pip is used to install the dependencies inside the virtual env not in system 
    
    using the cmd : 1) pip install Dajango --  it will install the django 
                    2) pip list            --  show all the dependencies installed
                    3) pip --version       --  show the pip version and python version it is linkes to 
                                               (pip 23.3.1 from C:\Python311\Lib\site-packages\pip (python 3.11))



Note : dont push the virtual env in version controll  

instead create a   requirement.txt -> pyhton -m freez > requirement.txt                      
'''