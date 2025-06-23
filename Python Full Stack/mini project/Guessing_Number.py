import random

while True:
    
    level = int(input("Enter level: \n1.Easy (1 to 10) \n2.Medium (1 to 100) \n3.Hard (1 to 1000)"))

    if level == 1:
        random_no = random.randint(1,10)
    elif level == 2:
        random_no = random.randint(1,100)
    elif level == 3:
        random_no = random.randint(1,1000)
    else:
        print("Invalid level, \n Starting level 1 Easy( 1 to 10 ): ")

    while True:
        guessed_no = int(input("Guess a number "))# 0 to exit

        '''if guessed_no == 0:
                print("Exiting")
                break'''
        if guessed_no < random_no:
                print("Sorry, too small")
        elif guessed_no > random_no:
                print("Sorry, too large")
        elif guessed_no == random_no:
                print("Congo!!! You Won")
                break

    cont = int(input("Do you want to play than 1 or 0: "))
    if cont == 1:
        continue
    else:
         break

