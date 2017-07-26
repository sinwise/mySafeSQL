#!/usr/bin/python

import os
import ConfigParser
import time
import datetime

#### Script Configuration ####

# DAILY_BACKUPS_ENABLED     = True      # Enable Daily Backups - True/False
# WEEKLY_BACKUPS_ENABLED        = True      # Enable Weekly Backups - True/False
# MONTHLY_BACKUPS_ENABLED       = True      # Enable Monthly Backups - True/False
# WEEKLY_BACKUPS_DAY        = 1         # 1 - Monday, 2, 3, 4, 5, 6, 7 - Sunday
# MONTHLY_BACKUPS_DATE      = 28        # 1 to 31
# DAILY_BACKUPS_RETENTION   = 7
# WEEKLY_BACKUPS_RETENTION  = 4
# MONTHLY_BACKUPS_RETENTION = 6
# DB_HOST           = 'localhost'
# DB_USER           = 'root'
# DB_USER_PASSWORD      = '_root_user_password_'
# DB_NAME           = 'databases.lst'
# BACKUP_PATH_DAILY     = '/mnt/mysql-backups/daily/' + os.getenv('HOSTNAME') + '/' + time.strftime('%d-%m-%Y') + '/'
# BACKUP_PATH_WEEKLY        = '/mnt/mysql-backups/weekly/' + os.getenv('HOSTNAME') + '/' + time.strftime('%d-%m-%Y') + '/'
# BACKUP_PATH_MONTHLY       = '/mnt/mysql-backups/monthly/' + os.getenv('HOSTNAME') + '/' + time.strftime('%d-%m-%Y') + '/'

#############################

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

#############################

backup_enabled      = [DAILY_BACKUPS_ENABLED, WEEKLY_BACKUPS_ENABLED, MONTHLY_BACKUPS_ENABLED]
backup_path_check   = [BACKUP_PATH_DAILY, BACKUP_PATH_WEEKLY, BACKUP_PATH_MONTHLY]

for backup_path_defined in backup_path_check:
    if not backup_path_defined:
        prLightPurple("Skipping" + backup_path_defined + " folder check/create step as this hasn't been defined...")
    else:
        if not os.path.exists(backup_path_defined):
                os.makedirs(backup_path_defined)
                    prYellow("Creating backup folders for " + backup_path_defined + "...")
        else:
            prGreen("Folder " + backup_path_defined + " already exists, moving to next step...")





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