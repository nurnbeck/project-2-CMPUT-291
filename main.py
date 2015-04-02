import bsddb
DATABASE = "cstudents.db“
#db = bsddb.hashopen(DATABASE, 'c') #this command create a hash db in file
#"cstudents.db“
#or db = bsddb.btopen(DATABASE, 'c') to create a B-Tree DB
#or db = bsddb.rnopen(DATABASE, 'c') to create a record format file





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
            
        elif inp == '4' or inp == 'v':
            
        elif inp == '5' or inp == 'd':
            
        elif inp == '6' or inp == 'q':
                        
        else:
            print("Invalid")
        print(inp)

    return
