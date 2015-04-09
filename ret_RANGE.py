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

#DB_SIZE = 100000
DB_SIZE = 200

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
        print(len(result_lst), "record(s) reveived")
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
                answers.write('\n')

                answers.write('\n')
        else:
            print("Data not found")
    else:
        # This is when lower_bound < upper_bound
        if filetype == 'btree':
            key_lst = []
            for key in db.keys():
                key = key.decode(encoding = 'UTF-8')
                key_lst.append(key)
            left_bound = 0
            right_bound = DB_SIZE - 1
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
    if type == '3' or type == 'indexfile' or type == 'i':
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
        
        lower_bound = str(input("Please enter your lower bound: "))
        upper_bound = str(input("Please enter your upper bound: "))
        resultlist = []
        
        if upper_bound < lower_bound:
            start_time = time.time()
            print("The bound is not valid, lower bound must be smaller\n")
            end_time = time.time()
                    
        elif upper_bound == lower_bound:
            thekey = upper_bound
            
            start_time = time.time()
            try:
                resultlist = db[thekey].decode(encoding = 'UTF-8')
                end_time = time.time()
                thekey = thekey.decode(encoding = 'UTF-8')
                
                resultlist = resultlist.split()                                                                      
                for data in resultlist:
                    print(thekey)
                    answers.write(thekey)
                    answers.write('\n')
                    print(data)     
                    answers.write(data)
                    answers.write('\n')
                    print()
                    answers.write('\n')  

            except:
                end_time = time.time()
                print('Key is not found\n')  
        
        else:  
            start_time = time.time()  
            if filetype == 'hash':  
                for i in key_list:          
                    if i<= upper_bound and i>= lower_bound:                 
                        resultlist.append(i)   
            else:
                    
                    left,right=0,len(key_list)-1
                    if left>right:
                        low = None
                    while left<=right:
                        mid=(left+right)//2
                        if lower_bound==key_list[mid]:
                            return mid
                        elif lower_bound<key_list[mid]:
                            right=mid-1
                            if right<0:
                                return 0
                            low=mid
                        elif lower_bound>key_list[mid]:
                            left=mid+1
                            if left>len(key_list)-1:
                                return False
                            low=mid+1
                
                while ((key_list[low] <= upper_bound) and (low < len(key_list)-1)):
                    resultlist.append(key_list[low])  
                    low += 1               
                    
                end_time = time.time()
                
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
            
            print("Number of records received: %d"%(len(resultlist))) 
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
