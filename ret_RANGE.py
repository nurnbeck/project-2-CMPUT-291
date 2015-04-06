import os
import time
import bsddb3 as bsddb


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
            Given = upper_bound
            
            start_time = time.time()
            try:
                resultlist = db[Given].decode(encoding = 'UTF-8')
                end_time = time.time()
                Given = Given.decode(encoding = 'UTF-8')
                
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
