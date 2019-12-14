import random
import time
class Fighters:
    roundx=1
    def __init__(self,name,strike,healt,specialpower):
        self.name=name
        self.strike=strike
        self.healt=healt
        self.specialpower=specialpower
        # self.message()

    @staticmethod
    def table():
        m1="Strike"
        m2="Healt"
        m3="S.Power"
        print("""                    --O-- FIGTH TABLE --O--                                         
                       +-------+-------+
        {} ({})   |       |       |    ({})  {}
        {}  ({})   |  P1   |   E1  |    ({}) {}
        {}({})   |       |       |    ({})  {}
                       +-------+-------+
        {} ({})    |       |       |    ({})  {}
        {}  ({})   |  P2   |   E2  |    ({}) {}
        {}({})   |       |       |    ({})  {}
                       +-------+-------+
        {} ({})    |       |       |    ({})  {}
        {}  ({})   |  P3   |   E3  |    ({}) {}
        {}({})   |       |       |    ({}) {}
                       +-------+-------+""".format(m1,P1.strike,E1.strike,m1,m2,P1.healt,E1.healt,m2,m3,P1.specialpower,E1.specialpower,m3,m1,P2.strike,E2.strike,m1,m2,P2.healt,E2.healt,m2,m3,P2.specialpower,E2.specialpower,m3,m1,P3.strike,E3.strike,m1,m2,P3.healt,E3.healt,m2,m3,P3.specialpower,E3.specialpower,m3))

    def attack(self,enemy):
        self.attackresult(enemy)

    def attackresult(self,enemy):
        enemy.healt-=self.strike

    def SuperPower(self):
        self.superAttack(attackChoose)
        self.SPcount=-1

    def superAttack(self,enemy):
        enemy.healt-=self.specialpower

    def SuperPower2(self):
        self.superAttack2(randomplayer)
        self.SPcount=-1

    def superAttack2(self,enemy):
        enemy.healt-=self.specialpower

    def result(self):
        print(self.name, "Healt: ",self.healt)

    def info(self,enemy):
        print("\n"," "*13,end="    ")
        print(self.name," ",end="")
        for i in "------attacking---> ":
            time.sleep(0.1)
            print(i,end="")
        print(" ",enemy.name,)
        print("\n"," "*21,"Round","[",Fighters.roundx,"]","Result")

    def message(self):
        for i in List+List2:
            if i.healt<=0:
                print(" "*26,end="")
                print("[",i.name,"]","is Defeat")

    def message2(self):
        print(" "*17,end="    ")
        print(self.name,"healt","[",self.healt,"]","left")

    def message3(self):
        for i in List+List2:
            if i.SPcount>=2:
                print(" "*20,"--",i.name,"Spc.Pow. Ready--")

    @staticmethod
    def winControl():
        a=0
        for i in List:
            if i.healt<=0:
                i.healt=0
            a+=i.healt
        if a<=0:
            print("PC Win")
            exit()
        b=0
        for i in List2:
            if i.healt<=0:
                i.healt=0
            b+=i.healt
        if b<=0:
            print("You Win")
            exit()

    @staticmethod
    def pc():
        teamChoose.attack(attackChoose)
        
class Player1(Fighters):
    SPcount=0
    def __init__(self,*args):
        super().__init__("P1",100,456,200)

class Player2(Fighters):
    SPcount=0
    def __init__(self,*args):
        super().__init__("P2",50,345,180)

class Player3(Fighters):
    SPcount=0
    def __init__(self,*args):
        super().__init__("P3",60,783,220)

class Enemy1(Fighters):
    SPcount=0
    def __init__(self,*args):
        super().__init__("E1",40,500,230)

class Enemy2(Fighters):
    SPcount=0
    def __init__(self,*args):
        super().__init__("E2",45,553,190)

class Enemy3(Fighters):
    SPcount=0
    def __init__(self,*args):
        super().__init__("E3",54,676,110)

P1=Player1()
P2=Player2()
P3=Player3()
E1=Enemy1()
E2=Enemy2()
E3=Enemy3()
Fighters.table()

while True:
    List=[P1,P2,P3]
    List2=[E1,E2,E3]
    teamChoose=eval(input("\nChoose Your Fighter: P1 or P2 or P3: ")) # büyük harf kullanamıyorum. nasıl yapabilirim?
    while teamChoose.healt<=0 or teamChoose not in List:
        print("Wrong Choose")
        teamChoose=eval(input("\nChoose Your Fighter: P1 or P2 or P3: ")) # büyük harf kullanamıyorum. nasıl yapabilirim?
    attackChoose=eval(input("\nWho will you attack?: "))
    while attackChoose.healt<=0 or attackChoose not in List2:
        print("Wrong Choose")
        attackChoose=eval(input("\nWho will you attack?: "))
    if teamChoose.SPcount>=2:
        sak=input("\nDo You Want Use SuperPower ?(Y/N): ").upper()
        if sak=="Y":
            Fighters.SuperPower(teamChoose)
            teamChoose.info(attackChoose)
            Fighters.table()

        elif sak=="N":
            print("You didn't want to use it. Normal attack")
            Fighters.pc()
            Fighters.table()

        else:
            Fighters.pc()
            Fighters.table()
    else:
        Fighters.pc()
        Fighters.table()

    Fighters.winControl()
    randompc=random.choice(List2)
    randomplayer=random.choice(List)

    while randompc.healt <=0:
        randompc=random.choice(List2)

    while randomplayer.healt <=0:
        randomplayer=random.choice(List)

    if randompc.SPcount>=2:
        Fighters.SuperPower2(randompc)

    elif randompc.SPcount<2:
        randompc.attack(randomplayer)

    randompc.info(randomplayer)
    Fighters.winControl()
    Fighters.message2(attackChoose)
    Fighters.message2(randomplayer)
    Fighters.message(randomplayer)
    teamChoose.SPcount+=1
    randompc.SPcount+=1
    Fighters.message3(teamChoose)
    Fighters.table()
    Fighters.roundx+=1