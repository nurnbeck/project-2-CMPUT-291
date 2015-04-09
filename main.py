#! /usr/bin/env python3

import bsddb3 as bsddb
import random
import time
import sys
from bsddb3 import db

from cr_DB import *
from ret_KEY import *
from ret_DATA import *
from ret_RANGE import *

DIR = "/tmp/yishuo_db/"
DB_FILE = "/tmp/yishuo_db/sample_db"
SDB_FILE = "/tmp/yishuo_db/IndexFile"

def de_DB():

    mkdir = os.system('rm -f %s' %(DB_FILE))
    mkdir = os.system('rm -f %s' %(SDB_FILE))
    print("Database now destroyed\n")
    return

def main():
    # initialze answer to an empty file
    answer = open('answers', 'w')
    answer.close()
    try:
        dbtype = sys.argv[1].lower()
    except:
        print("Usage: ./mydbtest db_type_option")
        return

    filetype = ''

    if dbtype == '-btree' or dbtype == 'btree' or dbtype == '-b':
        dbtype = 'btree'
    elif dbtype == '-hash' or dbtype == 'hash' or dbtype == '-h':
        dbtype = 'hash'
    elif dbtype == '-indexfile' or dbtype == 'indexfile' or dbtype == '-i':
        dbtype = 'indexfile'
    else:
        print("Usage: python3 main.py db_type_option")
        return

    while True:
        print("1. Create and populate a database (c)")
        print("2. Retrieve records with a given key (k)")
        print("3. Retrieve records with a given data (r)")
        print("4. Retrieve records with a given range of key values (v)")
        print("5. Destroy the database (d)")
        print("6. Quit (q)") 
        print("type cls to clear screen")
        inp = input("Enter your choice: ").lower()
        if inp == 'q' or inp == 'quit' or inp == "6":
            while True:
                if filetype == '' or filetype == False:
                    inp = input("Do you want to exit > ").lower()
                    if inp == 'y' or inp == 'yes' or inp == 'q':
                        print("Quit")
                        return
                    elif inp == 'n' or inp == 'no':
                        break
                    else:
                        print("Please enter yes (y) or no (n)")
                        continue
                else:
                    inp = input("Database exists, do you want to destroy it and exit > ").lower()
                    if inp == 'y' or inp == 'yes' or inp == 'q':
                        print("Destroy database and quit")
                        de_DB()
                        print("Quit")
                        return
                    elif inp == 'n' or inp == 'no':
                        break
                    else:
                        print("Please enter yes (y) or no (n)")
                        continue
            continue
        elif inp == '1' or inp == 'c':
            filetype = createdb(dbtype)
            print('filetype:', filetype)
        elif inp == '2' or inp == 'k':
            if filetype == '' or filetype == False:
                print("Database does not exist, create one first")
            else:
                ret_KEY(filetype)
        elif inp == '3' or inp == 'r':
            if filetype == '' or filetype == False:
                print("Database does not exist, create one first")
            else:
                ret_DATA(filetype)
        elif inp == '4' or inp == 'v':
            if filetype == '' or filetype == False:
                print("Database does not exist, create one first")
            else:
                ret_RANGE(filetype)
        elif inp == '5' or inp == 'd':
            # destroy database, update the filetype
            de_DB()
            filetype = ''
        elif inp == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Invalid input")
    return

if __name__ == "__main__":
    main()
