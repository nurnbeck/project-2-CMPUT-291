import os
import time
import bsddb3 as bsddb

'''
Retrieve records with a given key
- Modified and simplified based on the old version
- Has the same format and assumption as ret_DATA()

Tested under DB_SIZE = 10
'''

DB_FILE = "/tmp/yishuo_db/sample_db"
SDB_FILE = "/tmp/yishuo_db/IndexFile"

def ret_KEY(filetype):

    if filetype == 'btree':
        db = bsddb.btopen(DB_FILE, 'r')
    elif filetype == 'hash':
        db = bsddb.hashopen(DB_FILE, 'r')
    elif filetype == 'indexfile':
        db = bsddb.btopen(DB_FILE, 'r')
        indexfile = bsddb.hashopen(SDB_FILE, 'r')
    else:
        print("Unknown type, function terminated\n")
        return

    answers = open('answers', 'a')
    result_lst = []
    tkey = input("Enter the key you want to search > ")
    tkey = tkey.encode(encoding = 'UTF-8')
    start_time = time.time()
    for key in db.keys():
        if tkey == key:
            result_lst.append(key.decode(encoding = 'UTF-8'))
    end_time = time.time()
    elapse_time = (end_time - start_time) * 1000000

    print("Result:")
    if result_lst:
        for key in result_lst:
            print('Key:', key)
            answers.write(key)
            answers.write('\n')
            key = key.encode(encoding = 'UTF-8')
            data = db[key]
            data = data.decode(encoding = 'UTF-8')
            print('Data:', data)
            answers.write(data)
            answers.write('\n')

            answers.write('\n')
    else:
        print("Data not found")
    print()
    print(len(result_lst), "record(s) received")
    print("Used", elapse_time, "micro seconds")
    print()
    answers.close()
    db.close()
    if filetype == 'indexfile':
        indexfile.close()
    return
