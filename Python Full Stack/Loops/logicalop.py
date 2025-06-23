n = int(input("Enter any no: "))
if n%5 == 0 and n%11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("not Divisible by both 5 and 11")

print()
y = int(input("Enter any year"))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
