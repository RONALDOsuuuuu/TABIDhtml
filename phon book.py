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
def menu():
    print("1. Add a new contact")
    print("2. Remove a existing contact")
    print("3. Delete all contact")
    print("4. Search for a contact")
    print("5. display all  contact")
    print("6. Exit phonebook")
def add_contact(pb):
	dip = [] 
	for i in range(len(pb[0])): 
		if i == 0: 
			dip.append(str(input("Enter name: "))) 
		if i == 1: 
			dip.append(int(input("Enter number: "))) 
		if i == 2: 
			dip.append(str(input("Enter e-mail address: "))) 
		if i == 3: 
			dip.append(str(input("Enter date of birth(dd/mm/yy): "))) 
		if i == 4: 
			dip.append( 
				str(input("Enter category(Family/Friends/Work/Others): "))) 
	pb.append(dip) return pb
def remove_existing(pb):
        query = str(
            input("Please enter the name of the contact you wish to remove: "))
        temp = 0
        for i in range(len(pb)):
            if query == pb[i][0]:
               temp += 1
               print(pb.pop(i))
               print("This query has now been removed")
               return pb
        if temp == 0:
           print("Sorry, you have entered a invalid query.\nPlease recheck and try again latter.")
           return pb
def delete_all(pb):
    return p.clear()
def search_existing(pb):
    choice = int(input("Enter search critaria\n\n\n 1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\ \nPlease enter:"))
    temp = []
    check = -1
    if choice == 1:
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = str(input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
            query = str(input("Please enter the email ID\ of the contact you wish to search: "))
            for i in range(len(pb)):
                if query == pb[i][2]:
                    check = i
                    temp.append(pb[i])
    elif choice == 4:
            query = str(input("Please enter the DOB (in dd/mm/yy format ONLY) of the contact you wish to search: "))
            for i in range(len(pb)):
                    if query == pb[i][3]:
                        check = i
                        temp.append(pb[i])
    elif choice == 5:
           query = str(input("Please enter the category of the contact you wish to search: "))
    for i in range(len(pb)):
            if query == pb[i][4]:
                        check = i
                        temp.append(pb[i])
    else:
        print("Invalid searched criteria")
        return -1
    if check == -1:
        return -1
    else:
        display_all(tamp)
        return check
def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])
def thanks():
    print("Please visit again")
    sys.exit("Good bye, have a nice day ahead")
ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
     ch = menu