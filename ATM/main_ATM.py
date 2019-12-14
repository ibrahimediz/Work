def menu():
    mainMenu="""
                BOFA ATM\n
1- Balance Request
2- Deposit
3- WithDraw
4- Transfer Money Between My Accounts
5- Exit
"""
    print("-"*38,mainMenu,"-"*38,sep="")

def balance():

    print("."*25,"\n","Your Balance",sep="")
    print("Account 1 Balance: {}".format(lst[0]))
    print("Account 2 Balance: {}".format(lst[1]))

menu()
allow_Chracters="12345"
lst=[0,0]

def deposit():
    if menu_Question=="2":
        balance()
        menu_Question2=int(input("Which Account will you deposit? (1/2): "))

        if menu_Question2==1:
            menu_Question2_Q1=int(input("How Much Will You Deposit?: "))
            lst[0]=lst[0]+menu_Question2_Q1
            balance()
        elif menu_Question2==2:
            menu_Question2_Q2=int(input("How Much Will You Deposit?: "))
            lst[1]=lst[1]+menu_Question2_Q2
            balance()
def withDraw():
    if menu_Question=="3":
        balance()
        menu_Question3=int(input("Which Withdraws From Your Account? (1/2): "))

        if menu_Question3==1:
            menu_Question3_Q1=int(input("How Much Will You WithDraw?: "))
            if menu_Question3_Q1>lst[0]:
                print("Not Enough Balance!...")
            else:
                lst[0]-=menu_Question3_Q1
                balance()
        elif menu_Question3==2:
            menu_Question3_Q2=int(input("How Much Will You WithDraw?: "))
            if menu_Question3_Q2>lst[1]:
                print("Not Enough Balance!...")
            else:
                lst[0]-=menu_Question3_Q1
                balance()
                
def transferOwn():
    if menu_Question=="4":
        balance()
        menu_Question4=int(input("Withdraw Account: "))
        if menu_Question4==1:
            menu_Question4_Q1=int(input("Amount to Send: "))

            if menu_Question4_Q1>lst[0]:
                print("Not Enough Balance!...")
            else:
                lst[0]-=menu_Question4_Q1
                lst[1]+=menu_Question4_Q1

        elif menu_Question4==2:
            menu_Question4_Q2=int(input("Amount to Send: "))

            if menu_Question4_Q2>lst[1]:
                print("Not Enough Balance!...")
            else:
                lst[1]-=menu_Question4_Q2
                lst[0]+=menu_Question4_Q2
        balance()
def exitATM():
    if menu_Question=="5":
        soru=input("Are You Sure You Want to Exit ? (Y/N): ").upper()
        if soru=="Y":
            print("Exited...")
            exit()
while True:
    menu()
    menu_Question=input("Which Action Do You Want To Do?: ")
    if menu_Question not in allow_Chracters:
        print("Wrong Choose")

    if menu_Question=="1":
        balance()

    deposit()
    withDraw()
    transferOwn()
    exitATM()