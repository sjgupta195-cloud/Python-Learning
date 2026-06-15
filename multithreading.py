''' it actually helps to make process faster like u can download
    multiple files simaltaneously using thread ,
    "IT IS A WORKER IN A PROCESS" , but it doesnt usally means it 
    make ever process faster like in haevy calcualation it can 
    be slow i.e. ehy we use multiprocess in it .'''


# BASIC SYNTAX

import threading 

def task():
    print ("working...")

thread = threading.Thread(target = task)

thread.start()