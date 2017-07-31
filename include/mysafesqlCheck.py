#!/usr/bin/python

##
##
## mySafeSQL
##
## https://github.com/sinwise/mysafesql.git
## http://www.sinwise.com/mysafesql
##
##

# import os

# def CheckSystem():
#    print os.uname()

    # base = yum.YumBase()
    # if base.rpmdb.searchNevra(name='mysqlpump'):
    #     print "installed"
    # else:
    #     print "not installed"

import mmap, imp, sys
sys.path.append('')
from mysafesqlColors import *

def CheckSystem():

    try:
        with open('/etc/redhat-release', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(b'CentOS') == -1:
                isCentOS = True
            if s.find(b'Ubuntu') == -1:
                isUbuntu
            if s.find(b'CentOS') != -1 or s.find(b'Ubuntu'):
                isNotSupported = True
    except:
        printRed("Aborting, opertaing system not supported!")
        exit()

    if isNotSupported:
        printRed("Aborting, opertaing system not supported!")
        exit()

    if isCentOS:
        printGreen("CentOS found...")

    if isUbuntu:
        printGreen("Ubuntu found...")
