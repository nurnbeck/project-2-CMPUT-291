
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
