# from databases import Database
# import Database
import menulib
import book
import issue

# Database.DatabaseCreate()
# Database.TablesCreate()


while True:
    book.clrscreen()
    print("\t\t\t Library Management\n")
    print("=====================================================================")
    print("1. Book Management")
    print("2. Members Management")
    print("3. Issue/Return Book")
    print("4. Exit")
    choice = int(input("Enter Choice between 1 to 4 -------> : "))
    if choice == 1:
        menulib.Menubook()
    elif choice == 2:
        menulib.MenuMember()
    elif choice == 3:
        menulib.MenuIssueReturn()
    elif choice == 4:
        break
    else:
        print("Wrong Choice.....Enter Your Choice again")
        x = input("Press any key to continue")