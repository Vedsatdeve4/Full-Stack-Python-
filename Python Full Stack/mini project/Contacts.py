
contacts = { 1234 : 'aabb' ,
             5678 : 'bbcc' ,
             9911 : 'ccaa' ,
             1111 : 'dddd'}

def show_contacts():
    if len(contacts) != 0:
        srno = 1
        print('\n SR','MONO','NAME')
        for mono,name in contacts.items():
                print(' ',srno,mono,name)
                srno += 1
    else:
        print(  "Please Add contacts")
                
    
        
def add_contacts(a,b):
    if a not in contacts:
         contacts[a] = b
         print("Contact ADDED...")
    else:
        print('This contact already exits')

        
def update_contacts(a,b):
    if a in contacts:
        contacts.update({a : b})
        print("Contact UPDATED...")
    else:
        print("No Such Number Exits in Contacts")

        
def delete_contacts(a):
    if a in contacts:
        contacts.pop(a)
        print("Contact Deleted ...")
    else:
        print("The Entered Number Does Not Exits")

def sort_in_ascending_contacts():
    print(sorted(contacts))

def sort_in_descending_contacts():
    print(sorted(contacts, reverse = True))

def search_contacts(a):
    if a in contacts:
        sc = contacts[a]
        print(mono , '=' , sc)
    else:
        print("There is no such contact")

while True:

    ch = int(input("\n Enter choice:\n1. Add New Contact\n2. Update A Contact \n3. Delete A Contact\n4. Show all Contacts\n5. Sorted in Ascending Contacts\n6. Sorted in Descending Contacts\n7. Search A Contact\n8. Exit"))

    if ch == 1:
        print("Add new Contact")
        mono = int(input("Enter a MONO to Add: "))
        name = input("Enter a NAME to Add: ")
        add_contacts(mono,name)
        

    elif ch == 2:
        print("Update A Contact") 
        mono = int(input("Enter a MONO to Add: "))
        name = input("Enter a new NAME to Add: ")
        update_contacts(mono,name)
        

    elif ch == 3:
        print("Delete A Contact")
        mono = int(input("Enter a MONO to Add: "))
        delete_contacts(mono)
        

    elif ch == 4:
        print("Show All Contacts")
        show_contacts()

    elif ch == 5:
        print("Sorted in Ascending Contacts")
        sort_in_ascending_contacts()

    elif ch == 6:
        print("Sorted in Descending Contacts")
        sort_in_descending_contacts()

    elif ch == 7:
        print("Search A Contact")
        mono = int(input("Enter a MONO to Add: "))
        search_contacts(mono)

    elif ch == 8:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
'''

contacts = {'1234' : 'aabb' ,
            '5678' : 'bbcc' ,
            '9911' : 'ccaa' ,
            '1111' : 'dddd'}

def show_contacts():
    if len(contacts) != 0:
        srno = 1
        print('\n SR','MONO','NAME')
        for mono,name in contacts.items():
                print(' ',srno,mono,name)
                srno += 1
    else:
        print(  "Please Add contacts")
                

while True:

    ch = int(input("\n Enter choice:\n1. Add New Contact\n2. Update A Contact \n3. Delete A Contact\n4. Show all Contacts\n5. Exit"))

    if ch == 1:
        print("Add new Contact")
        mono = input("Enter a MONO to Add: ")
        if mono in contacts:
            print(mono,"Already exists ")
        else:
            name = input("Enter a NAME to Add: ")
            contacts[mono] = name
            print("Contact ADDED...")
                    

    elif ch == 2:
        print("Update A Contact") 
        mono = input("Enter a MONO to Update: ")
        if mono in contacts:
            name = input("Enter a new NAME to Add: ")
            contacts.update({mono : name})
            print("Contact UPDATED...")
        else:
            print("No Such Number Exits in Contacts")
            
    elif ch == 3:
        print("Delete A Contact")
        mono = input("Enter a MONO to Add: ")
        if mono in contacts:
            contacts.pop(mono)
            print("Contact Deleted ...")
        else:
            print("The Entered Number Does Not Exits")
        

    elif ch == 4:
        print("Show All Contacts")
        show_contacts()

    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
'''
