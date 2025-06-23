class Student(BaseException):
    roll = 0
    name = " "
    marks = 0

    def __init__(self, r, nm, m):
        self.roll = r
        self.name = nm
        self.marks = m

    def __str__(self):
        return '\n Student Information '\
               f'\n Student ROLL no: {self.roll}'\
               f'\n Student NAME: {self.name}'\
               f'\n Student MARKS: {self.marks}'

Student_list = []


while 1 == 1: 
    ch = int(input('\n Menu'\
                   '\n1.Add Student'\
                   '\n2.Retrive Student'\
                   '\n3.Update Student'\
                   '\n4.Delete Student'\
                   '\n5.Exit'\
                   '\n  Enter your Choice: '))

## TO ADD
    if ch == 1:
        n = int(input("How many Students you want to add: "))

        for i in range(n):
            r = int(input("Enter Student roll no: "))
            nm = input("Enter Student name: ")
            m = input("Enter Student marks: ")

            obj = Student(r, nm, m)
            Student_list.append(obj)

##Retrive
    elif ch == 2:
        ch1 = int(input("\n Do you want to Retrive"\
                        "\n1. All Student"\
                        "\n2. Particular Student"
                        "\n   Enter your choice: "))
        if ch1 == 1:
            for stu in Student_list:
                print(stu)

        if ch1 == 2:
            roll_ref = int(input("Enter roll no of Student whose you want to Retrive: "))
            for stu in Student_list:
                if stu.roll == roll_ref:
                    print(stu)

##Update
    elif ch == 3:
        roll_ref = int(input("Enter roll no of Student whose you want to Update: "))
        for stu in Student_list:
            if stu.roll == roll_ref:

                ch1 = int(input('\n What do you want to update'\
                                "\n1. Name"\
                                "\n2. Marks"\
                                "\n3. Enter your choice: "))
                if ch1 == 1:
                    name_new = input("Enter new name: ")
                    stu.name = name_new

                if ch1 == 2:
                    marks_new = input("Enter new Marks: ")
                    stu.Marks = marks_new

##Delete
    elif ch == 4:
        ch1 = int(input("Do you want to Delete"\
                        "\n1. All Students"\
                        "\n2. Particular Student"\
                        "\n   Enter your Choice: "))
        if ch1 == 1:
            Student_list.clear()

        elif ch1 == 2:
            roll_ref = int(input("Enter roll no of Student whose you want to Delete: "))
            for stu in Student_list:
                if stu.roll == roll_ref:
                    Student_list.remove(stu)

##Exit
    elif ch == 5:
        print("Exiting.....")
        break

    else:
        print("Invalid choice")

















                    
    
            
