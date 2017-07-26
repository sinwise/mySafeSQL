#!/usr/bin/python

##
##
## mySafeSQL
##
## https://github.com/sinwise/mysafesql.git
## http://www.sinwise.com/mysafesql
##
##

# Modules

import os
import ConfigParser
import time
import datetime

# Colors Definition

def printRed(prt):          print("\033[91m {}\033[00m" .format(prt))
def printGreen(prt):        print("\033[92m {}\033[00m" .format(prt))
def printYellow(prt):       print("\033[93m {}\033[00m" .format(prt))
def printLightPurple(prt):  print("\033[94m {}\033[00m" .format(prt))
def printPurple(prt):       print("\033[95m {}\033[00m" .format(prt))
def printCyan(prt):         print("\033[96m {}\033[00m" .format(prt))
def printLightGray(prt):    print("\033[97m {}\033[00m" .format(prt))
def printBlack(prt):        print("\033[98m {}\033[00m" .format(prt))

# Loading variables defined within mysafesql.cfg

backup_enabled      = [DAILY_BACKUPS_ENABLED, WEEKLY_BACKUPS_ENABLED, MONTHLY_BACKUPS_ENABLED]
backup_path_check   = [BACKUP_PATH_DAILY, BACKUP_PATH_WEEKLY, BACKUP_PATH_MONTHLY]

for backup_path_defined in backup_path_check:
    if not backup_path_defined:
        prLightPurple("Skipping " + backup_path_defined + " folder check/create step as this hasn't been defined...")
    else:
        if not os.path.exists(backup_path_defined):
            os.makedirs(backup_path_defined)
            prYellow("Creating backup folders for " + backup_path_defined + "...")
        else:
            prGreen("Folder " + backup_path_defined + " already exists, moving to the next step...")





#print "checking for databases names file."
# if os.path.exists(DB_NAME):
#    file1 = open(DB_NAME)
#    multi = 1
#    print "Databases file found..."
#    print "Starting backup of all dbs listed in file " + DB_NAME
#else:
#    print "Databases file not found..."
#    print "Starting backup of database " + DB_NAME
#    multi = 0

# Starting actual database backup process.
#if multi:
#   in_file = open(DB_NAME,"r")
#   flength = len(in_file.readlines())
#   in_file.close()
#   p = 1
#   dbfile = open(DB_NAME,"r")

#   while p <= flength:
#       db = dbfile.readline()   # reading database name from file
#       db = db[:-1]         # deletes extra line
#       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
#       os.system(dumpcmd)
#       p = p + 1
#   dbfile.close()
#else:
#   db = DB_NAME
#   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
#   os.system(dumpcmd)
#
#print "Backup script completed"