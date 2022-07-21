import book
import member
import issue

def Menubook():
    while True:
        book.clrscreen()
        print("\t\t\t Book Record Management\n")
        print("==========================================================")
        print("1. Add Book Record")
        print("2. Search Book Record")
        print("3. Delete Book Record")
        print("4. Update Book Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 -------> : "))
        if choice == 1:
            book.insertData()
        elif choice == 2:
            book.SearchBookRec()
        elif choice == 3:
            book.deleteBook()
        elif choice == 4:
            book.UpdateBook()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuMember():
    while True:
        book.clrscreen()
        print("\t\t\t Member Record Management\n")
        print("==========================================================")
        print("1. Add Member Record")
        print("2. Search Member Record")
        print("3. Delete Member Record")
        print("4. Update Member Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            member.insertMember()
        elif choice == 2:
            member.SearchMember()
        elif choice == 3:
            member.deleteMember()
        elif choice == 4:
            member.UpdateMember()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuIssueReturn():
    while True:
        book.clrscreen()
        print("\t\t\t Member Record Management\n")
        print("==========================================================")
        print("1. Issue Book")
        print("2. Search Issue Book Record")
        print("3. Return Issued Book")
        print("4. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 4 ------> : "))
        if choice == 1:
            issue.issueBook()
        elif choice == 2:
            issue.SearchIssuedBooks()
        elif choice == 3:
            issue.returnBook()
        elif choice == 4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")