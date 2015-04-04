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
    """
    Creates and populates the database
    """
    # gets the type from the arguements used to run the program
    #type = input(" > ")
    #print("Type is {}",type)
    # Check if there is an existing database
    try:
        print ("Opening existing database.")
        DATABASE = db.DB()
        DATABASE.open(DB_FILE)
        # Database should not exist, if you hit this something is wrong
        print("error")
    except:
        # Create a database based on type
        DATABASE = db.DB()
        print ("Database doesn't exist. Creating a new one.")
        if "BTREE" in type or "btree" in type or "indexfile" in type:
            DATABASE.open(DB_FILE, None, db.DB_BTREE, db.DB_CREATE)
            if "indexfile" in type or "IndexFile" in type:
                SEC_DB = db.DB()
                SEC_DB.open(SDB_FILE, None, db.DB_BTREE, db.DB_CREATE)
                print("Creating Indexed Database. Please wait.")
            else:
                print("btree database created")
        elif "HASH" in type or "hash" in type:
            DATABASE.open(DB_FILE, None, db.DB_HASH, db.DB_CREATE)
            print("Creating Hash Table Database. Please wait.")
        else:
            print("Invalid type on execution, format should be ./mydbtest.py btree or hash or indexfile")
            return
    # This is taken from python example shown in lab, with changes for python3
    # Add records to the database
    lib.set_seed(SEED)
    #for index in range(DB_SIZE):
    index = 1
    while index <= DB_SIZE:
        krng = 64 + (lib.get_random() % 64)
        key = ""
        for i in range(krng):
            key = key + str(chr(lib.get_random_char()))
            vrng = 64 + (lib.get_random() % 64)
            value = ""
        for i in range(vrng):
            value = value + str(chr(lib.get_random_char()))
            # Change the string into bytes.
            key = key.encode('utf-8')
            value = value.encode('utf-8')
            # Add key,value pair to database only if key is unique.
        if (DATABASE.exists(key) == False):
            DATABASE.put(key,value)
            if "indexfile" in type:
                SEC_DB.put(value, key)
        else:
            while (DATABASE.exists(key) == True):
                print(key.decode('utf-8'), "cannot be added as it is a duplicate.")
                krng = 64 + (lib.get_random() % 64)
                key = ""
                for i in range(krng):
                    key = key + str(chr(get_random_char()))
                    key = key.encode('utf-8')
            if "indexfile" in type:
                SEC_DB.put(value, key)
                DATABASE.put(key,value)
            index = index + 1
    if "indexfile" in type:
        SEC_DB.close()
        print("Length of Database: ", len(DATABASE))
        DATABASE.close()
        return    
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
