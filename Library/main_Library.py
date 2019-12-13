archive=[]
allowCharacters="123456"

def menu():
    print("_"*25,
"""\n\n      My Contacts
\n1- Add Person
2- Search Person
3- List All Persons
4- Delete Person
5- Exit
""",
"_"*25,sep="")

def personAdd():
    if menu_Choose=="1":
        personAdd=input("Please enter the name of person you want to add: ")
        phoneAdd=input("Enter the Phone Number of person: ")
        archive.append(tuple((personAdd,phoneAdd)))
        print("Listing Added ...")

def personFind():
    if menu_Choose=="2":
        print("."*10)
        personFind_Q=input("Enter the name of the Person you are looking for: ")
        for i in archive:
            if personFind_Q==i[0]:
                print(i[0],":",i[1])

def allPersons():
    if menu_Choose=="3":
        dot=1
        print("."*10,"\n""PERSONS")
        for i in archive:
            print(str(dot),"-",i[0],":",i[1])
            dot+=1

def delPerson():
    if menu_Choose=="4":
        bookDelete=input("Enter the name of the Person to be deleted: ")
        for i in archive:
            if bookDelete==i[0]:
                print(i[0],":",i[1])
        bookDelete_Q=input("Delete This Person ? (Y/N): ").upper()
        if bookDelete_Q=="Y":
            for i in archive:
                if bookDelete==i[0]:
                    archive.remove(i)
                    print("Record Deleted")

def exitContactList():
    if menu_Choose=="5":
        eq=input("Are You Sure You Want To Exit? (Y/N): ").upper()
        if eq=="Y":
            exit()

while True:
    menu()
    menu_Choose=input("Please Select Your Transaction: ")
    
    if menu_Choose not in allowCharacters:
        print("Warning !!!. You Have Selected The Wrong Transaction. Please Try Again.")
    
    personAdd()
    personFind()
    allPersons()

    delPerson()
    exitContactList()