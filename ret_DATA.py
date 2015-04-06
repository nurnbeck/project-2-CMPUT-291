import os
import time
import bsddb3 as bsddb

'''
Retrieve records with a given data
- Assume that database is closed before calling ret_DATA();
- Returns False if database open failed;
- Writes (append) the result to the file 'answers'.

For now I assume that indexfile = btree, further tests are necessary.

Not tested
'''

def ret_DATA(DB_FILE, filetype):
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

    # open answers for writing, appending to the end of the file
    answers = open('answers', 'a')

    result_lst = []
    data = input("Enter the data you want to search > ")
    
    start_time = time.time()
    for elem in db.keys():
        if db[key] == data:
            result_lst.append(elem.decode(encoding = 'UTF-8'))
    end_time = time.time()
    
    elapse_time = (end_time - start_time) * 1000000

    print(len(result_lst), "record(s) received")
    print("Used", elapse_time, "micro secnods")

    data = data.decode(encoding = 'UTF-8')

    if result_lst:
        for elem in result_lst:
            print('Elem', elem)
            answers.write(elem)
            answers.write('\n')
            print('Data', data)
            answers.write(data)
            answers.write('\n')
            
            answers.write('\n')
    else:
        print("Data not found")
        while True:
            inp = input("Do you want to write empty lines to answers (y/n) > ").lower
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

    answers.close()
    db.close()
    return True


