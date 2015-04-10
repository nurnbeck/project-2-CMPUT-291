import os
import time
import bsddb3 as bsddb

'''
Retrieve records with a given range of key values
- Modified and simplified based on the old bersion
- Has the same format and assumption as ret_DATA()

Tested under DB_SIZE = 10
'''

DB_FILE = "/tmp/yishuo_db/sample_db"
SDB_FILE = "/tmp/yishuo_db/IndexFile"

DB_SIZE = 100000
#DB_SIZE = 200

def ret_RANGE(filetype):
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
    while True:
        lower_bound = input("Please enter your lower bound > ")
        upper_bound = input("Please enter your upper bound > ")
        if lower_bound <= upper_bound:
            break
        else:
            print("Invalid input")
            continue
    if lower_bound == upper_bound:
        # This is the same as retrieve key
        # Same algorithm as ret_KEY()
        tkey = lower_bound
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
                answers.write('\n')

                answers.write('\n')
        else:
            print("Data not found")
    else:
        # This is when lower_bound < upper_bound
        if filetype == 'btree' or filetype == 'indexfile':
            key_lst = []
            for key in db.keys():
                key = key.decode(encoding = 'UTF-8')
                key_lst.append(key)
            left_bound = 0
            right_bound = len(key_lst) - 1
            index = -999
            start_time = time.time()
            while left_bound <= right_bound:
                mid = (left_bound + right_bound) // 2
                if lower_bound == key_lst[mid]:
                    index = mid
                    break
                elif lower_bound < key_lst[mid]:
                    right_bound = mid - 1
                    index = mid
                elif lower_bound > key_lst[mid]:
                    left_bound = mid + 1
                    index = mid + 1
            while key_lst[index] <= upper_bound and index < DB_SIZE- 1:
                result_lst.append(key_lst[index])
                index += 1
            end_time = time.time()
        elif filetype == 'hash':
            start_time = time.time()
            for key in db.keys():
                key = key.decode(encoding = 'UTF-8')
                if key <= upper_bound and key >= lower_bound:
                    result_lst.append(key)
            end_time = time.time()

        # Now we have result list for either case
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
