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

installed_packages      = ["mysqlpump", "pigz"]

def CheckSystem():

    if sys.platform.startswith('linux'):
        distro, version, dist_id = platform.linux_distribution()
        if "CentOS" in distro:
            isCentOS = True
        elif "Ubuntu" in distro:
            isUbuntu = True
        else:
            printRed("Aborting, your operating system is not currenly supported.")
    elif sys.platform.startswith('darwin'):
        printRed("Mac OS is not currenly supported")
        exit()
    elif sys.platform.startswith('openbsd'):
        printRed("OpenBSD is not currenly supported")
        exit()

    if isCentOS:
        printGreen("CentOS found on your server, checking packages...")


    if isUbuntu:
        printGreen("Ubuntu found on your server, checking packages...")
