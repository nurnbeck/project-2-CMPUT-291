'''
Creates a database
Return type if a database is successfully created, otherwise return False
- Simplified based on older version;
- Tested under DB_SIZE = 10;
- Removes database file and directory if mkdir fails the first time;
- Does not handle duplicate keys so far. Will add that feature later;
- Only supports btree and hash, further tests are necessory in order to create indexfile;
- Closes the database before function return.
'''

import os
import random
import bsddb3 as bsddb

DIR = "/tmp/yishuo_db/"
DB_FILE = "/tmp/yishuo_db/sample_db"
SDB_FILE = "/tmp/yishuo_db/IndexFile"

#DB_SIZE = 100000
DB_SIZE = 200
SEED = 10000000

def get_random():
    return random.randint(0, 63)

def get_random_char():
    return chr(97 + random.randint(0, 25))

def createdb(type):
    print("\nCreate database")
    # Create a directory, mkdir = 0 if one is successfully created
    mkdir = os.system('mkdir %s' %(DIR))
    if mkdir != 0:
        # This is when the directory already exist
        print("Remove database and directory\n")
        mkdir = os.system('rm -f %s' %(DB_FILE))
        mkdir = os.system('rm -f %s' %(SDB_FILE))
        mkdir = os.system('rmdir %s' %(DIR))
        mkdir = os.system('mkdir %s' %(DIR))
        if mkdir != 0:
            # This is when second mkdir failed, unknow error occured
            print("mkdir failed, unknown error occured")
            return False

    # if database exists then overwrite it
    if type == '1' or type == 'btree' or type == 'b':
        # create btree db
        db = bsddb.btopen(DB_FILE, 'c')
    elif type == '2' or type == 'hash' or type == 'h':
        # create hash db
        db = bsddb.hashopen(DB_FILE, 'c')
    elif type == '3' or type == 'indexfile' or type == 'i':
        db = bsddb.btopen(DB_FILE, 'c')
        indexfile = bsddb.hashopen(SDB_FILE, 'c')

    random.seed(SEED)
    for i in range(DB_SIZE):
        krng = 64 + get_random()
        key = ''
        for j in range(krng):
            key += str(get_random_char())
        print("KEY:", key)
        vrng = 64 + get_random()
        value = ''
        for j in range(vrng):
            value += str(get_random_char())
        print("VALUE:", value)
        print()
        key = key.encode(encoding = 'UTF-8')
        value = value.encode(encoding = 'UTF-8')
        db[key] = value
        
    db.close()
    if type == '3' or type == 'indexfile' or type == 'i':
        indexfile.close()
    print("\nDatabase created, type:", type, "\n")
    return type



'''
def cr_DB():
    """
    Creates and populates the database
    """
    #gets the type from the arguements used to run the program
    type = input(" select DB type > ").lower()
    while (1 = 1):
        if ( type == 'btree' ):
            break
        if ( type == 'indexfile' ):
            break
        if ( type == 'hash' ):
            break
        type = input(" select DB type (btree, hash, or indexfile) > ").lower()
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
        if "btree" in type or "indexfile" in type:
            DATABASE.open(DB_FILE, None, db.DB_BTREE, db.DB_CREATE)
            if "indexfile" in type :
                SEC_DB = db.DB()
                SEC_DB.open(SDB_FILE, None, db.DB_BTREE, db.DB_CREATE)
                print("Creating Indexed Database. Please wait.")
            else:
                print("btree database created")
        elif "hash" in type:
            DATABASE.open(DB_FILE, None, db.DB_HASH, db.DB_CREATE)
            print("Creating Hash Table Database. Please wait.")
        else:
            print("Invalid type on execution, format should be ./mydbtest.py btree or hash or indexfile")
            return
    # This is taken from python example shown in lab, with changes for python3
    # Add records to the database
    #set_seed(SEED)
    #for index in range(DB_SIZE):
    index = 1
    while index <= DB_SIZE:
        krng = 64 + (get_random() % 64)
        key = ""
        for i in range(krng):
            key = key + str(chr(get_random_char()))
            vrng = 64 + (get_random() % 64)
            value = ""
        for i in range(vrng):
            value = value + str(chr(get_random_char()))
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
                krng = 64 + (get_random() % 64)
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
'''
