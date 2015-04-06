import bsddb3 as bsddb
import random
import time
from bsddb3 import db

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


def cr_DB():
  
def ret_KEY():
    return
'''
def ret_DATA():
    return
'''
def ret_RANGE():
    return
def de_DB():
    db.close()
    return




def main():
    if connection == 0:
        print("Bye")
        return
    

    while True:
        print("1. Create and populate a database (c)")
        print("2. Retrieve records with a given key (k)")
        print("3. Retrieve records with a given data (r)")
        print("4. Retrieve records with a given range of key values (v)")
        print("5. Destroy the database (d)")
        print("6. Quit (q)") 
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
            
        elif inp == '2' or inp == 'k':
            
        elif inp == '3' or inp == 'r':
            # I passed filetype as a parameter into the function, which determines the type of database, 
            #   i.e. filetype = 'btree' or filetype = 'hash' or filetype = 'indexfile'
            # We don't have this variable yet, so maybe consider to have one in cr_DB()?
            ret_DATA(DB_FILE, filetype)
        elif inp == '4' or inp == 'v':
            
        elif inp == '5' or inp == 'd':
            
        elif inp == '6' or inp == 'q':
                        
        else:
            print("Invalid")
        print(inp)

    return
