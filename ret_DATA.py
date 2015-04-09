import os
import time
import bsddb3 as bsddb

'''
Retrieve records with a given data
- Assume that database is closed before calling ret_DATA();
- Writes (append) the result to the file 'answers'.

For now I assume that indexfile = btree, further tests are necessary.

Tested under DB_SIZE = 10
'''

DB_FILE = "/tmp/yishuo_db/sample_db"
SDB_FILE = "/tmp/yishuo_db/IndexFile"

def ret_DATA(filetype):
    '''
    try:
        if filetype == 'btree':
            db = bsddb.btopen(DB_FILE, 'r')
        elif filetype == 'hash':
            db = bsddb.hashopen(DB_FILE, 'r')
        elif filetype == 'indexfile':
            db = bsddb.btopen(DB_FILE, 'r')
    except:
        print("Unknown error occured, try again")
        return False
    '''
    if filetype == 'btree':
        db = bsddb.btopen(DB_FILE, 'r')
    elif filetype == 'hash':
        db = bsddb.hashopen(DB_FILE, 'r')
    elif filetype == 'indexfile':
        db = bsddb.btopen(SDB_FILE, 'r')
    else:
        print("Unknown type, function terminated\n")
        return

    # open answers for writing, appending to the end of the file
    answers = open('answers', 'a')

    result_lst = []
    '''
    # Prints out all the values in database
    # For test only
    # DO NOT use it if there are more than 20 keys in database
    print("******************************")
    for key in db.keys():
        str = db[key]
        str.decode(encoding = 'UTF-8')
        print("VALUE:", str)
    print("******************************")
    '''
    data = input("Enter the data you want to search > ")
    data = data.encode(encoding = 'UTF-8')
    start_time = time.time()
    for key in db.keys():
        if db[key] == data:
            result_lst.append(key.decode(encoding = 'UTF-8'))
    end_time = time.time()
    
    elapse_time = (end_time - start_time) * 1000000

    print(len(result_lst), "record(s) received")
    print("Used", elapse_time, "micro seconds")

    data = data.decode(encoding = 'UTF-8')

    if result_lst:
        for key in result_lst:
            print('Key:', key)
            answers.write(key)
            answers.write('\n')
            print('Data:', data)
            answers.write(data)
            answers.write('\n')
            
            answers.write('\n')
    else:
        print("Data not found")
        '''
        while True:
            inp = input("Do you want to write empty lines to answers (y/n) > ").lower()
            if inp == 'y' or inp == 'yes':
                answers.wirte('\n')
                answers.write('\n')
                answers.write('\n')
                break
            elif inp == 'n' or inp == 'no':
                break
            else:
                print("Please enter yes (y) or no (n)")
                continue
        '''
    print()
    answers.close()
    db.close()
    return


