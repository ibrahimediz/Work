archive=[]
allowCharacters="123456"

def menu():
    print("_"*25,
"""\n\n      LIBRARY MENU
\n1- Add Books
2- Search Books
3- List All Authors
4- List All Books
5- Delete Book
6- Exit
""",
"_"*25,sep="")

def bookAdd():
    if menu_Choose=="1":
        bookAdd=input("Please enter the name of the book you want to add: ")
        writerAdd=input("Enter the Author of this Book: ")
        archive.append(tuple((bookAdd,writerAdd)))
        print("Listing Added ...")

def bookFind():
    if menu_Choose=="2":
        print("."*10)
        bookFind_Q=input("Enter the title of the book you are looking for: ")
        for i in archive:
            if bookFind_Q==i[0]:
                print("-->",i[0],"Author",i[1])

def allWriter():
    if menu_Choose=="3":
        dot=1
        print("."*10,"\n""AUTHORS")
        for i in archive:
            print(str(dot),"-",i[1])
            dot+=1
def allBook():
    if menu_Choose=="4":
        dot=1
        print("."*10,"\n""BOOKS")
        for i in archive:
            print(str(dot),"-",i[0])
            dot+=1

def delBook():
    if menu_Choose=="5":
        bookDelete=input("Enter the name of the book to be deleted: ")
        for i in archive:
            if bookDelete==i[0]:
                print(i[0],"Author",i[1])
        bookDelete_Q=input("Delete This Book ? (Y/N): ").upper()
        if bookDelete_Q=="Y":
            for i in archive:
                if bookDelete==i[0]:
                    archive.remove(i)
                    print("Record Deleted")

def exitLibrary():
    if menu_Choose=="6":
        eq=input("Are You Sure You Want To Exit? (Y/N): ").upper()
        if eq=="Y":
            exit()

while True:
    menu()
    menu_Choose=input("Please Select Your Transaction: ")
    
    if menu_Choose not in allowCharacters:
        print("Warning !!!. You Have Selected The Wrong Transaction. Please Try Again.")
    
    bookAdd()
    bookFind()
    allWriter()
    allBook()
    delBook()
    exitLibrary()