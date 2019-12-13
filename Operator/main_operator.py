minutes=1000
sms=1000
mb=5000

mbPrice=5
minPrice=50
smsPrice=50

monthlyStabil=30

    
def menu():
    print(
    " "*16,"OPERATOR NAME\n","="*50,"\n"," "*14,"Recipe Information\n",
"""
Talk Time Defined to Your Recipe: {} Min
Amount of messages defined in your recipe.: {} SMS
Internet Package Defined to Your Recipe: {} MB""".format(minutes,sms,mb),
"""
\nUsage Fee When Your Internet Is Over   :  For Every 100 Mb {} Cent
Usage Fee When Your Minutes Are Over  :  {} Cent/Min
Usage Fee When Your SMS is Done    :  {} Cent/SMS\n""".format(mbPrice,minPrice,smsPrice),
"_"*50,"\n"
"YOUR MONTHLY RECIPE  : {}".format(monthlyStabil),"$","\n",
"\nPlease query your invoice by entering usage amounts...\n")
menu()
minUse=int(input("Enter your monthly speaking minutes   : "))
smsUse=int(input("Enter amount of SMS you use monthly   : "))
mbUse=int(input("Enter your monthly amount of Internet : "))
print("\n","."*50,sep="")

def price():
    bill=30
    if minUse>minutes:
        minDiff=minUse-minutes
        minBill=(minDiff*minPrice)/100
        bill+=minBill
        print("SPEECH OVER LIMIT   : ",minDiff," "*10,"Extra pay: ",minBill,"$")

    if smsUse>sms:
        smsDiff=smsUse-sms
        smsBill=(smsDiff*smsPrice)/100
        bill+=smsBill
        print("SMS OVER LIMIT      : ",smsDiff," "*10,"Extra pay: ",smsBill,"$")

    if mbUse>mb:
        mbDiff=mbUse-mb
        mbBill=(mbDiff*mbPrice)/100
        bill+=mbBill
        print("INTERNET OVER LIMIT : ",mbDiff," "*10,"Extra pay: ",mbBill,"$")

    if bill<=monthlyStabil:
        print("IN YOUR RECIPE, THERE IS NO OVERDRAFT FEE :=)")

    print("TOTAL INVOICE AMOUNT: ","{} $".format(bill),"\n\n",">>>>>>>",sep="")

price()