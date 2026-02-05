# linux .sh file and its working : in linux .sh file contain the executable file of linux shell commands 

'''so for creating a shell script cmd :- touch notes.sh 
checking the file permission          :- ls -l notes.txt
giving it the executable permission   :- chmod +x notes.sh

to run the file (execute it):- ./notes.sh cmd is used  '''

# To Handle Process In Linux We Have The : ps command 

# ps : process state  show the process of current state

# ps -ef : it will show all the currently running process only 

# and we also need to filter the process so for to filter all the
# process in linux we have to use the 

# ps aux | grep bash : this will tell us about how many of the process have
#                       an involvement of the bash process 

# it work in way like ps then the aux and with a pipe | name if the file we want to filter 
# in this case we are having the base process 

# How to kill a running process  :

# first we need the process id :  top  :- will tell us about the process id 

''' and in second step we will run the : kill 2025 (pid) 
it will terminate the process with this name and the id '''

# And For Monitor running process and the summary of the process we can use the top 
# command because monitoring will helps developer to understand about their process state and the activity 

# # ex:- top

# top - 11:05:34 up 54 min,  3 users,  load average: 0.00, 0.00, 0.00
# Tasks: 110 total,   1 running, 109 sleeping,   0 stopped,   0 zombie
# %Cpu(s):  0.0 us,  0.3 sy,  0.0 ni, 82.0 id,  0.0 wa,  0.0 hi,  0.0 si, 17.
# MiB Mem :    957.3 total,    524.1 free,    327.9 used,    261.4 buff/cache
# MiB Swap:      0.0 total,    

'''Htop :- need to install it first before using and the '''

# htop :- will display it in a well structure manner 

# to know about the status code and response of our api or web app 

# curl cmd is used : curl url or api

# extended version of curl 

# curl -I api(url):- 

# it will show all headers of api or url 

# like :- HTTPS, X-powered (tech stack), connection : keep connection
