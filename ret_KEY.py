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
    print(len(result_lst), "record(s) received")
    print("Used", elapse_time, "micro seconds")

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
    answers.close()
    db.close()
    if filetype == 'indexfile':
        indexfile.close()
    return


'''
def ret_RANGE(DB_FILE,filetype):
    
    again = True
    while again:
        print('Retrieve records with a given range of key values\n')
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
        
        answers = open('answers', 'a')
        
        thekey = str(input("Please enter your key: "))
        resultlist = []

        start_time = time.time()
        try:
            resultlist = db[thekey].decode(encoding = 'UTF-8')
            end_time = time.time()
            thekey = thekey.decode(encoding = 'UTF-8')
                
            resultlist = resultlist.split()                                                                      
            for data in resultlist:
                print(Given)
                answers.write(Given)
                answers.write('\n')
                print(data)     
                answers.write(data)
                answers.write('\n')
                print()
                answers.write('\n')  
                
        except:
            end_time = time.time()
            print('Key is not found\n')  
            

        if resultlist:
            
            for data in resultlist:
                print(data.decode(encoding ='UTF-8'))
                answers.write(data.decode(encoding ='UTF-8'))
                answers.write('\n')
                print(db[data].decode(encoding ='UTF-8'))     
                answers.write(db[data].decode(encoding ='UTF-8'))
                answers.write('\n')
                print()
                answers.write('\n')                     
            
        else:                              
            print("No matching results were found\n")                                        
                    
        time_used = end_time - start_time
        time_used *= 1000000 
            
        print("The program runs %.6f micro seconds"%time_used)            

        try:
            db.close()
        except:
            print("Error Occured")

                
        a = input("Do you want to perform another range search? y/n").lower
        while not (a == 'y' or a =='n'):
            a = input("Please enter y or n").lower
        if a == 'y':
            again = True
        else:
            again = False

    answers.close()
'''
