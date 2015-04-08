import bsddb3 as bsddb
import random
import time
import sys
from bsddb3 import db

from cr_DB import *
from ret_DATA import *

#DATABASE = "cstudents.db“
#db = bsddb.hashopen(DATABASE, 'c') #this command create a hash db in file
#"cstudents.db“
#or db = bsddb.btopen(DATABASE, 'c') to create a B-Tree DB
#or db = bsddb.rnopen(DATABASE, 'c') to create a record format file
# Make sure you run "mkdir /tmp/my_db" first!
DB_FILE = "/tmp/my_db/sample_db"
SDB_FILE = "/tmp/my_db/IndexFile"
DB_SIZE = 100000
SEED = 10000000
database_exists = False # bool does database already exist
cur = None # cursor must be accessible by all functions
DATABASE = None # Not sure if this needs to be here, but playing it safe for now

def get_random():
    return random.randint(0, 63)
def get_random_char():
    return chr(97 + random.randint(0, 25))

'''
def cr_DB():
    return
'''
def ret_KEY():
    return
'''
def ret_DATA():
    return
'''
def ret_RANGE():
    return
def de_DB(indexfile = False):
    '''
    db.close()
    return
    '''
    # If there is an indexfile (indexfile = True) then remove it. Set initial value to False
    os.remove(DB_FILE)
    if indexfile:
        os.remove(SDB_FILE)
    return




def main():
    # initialze answer to an empty file
    answer = open('answers', 'w')
    answer.close()
    try:
        dbtype = sys.argv[1].lower()
    except:
        print("Usage: python3 main.py db_type_option")
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
                inp = input("Do you want to exit? ").lower()
                if inp == 'y' or inp == 'yes' or inp == 'q':
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
        elif inp == '2' or inp == 'k':
            pass
        elif inp == '3' or inp == 'r':
            if filetype == '' or filetype == False:
                print("Database may not exist, continue may cause program crash")
                while True:
                    inp = input("Do you wish to continue (y/n) > ").lower()
                    if inp == 'y' or inp == 'yes':
                        break
                    elif inp == 'n' or inp == 'no':
                        break
                    else:
                        print("Please enter yes (y) or no (n)")
                        continue
                if inp == 'n' or inp == 'no':
                    continue
            ret_DATA(DB_FILE, filetype)
        elif inp == '4' or inp == 'v':
            pass
        elif inp == '5' or inp == 'd':
            pass
        elif inp == '6' or inp == 'q':
            pass
        elif inp == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Invalid")
        print(inp)

    return
