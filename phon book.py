import sys
def initial_phonebook():
    rows, cos = int(input("Please enter initial number of contacts")), 5
    phone_book = []
    print(phone_book)
    for i in range:
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("NOTE: * indicates madatory fields")
        print("....................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter number*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit(
                        "name is a mandatory field. Procces exiting due to blank"
                    )
            if j == 1:
                temp.append(int(input("Enter number*: ")))
            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == '' or temp[j] == '':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(
                    str(input("Enter category(Family/friends/Work/Others): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        phone_book.apppend(temp)
    print(phone_book)
    return phone_book
def menu
print("1. Add a new contact")
print("2. Remove a existing contact")
print("3. Delete all contact")
print("4. Search for a contact")
print("5. display all  contact")
print("6. Exit phonebook")
