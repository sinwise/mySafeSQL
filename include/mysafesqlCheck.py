#!/usr/bin/python

##
##
## mySafeSQL
##
## https://github.com/sinwise/mysafesql.git
## http://www.sinwise.com/mysafesql
##
##

import imp, sys, os, platform
sys.path.append('')
from mysafesqlColors import *

def CheckSystem():

    if not platform.linux_distribution() == "CentOS":
        printRed("Nope...")
        print platform.linux_distribution()
        exit()
    else:
        printGreen("Found CentOS installed...")

    # try:
    #     with open('/etc/redhat-release', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    #         if s.find(b'CentOS') == -1:
    #             isCentOS = True
    #         if s.find(b'Ubuntu') == -1:
    #             isUbuntu
    #         if s.find(b'CentOS') != -1 or s.find(b'Ubuntu'):
    #             isNotSupported = True
    # except:
    #     printRed("Aborting, opertaing system not supported!")
    #     exit()

    # if isNotSupported:
    #     printRed("Aborting, opertaing system not supported!")
    #     exit()

    # if isCentOS:
    #     printGreen("CentOS found...")

    # if isUbuntu:
    #     printGreen("Ubuntu found...")
