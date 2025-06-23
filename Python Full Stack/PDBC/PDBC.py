import MySQLdb

conn = MySQLdb.connect(user='root', password ='pavaniswind', host ='localhost', db='b53db')

cur = conn.cursor()

while 1==1:

    ch = int(input('\n MENU'\
                   '\n1. Create table'\
                   '\n2. Insert Data'\
                   '\n3. Retrive Data'\
                   '\n4. Update Data'\
                   '\n5. Delete Data'\
                   '\n6. Exit'\
                   '\n Enter your choice'))

#CREATE
    if ch == 1:
        query = 'create table student(roll int,name varchar(80), marks float);'

        cur.execute(query)

#INSERT
    elif ch == 2:
        r = int(intput('Enter Student Roll:'))
        nm = intput('Enter Student Name:')
        m = float(input('Enter Student marks:'))

        query = f'insert into student values({r},"{nm}", {m});'
        cur.execute(query)

#RETRIVE
    elif ch == 3:
        ch1 = int(input('\n Do you want to Retrive Data:'\
                        '\n1. All Records'\
                        '\n2. Particular Records'\
                        '\n Enter your Choice: '))
        #ALL RECORDS
        if ch1 == 1:
            query = 'select * from student;'
            cur.execute(query)

            for record in cur:
                print('\n\n Student Information'\
                      f'\n Student Roll: {record[0]}'\
                      f'\n Student Name: {record[1]}'\
                      f'\n Student Marks: {record[2]}')

        #PARTICULAR RECORDS
        if ch1 == 2:
            pass

#UPDATE
    elif ch == 4:
        roll_ref = int(input('\n Enter Roll of Student whose record you want to Update: '))
        cur.execute('select roll from student;')

        for record in cur:
            if record[0] = roll_ref:
                ch1 = int(input('\n What do you want to update'\
                                '\n1. Name'\
                                '\n2. Marks'\
                                '\n Enter your Choice: '))
                # To Update Name
                if ch1 == 1:
                    name_new = input('\n Enter New Name to Update: ')

                    query = f'update student set name="{name_new}" where roll={roll_ref};'
                    cur.execute(query)

                # To Update Marks
                if ch1 == 2:
                    pass

#Delete
    elif ch == 5:
        ch1 = int(input('\n Do you want to Delete'\
                        '\n1. All Records'\
                        '\n2. Particular Record'
                        '\n3. Enter your choice:'))
        #To Delete All
        if ch1 == 1:
            query = 'delete from student;'
            cur.execute(query)

        #TO Delete Particular Record
        elif ch1 ==2:
            pass

#Exit
    elif ch == 6:
        break

#Defalut Block
    else:
        print('\n\t INVALID OPTION!!')

    conn.commit()
conn.close()
