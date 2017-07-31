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

import os, sys, socket, ConfigParser, imp, time, datetime
sys.path.append('include')
from mysafesqlColors import *
# from mysafesqlDaily import *
# from mysafesqlWeekly import *
# from mysafesqlMonthly import *

# Loading variables defined within mysafesql.cfg configuration file

def getVarFromFile(filename):
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()
getVarFromFile('config/mysafesql.cfg')
host_stamp = socket.gethostname() + "/" + time.strftime('%d-%m-%Y')

#### Daily Backups 

# CheckSystem()

if data.DAILY_BACKUPS_ENABLED:
    if not (data.DAILY_BACKUPS_RETENTION_PERIOD <= 0):
        if data.DAILY_BACKUPS_PATH:
            if not os.path.exists(data.DAILY_BACKUPS_PATH):
                os.makedirs(data.DAILY_BACKUPS_PATH + host_stamp)
                printYellow("Backup folder '" + data.DAILY_BACKUPS_PATH + host_stamp + "' has been created...")
            else:
                printGreen("Folder '" + data.DAILY_BACKUPS_PATH + host_stamp + "' exists, moving to the next step...")    
        else:
            printLightPurple("Skipping daily backups folder '" + data.DAILY_BACKUPS_PATH + host_stamp + "' folder check / create step as this hasn't been defined...")
    else:
        printLightPurple("Skipping daily backups as the rentention period is invalid, please change 'DAILY_BACKUPS_RETENTION_PERIOD'...")
else:
    printLightPurple("Skipping daily folder '" + data.DAILY_BACKUPS_PATH + host_stamp + "' check / create step as this has been disabled...")

#### Weekly Backups

if data.WEEKLY_BACKUPS_ENABLED:
    if not (data.WEEKLY_BACKUPS_START_DAY > 31) | (data.WEEKLY_BACKUPS_START_DAY < 1):
        if not (data.WEEKLY_BACKUPS_RETENTION_PERIOD <= 0):
            if data.WEEKLY_BACKUPS_PATH:
                if not os.path.exists(data.WEEKLY_BACKUPS_PATH):
                    os.makedirs(data.WEEKLY_BACKUPS_PATH + host_stamp)
                    printYellow("Backup folder '" + data.WEEKLY_BACKUPS_PATH + host_stamp + "' has been created...")
                else:
                    printGreen("Folder '" + data.WEEKLY_BACKUPS_PATH + host_stamp + "' exists, moving to the next step...")    
            else:
                printLightPurple("Skipping weekly backups folder '" + data.WEEKLY_BACKUPS_PATH + host_stamp + "' folder check / create step as this hasn't been defined...")
        else:
            printLightPurple("Skipping weekly backups as the rentention period is invalid, please change 'WEEKLY_BACKUPS_RETENTION_PERIOD'...")
    else:
        printLightPurple("Skipping weekly backups as the day value is invalid, please change 'WEEKLY_BACKUPS_START_DAY'...")
else:
    printLightPurple("Skipping weekly folder '" + data.WEEKLY_BACKUPS_PATH + host_stamp + "' check / create step as this has been disabled...")


#### Monthly Backups

if data.MONTHLY_BACKUPS_ENABLED:
    if not (data.MONTHLY_BACKUPS_RETENTION_PERIOD <= 0):
        if data.MONTHLY_BACKUPS_PATH:
            if not os.path.exists(data.MONTHLY_BACKUPS_PATH):
                os.makedirs(data.MONTHLY_BACKUPS_PATH + host_stamp)
                printYellow("Backup folder '" + data.MONTHLY_BACKUPS_PATH + host_stamp + "' has been created...")
            else:
                printGreen("Folder '" + data.MONTHLY_BACKUPS_PATH + host_stamp + "' exists, moving to the next step...")    
        else:
            printLightPurple("Skipping monthly backups folder '" + data.MONTHLY_BACKUPS_PATH + host_stamp + "' folder check / create step as this hasn't been defined...")
    else:
        printLightPurple("Skipping monthly backups as the rentention period is invalid, please change 'MONTHLY_BACKUPS_RETENTION_PERIOD'...")
else:
    printLightPurple("Skipping monthly folder '" + data.MONTHLY_BACKUPS_PATH + host_stamp + "' check / create step as this has been disabled...")


# for enabled_backups in backups_enabled_list:

#     if enabled_backups:

#         for defined_backup_paths in backups_path_check_list:

#             if backups_path_check_list:

#                 if not os.path.exists(defined_backup_paths):

#                     os.makedirs(defined_backup_paths + host_stamp)
#                     printYellow("Creating backup folders for " + defined_backup_paths + host_stamp + "...")

#                 else:

#                     printGreen("Folder " + defined_backup_paths + host_stamp + " exists, moving to the next step...")

#             else:

#                 printLightPurple("Skipping " + defined_backup_paths + host_stamp + " folder check / create step as this hasn't been defined...")

#     else:

#         printLightPurple("Skipping folder check / create step as this has been disabled...")

################

# for backup_path_defined in backup_path_check:

#     if not backup_path_defined:
#         printLightPurple("Skipping " + backup_path_defined + host_stamp + " folder check/create step as this hasn't been defined...")
#     else:

#         if data.DAILY_BACKUPS_ENABLED:

#             if not os.path.exists(backup_path_defined):
#                 os.makedirs(backup_path_defined + host_stamp)
#                 printYellow("Creating backup folders for " + backup_path_defined + host_stamp + "...")
#             else:
#                 printGreen("Folder " + backup_path_defined + host_stamp + " exists, moving to the next step...")
#         else:
#             printLightPurple("Skipping " + backup_path_defined + host_stamp + " folder check/create step as this has been disabled...")


























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