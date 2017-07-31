#!/usr/bin/python

##
##
## mySafeSQL
##
## https://github.com/sinwise/mysafesql.git
## http://www.sinwise.com/mysafesql
##
##

import imp, sys, platform
sys.path.append('')
from mysafesqlColors import *
global isCentOS, isUbuntu

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
        printRed("Aborting, Mac OS is not currenly supported.")
        exit()
    
    elif sys.platform.startswith('openbsd'):
        printRed("Aborting, OpenBSD is not currenly supported.")
        exit()

    if isCentOS:
        
        printGreen("CentOS found on your server, checking packages...")

        import yum

        yb              = yum.YumBase()
        yb.conf.cache   = 1 # enable cache
        installed       = yb.rpmdb.returnPackages()
        searchlist      = ['name']
        packages        = ['pigz']

        for package in packages:
        
            if package in installed:
                print('{0} is already installed, skipping...'.format(package))
            else:
                print('Installing {0}'.format(package))
                yb.install(package)
                yb.resolveDeps()
                yb.buildTransaction()
                yb.processTransaction()
        
        import yum
        yb          = yum.YumBase()
        searchlist  = ['name']
        arg         = ['pigz']
        matches     = yb.searchGenerator(searchlist,arg)
        
        for (package, matched_value) in matches:
        
            if package.name == 'pigz':
                yb.install(package)
                yb.buildTransaction()
                yb.processTransaction()

    elif isUbuntu:

        printGreen("Ubuntu found on your server, checking packages...")

        import apt
        ag          = apt.AptBase()
        searchlist  = ['name']
        arg         = ['pigz']
        matches     = ap.searchGenerator(searchlist,arg)
        
        for (package, matched_value) in matches:
        
            if package.name == 'pigz':
                ap.install(package)
                ap.buildTransaction()
                ap.processTransaction()
