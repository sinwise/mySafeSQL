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

supported_linux_oses    = ["CentOS", "Ubuntu"]
installed_packages      = ["mysqlpump", "pigz"]

def CheckSystem():

    if sys.platform.startswith('linux'):
        distro, version, dist_id = platform.linux_distribution()
        if distro == 'CentOS':
            printGreen("CentOS found...")
        elif distro in ('Debian', 'debian'):
            printGreen("Debian found...")
        elif distro == 'Fedora':
            printGreen("Fedora found...")
        elif distro == 'Gentoo Base System':
            printGreen("Gentoo found...")
        elif distro in ('Mint', 'LinuxMint'):
            printGreen("Mint found...")
        elif distro == 'Ubuntu':
            printGreen("Ubuntu found...")
        else:
            printRed("Aborting, your operating system is not currenly supported.")

        args['version'] = version
        args['dist_id'] = dist_id

    elif sys.platform.startswith('darwin'):
            # TODO Support Darwin platforms that aren't OS X.
            #osx_version = platform.mac_ver()[0]
        printRed("Mac OS is not currenly supported")

    elif sys.platform.startswith('openbsd'):
            # cls = OpenBSDBootstrapper
            # args['version'] = platform.uname()[2]
        printRed("OpenBSD is not currenly supported")

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
